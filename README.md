# quick-i18n

**quick-i18n** is a simple and efficient internationalization (i18n) library for Python applications. It allows you to manage translations using JSON files, supports dynamic language switching, and provides formatting for translation strings.

## Features

- Simple setup and integration
- Supports multiple languages with dynamic switching
- Uses JSON files for storing translations
- Automatic handling of missing translations in development mode
- Supports positional and keyword arguments for string formatting
- Domain separation for organizing translations
- Customizable translation directories

## Installation

Install the package via pip:

```bash
pip install quick-i18n
```

## Usage

```python
from quicki18n import i18n

# Initialize the i18n class
t = i18n(
    languages=['en', 'es'],
    default_language='en',
    default_domain="default",
    dev_mode=True  # Set to False in production
)

# Set the current language
t.set_language('es')

# Get translations
print(t('Welcome to our application!'))  # Translates based on the current language

# Use formatting in translations
print(t('Greeting, {name}', name='Alice', domain='messages'))
```

After execution quick-i18n generate for You json files:

```json
{
  "default": {
    "welcome-to-our-application": "Welcome to our application!"
  },
  "messages": {
    "greeting-name": "Greeting, {name}!"
  }
}
```

## Development Mode

When dev_mode is set to True, missing translation keys are automatically added to all language files,
making it easier to manage translations during development.


## Recommendations for organizing file structure

When integrating the quick-i18n package into your Python project, it's important to organize your files and
directories effectively to ensure maintainability and scalability. This guide provides recommendations for 
structuring your project to make the most out of quick-i18n.

### Project Structure

A well-organized project structure enhances readability and maintainability. Here's a recommended structure 
when using quick-i18n:
```scss
your_project/
├── app/
│   ├── __init__.py
│   ├── i18n.py
│   ├── main.py
│   └── ... (other modules)
├── translations/
│   ├── en.json
│   ├── es.json
│   ├── ru.json
│   └── ... (other language files)
├── requirements.txt
├── README.md
└── ... (other files)
```
- `app/`: Contains your application code.
- `translations/`: Stores your translation JSON files.
- `requirements.txt`: Lists your project dependencies.
- `README.md`: Provides information about your project.

### Translation Files

Place or generate your translation files in a dedicated translations/ 
directory at the root of your project. Each language has its own 
JSON file named after its language code (e.g., en.json for English).

Example en.json:
```json
{
  "default": {
    "welcome": "Welcome to our application!",
    "farewell": "Goodbye, {name}!"
  },
  "errors": {
    "not_found": "The requested item was not found.",
    "unauthorized": "You are not authorized to perform this action."
  }
}
```

es.json
```json
{
  "default": {
    "welcome": "¡Bienvenido a nuestra aplicación!",
    "farewell": "¡Adiós, {name}!"
  },
  "errors": {
    "not_found": "El elemento solicitado no fue encontrado.",
    "unauthorized": "No estás autorizado para realizar esta acción."
  }
}


```

### Initializing quick-i18n
Initialize quick-i18n in a central location within your application, such as the __init__.py file of your app/ package 
or a dedicated module (e.g., app/i18n.py).

```python 
# app/i18n.py

import os
from quicki18n import i18n

# Determine the path to the translations directory
translations_path = os.path.join(os.path.dirname(__file__), '..', 'translations')

# Initialize the i18n instance
t = i18n(
    languages=['en', 'es', 'ru'],
    default_language='en',
    dev_mode=False,  # Set to True during development
    translations_path=translations_path
)
```
- languages: List of supported language codes.
- current_language: Default language for your application.
- dev_mode: When True, missing translation keys are added automatically.
- translations_path: Path to your translations/ directory.

### Using Translations in Your Code
Import the translation instance t and use it to fetch translations within your application modules.

```python
# app/main.py

from . import t

def greet_user(name):
    welcome_message = t('default.welcome')
    personalized_farewell = t('default.farewell', name=name)
    print(welcome_message)
    print(personalized_farewell)

if __name__ == "__main__":
    t.set_language('es')  # Set language to Spanish
    greet_user('Carlos')


```

Output:
```css
¡Bienvenido a nuestra aplicación!
¡Adiós, Carlos!
```
## Best Practices
1. **Consistent Key Naming:**
Use dot notation to organize translation keys into namespaces (e.g., default.welcome, errors.not_found).
Keep key names consistent across all language files.
2. **Placeholder Usage:**
Use placeholders for dynamic content in your translations.
Support both positional ({}) and keyword ({name}) placeholders.
Ensure placeholders are consistent in all translations for a key.
3. **Language Codes:**
Use standard ISO 639-1 language codes (e.g., en for English, es for Spanish).
This ensures compatibility and clarity.
4. **Development Mode:**
Enable dev_mode during development to automatically add missing keys.
Remember to disable dev_mode in production to prevent unintended file modifications.
5. **Translation Updates:**
When adding new translations, update all language files to keep them in sync.
Use empty strings or the original text as placeholders until translations are available.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any improvements or bug fixes.
