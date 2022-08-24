from PIL import Image

import pytesseract

# If you don't have tesseract executable in your PATH, include the following:

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# Example tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

# Simple image to string
#print(pytesseract.image_to_string(Image.open('test.png')))

# List of available languages
print(pytesseract.get_languages(config=''))

# Hindi text image to string
print(pytesseract.image_to_string(Image.open('hindi.png'), lang='hin'))
