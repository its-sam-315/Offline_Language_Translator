import argostranslate.package
import argostranslate.translate

# Path to downloaded model file
package_path = "C:/Users/coolb/Downloads/en_hi.argosmodel"  # Change if needed

# Install the model
argostranslate.package.install_from_path(package_path)

print("Model installed successfully!")
