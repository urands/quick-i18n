# main.py

from i18n import t

# List of languages to test
languages = ['en', 'es', 'ch', 'ru']

# Test the translations for each language
for lang in languages:
    t.set_language(lang)
    print(t('Language: {}',lang))
    print(t('Welcome to our application!'))
    print(t('greeting', name='Alice'))
    print('-' * 30)