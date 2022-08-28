
import io
import pandas as pd
from skimage import io
img = io.imread('assets/test_image.jpg')
print(img.shape)
df = pd.DataFrame(img.flatten())
filepath = 'assets/pixel_values1.xlsx'
df.to_excel(filepath,index=False)

