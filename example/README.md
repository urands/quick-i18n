## Introduction

The i18n class provides a simple and efficient way to manage internationalization (i18n) in Python applications. It allows you to handle translations for multiple languages using JSON files. This documentation will guide you through setting up the i18n class, configuring translations, and using it in your application.

## Directory Structure

Organize your project with the following structure:

```css
project/
├── i18n/
│   ├── __init__.py
│   ├── i18n.py
│   └── translation/
│       ├── en.json
│       ├── es.json
│       ├── ch.json
│       └── ru.json
└── main.py

```

- `i18n/`: The package containing the i18n class and translation files.
- `main.py`: The main script demonstrating how to use the i18n class.

## Setting Up the i18n Class

`i18n/__init__.py`

In this file, initialize the i18n class and configure it to use the translation directory within the same folder, including the languages 'en', 'es', 'ch', and 'ru'.

```python
# i18n/__init__.py

from .i18n import i18n
import os

# Determine the path for the translations directory within the package
translations_path = os.path.join(os.path.dirname(__file__), 'translation')

# Initialize the i18n instance
t = i18n(
    languages=['en', 'es', 'ch', 'ru'],
    default_language='en',
    dev_mode=True,  # Set to False in production
    translations_path=translations_path
)

# Expose the instance for import
__all__ = ['t']
```

This file contains the full implementation of the i18n class.

## Using the i18n Class in Your Application

Create a main.py file to demonstrate how to use the i18n class.

`main.py`

```python
# main.py

from i18n import t

# Test the translations for each language
for lang in t.languages:
    t.set_language(lang)
    print(t('default.language', lang))
    print(t('default.welcome-to-our-application'))
    print(t('greeting', 'Alice'))
    print('-' * 30)


```

#### Output

```bash
Language: en
Welcome to our application!
Hello, Alice!
------------------------------
Idioma: es
¡Bienvenido a nuestra aplicación!
¡Hola, Alice!
------------------------------
语言：ch
欢迎使用我们的应用程序！
你好，Alice！
------------------------------
Язык: ru
Добро пожаловать в наше приложение!
Привет, Alice!
------------------------------
```

[!NOTE]
Remember to install `pip install quick-i18n` and its dependencies before running your application.

## Conclusion

The i18n class provides a simple yet powerful way to manage internationalization in your Python applications. By using JSON files for translations and providing dynamic language switching and string formatting, it makes it easy to support multiple languages and enhance the user experience.
