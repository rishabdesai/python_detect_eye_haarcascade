"""
Ref sites: 
Installation: https://github.com/UB-Mannheim/tesseract/wiki

project: 
https://nanonets-com.cdn.ampproject.org/v/s/nanonets.com/blog/ocr-with-tesseract/amp/?amp_js_v=a6
https://github.com/madmaze/pytesseract


"""

from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

im = Image.open("test.jpg")

text = pytesseract.image_to_string(im, lang = 'eng')

print(text)