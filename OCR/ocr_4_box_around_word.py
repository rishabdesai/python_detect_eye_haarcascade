import cv2
import pytesseract
from pytesseract import Output

img = cv2.imread('invoice2.png')

"""
Below code should give you the following output -
dict_keys(['level', 'page_num', 'block_num', 'par_num', 'line_num', 'word_num', 'left', 'top', 'width', 'height', 'conf', 'text'])
"""
d = pytesseract.image_to_data(img, output_type=Output.DICT)
print(d.keys())


"""
You can plot the boxes by using the code below -
"""
n_boxes = len(d['text'])
for i in range(n_boxes):
    if int(d['conf'][i]) > 60:
        (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow('img', img)
cv2.waitKey(0)

