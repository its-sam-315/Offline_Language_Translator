import argostranslate.package
import argostranslate.translate

# Load installed languages
installed_languages = argostranslate.translate.get_installed_languages()

# Print installed translation pairs (older compatible way)
print("Installed Translation Pairs:")
for from_lang in installed_languages:
    for to_lang in installed_languages:
        try:
            translation = from_lang.get_translation(to_lang)
            if translation:
                print(f"{from_lang.code} → {to_lang.code}")
        except:
            pass

# Translate English to Hindi
from_lang = next((lang for lang in installed_languages if lang.code == "en"), None)
to_lang = next((lang for lang in installed_languages if lang.code == "hi"), None)

if from_lang and to_lang:
    translation = from_lang.get_translation(to_lang)
    output = translation.translate("I love programming.")
    print("Original (en): I love programming.")
    print("Translated (hi):", output)
else:
    print("Required language model not found.")
