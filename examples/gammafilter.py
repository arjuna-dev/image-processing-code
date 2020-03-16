
from skimage import data, img_as_float, io
from skimage import exposure
import matplotlib.pyplot as plt


img = data.moon()
gamma_corrected = exposure.adjust_gamma(img, 2)
io.imshow(img)
io.imshow(gamma_corrected)
plt.show()