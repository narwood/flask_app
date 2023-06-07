"""Contains functions that translate text between french and english."""

from deep_translator import MyMemoryTranslator

def englishToFrench(english_text):
    """Translates english text to french text."""
    french_text = MyMemoryTranslator(source='english', target='french').translate(english_text)
    return french_text

def frenchToEnglish(french_text):
    """Translates french text to english text."""
    english_text = MyMemoryTranslator(source='french', target='english').translate(french_text)
    return english_text
