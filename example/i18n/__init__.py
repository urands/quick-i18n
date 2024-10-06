# i18n/__init__.py

from quicki18n import i18n
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
