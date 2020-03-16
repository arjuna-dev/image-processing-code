#https://scikit-image.org/docs/dev/auto_examples/color_exposure/plot_rgb_to_hsv.html#sphx-glr-auto-examples-color-exposure-plot-rgb-to-hsv-py

import matplotlib.pyplot as plt

from skimage import data
from skimage.color import rgb2hsv

rgb_img = data.coffee()
hsv_img = rgb2hsv(rgb_img)
#Numpy sthing: hsv_img[rows, columns, pixels]. hsv_img[:, :, 0] <- the 0 accesses the h value levaing out s and v
hue_img = hsv_img[:, :, 0]
sat_img = hsv_img[:, :, 1]
value_img = hsv_img[:, :, 2]


fig, (ax0, ax1, ax2) = plt.subplots(ncols=3, figsize=(8, 2))


ax0.imshow(hue_img)
ax1.imshow(sat_img)
ax2.imshow(value_img)


# ax0.imshow(rgb_img)
# # ax0.set_title("RGB image")
# ax0.axis('off')
# ax1.imshow(hue_img, cmap='hsv')
# # ax1.set_title("Hue channel")
# ax1.axis('off')
# ax2.imshow(value_img)
# # ax2.set_title("Value channel")
# ax2.axis('off')

# fig.tight_layout()

# hue_threshold = 0.04
# binary_img = hue_img > hue_threshold

# fig, (ax0, ax1) = plt.subplots(ncols=2, figsize=(8, 3))

# ax0.hist(hue_img.ravel(), 512)
# ax0.set_title("Histogram of the Hue channel with threshold")
# ax0.axvline(x=hue_threshold, color='r', linestyle='dashed', linewidth=2)
# ax0.set_xbound(0, 0.12)
# ax1.imshow(binary_img)
# ax1.set_title("Hue-thresholded image")
# ax1.axis('off')

# fig.tight_layout()



# fig, ax0 = plt.subplots(figsize=(4, 3))

# value_threshold = 0.10
# binary_img = (hue_img > hue_threshold) | (value_img < value_threshold)

# ax0.imshow(binary_img)
# ax0.set_title("Hue and value thresholded image")
# ax0.axis('off')

# fig.tight_layout()


plt.show()
