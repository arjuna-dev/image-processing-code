
from skimage import data, img_as_float, io, exposure
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from math import log2, log, log10

moon = data.moon()

def gamma_correct(image):
    img = image.copy()
    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            lum = img[x, y] 
            if lum == 0:
                continue
            newlum = 255 * (lum/255)**(1/2.2)
            img[x, y] = newlum
    return img

def degammify(image):
    img = image.copy()
    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            lum = img[x, y] 
            if lum == 0:
                continue
            newlum = 255 * (lum/255)**(2.2)
            img[x, y] = newlum
    return img

def log_correct(image):
    img = image.copy()
    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            lum = img[x, y]
            if lum == 0:
                continue
            newlum = 255/log2(lum)
            # print(lum, ":")
            # print(newlum)
            img[x, y] = newlum
    return img

# gamma_corrected = exposure.adjust_gamma(moon, 2)
# io.imshow(gamma_corrected)

img = gamma_correct(moon)
img2 = log_correct(moon)
img_de = degammify(img)

fig, (ax0, ax1, ax2) = plt.subplots(ncols=3, figsize=(12, 5))


ax0.imshow(moon, cmap=cm.gray, vmin=0, vmax=255)
ax1.imshow(img, cmap=cm.gray, vmin=0, vmax=255)
ax2.imshow(img_de, cmap=cm.gray, vmin=0, vmax=255)

fig.tight_layout()
plt.show()

# io.imshow(img, cmap=cm.gray, vmin=0, vmax=255)
# plt.show()