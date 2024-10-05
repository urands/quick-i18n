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
    current_language='en',
    dev_mode=True  # Set to False in production
)

# Set the current language
t.set_language('es')

# Get translations
print(t('Welcome to quick-i18n sample.'))  # Translates based on the current language

# Use formatting in translations
print(t('greeting', name='Alice'))
```


## Development Mode
When dev_mode is set to True, missing translation keys are automatically added to all language files, 
making it easier to manage translations during development.


## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any improvements or bug fixes.