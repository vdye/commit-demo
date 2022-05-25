import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread('images/test-landscape.jpg')

imgplot = plt.imshow(img)
plt.show()