from matplotlib import pyplot as plt
import matplotlib.image as mimg
image = mimg.imread('logo.png')
plt.imshow(image)
plt.show()
print(type(image))
print(image.shape)