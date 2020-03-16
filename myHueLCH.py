from skimage import data
from skimage.color import rgb2lab, lab2lch, lch2lab, lab2rgb
import matplotlib.pyplot as plt
from math import pi

# img = data.coffee()
img_file = "./graph.png"
img = plt.imread(img_file)



def change_hue(img, hue):
    lab_img = rgb2lab(img)
    lch_img = lab2lch(lab_img)
    lch_img[:,:,2]=hue
    lab_img = lch2lab(lch_img)
    rgb_img = lab2rgb(lab_img)
    return rgb_img

img2 = change_hue(img, 0.5)

fig, (ax0, ax1) = plt.subplots(ncols=2, figsize=(12, 5))


ax0.imshow(img)
ax1.imshow(img2)

fig.tight_layout()
plt.show()
