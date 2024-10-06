import os
import json
from slugify import slugify

class i18n:
    def __init__(self, languages, default_language=None, dev_mode=False, default_domain='default', translations_path=None):
        """
        Initialize the i18n class.

        :param languages: List of language codes (e.g., ['en', 'ru'])
        :param current_language: The current language code (e.g., 'en')
        :param dev_mode: If True, missing tags will be added to all JSON files
        :param default_domain: Default domain for translations
        :param translations_path: Path to the directory for translation files
        """
        self.languages = languages
        self.default_language = default_language if default_language in languages else languages[0]
        self.current_language = self.default_language
        self.dev_mode = dev_mode
        self.translations = {}
        self.default_domain = default_domain

        # Set the base path for translations
        if translations_path:
            self.base_path = os.path.abspath(translations_path)
        else:
            # Default to the current working directory where the class is instantiated
            self.base_path = os.path.join(os.getcwd(), 'translation')

        # Create the translation directory if it doesn't exist
        os.makedirs(self.base_path, exist_ok=True)

        # Load translations for each language
        for lang in self.languages:
            self._load_language(lang)

    def set_language(self, lang):
        """
        Set the current language.

        :param lang: Language code to set as current language
        """
        if lang in self.languages:
            self.current_language = lang
        else:
            raise ValueError(f"Language '{lang}' is not in the list of supported languages.")

    def get_language(self):
        """
        Get the current language.

        :return: Current language code
        """
        return self.current_language

    def _load_language(self, lang):
        """
        Load translations for a specific language from a JSON file.

        :param lang: Language code (e.g., 'en' or 'ru')
        """
        lang_file = os.path.join(self.base_path, f"{lang}.json")
        if os.path.exists(lang_file):
            with open(lang_file, 'r', encoding='utf-8') as f:
                self.translations[lang] = json.load(f)
        else:
            self.translations[lang] = {}
            # Create an empty translation file in development mode
            if self.dev_mode:
                with open(lang_file, 'w', encoding='utf-8') as f:
                    json.dump({}, f, ensure_ascii=False, indent=4)

    def __call__(self, tag_or_text, *args, lang=None, domain=None, **kwargs):
        """
        Return the translation for a given tag or text and language.

        :param tag_or_text: Translation tag or direct text
        :param args: Positional arguments for formatting
        :param lang: Language code (defaults to current language)
        :param domain: Domain or namespace for translations
        :param kwargs: Keyword arguments for formatting
        :return: Translated string or the original text if not found
        """
        if lang is None:
            lang = self.current_language

        if lang not in self.languages:
            lang = self.default_language  # Use the first language as default

        if domain is None:
            domain = self.default_domain

        # Check if input is a tag (no spaces) or direct text
        if self._is_tag(tag_or_text):
            tag = tag_or_text
        else:
            # Treat input as direct text, generate a slugified key
            tag = slugify(tag_or_text)
        # Prepend domain to the tag
        if domain:
            tag = f"{domain}.{tag}"
        # In development mode, add the tag and original text to translations
        if self.dev_mode:
            self._add_translation_to_all_languages(tag, tag_or_text)

        translation = self._get_translation(tag, lang)

        if translation is None:
            if self.dev_mode:
                # Add missing tag to all JSON files with the value
                self._add_translation_to_all_languages(tag, tag)
            # Return the original text if translation is missing
            translation = tag_or_text

        # If formatting arguments are provided, format the translation string
        if args or kwargs:
            try:
                translation = translation.format(*args, **kwargs)
            except (KeyError, IndexError) as e:
                # Handle missing keys or indices in formatting arguments
                raise ValueError(f"Formatting error in translation '{translation}': {e}")

        return translation

    def _is_tag(self, text):
        """
        Determine if the text should be considered a tag.

        :param text: Input text
        :return: True if text is a tag (no spaces), False otherwise
        """
        return ' ' not in text and text.lower() == text

    def _get_translation(self, tag, lang):
        """
        Recursively retrieve the translation for a tag.

        :param tag: Translation tag
        :param lang: Language code
        :return: Translated string or None if not found
        """
        keys = tag.split('.')
        current = self.translations.get(lang, {})
        for key in keys:
            if key in current:
                current = current[key]
            else:
                return None
        if isinstance(current, str):
            return current
        else:
            return None

    def _add_translation_to_all_languages(self, tag, value):
        """
        Add a missing tag to all translation dictionaries and save them to files.

        :param tag: Translation tag
        :param value: Value to assign to the tag in all languages
        """
        for lang in self.languages:
            self._add_translation(tag, lang, value)

    def _add_translation(self, tag, lang, value):
        """
        Add a missing tag to the translations dictionary and save it to the file.

        :param tag: Translation tag
        :param lang: Language code
        :param value: Value to assign to the tag
        """
        keys = tag.split('.')
        current = self.translations[lang]
        for key in keys[:-1]:
            current = current.setdefault(key, {})
        last_key = keys[-1]
        if last_key not in current or current[last_key] == "":
            current[last_key] = value
            self._save_language(lang)

    def _save_language(self, lang):
        """
        Save translations for a specific language to a JSON file, sorting the keys.

        :param lang: Language code
        """
        lang_file = os.path.join(self.base_path, f"{lang}.json")
        with open(lang_file, 'w', encoding='utf-8') as f:
            json.dump(
                self._sort_dict(self.translations[lang]),
                f,
                ensure_ascii=False,
                indent=4
            )

    def _sort_dict(self, obj):
        """
        Recursively sort a dictionary by its keys.

        :param obj: Dictionary to sort
        :return: Sorted dictionary
        """
        if isinstance(obj, dict):
            return {k: self._sort_dict(obj[k]) for k in sorted(obj)}
        else:
            return obj
