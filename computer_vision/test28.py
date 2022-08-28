"""
pip install --upgrade Pillow
https://pillow.readthedocs.io/en/latest/handbook/tutorial.html
"""

from PIL import Image
# open image
im = Image.open("assets/test_image.jpg")
# convert image to greyScale
#im.convert('L')
# print format , size of image
print(im.format, im.size, im.mode)
# display image
im.show()

