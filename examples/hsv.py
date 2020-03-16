#Original example:
#https://stackoverflow.com/questions/55767292/skimage-how-to-get-correct-color-when-converting-rgb-to-hsv-understanding-hue

from skimage import data, exposure
from skimage.color import rgb2hsv
import matplotlib.pyplot as plt

img = "./graph.png"

img_data = plt.imread(img)

hsv_img=rgb2hsv(img_data)

# hsv_test_img_arr=rgb2hsv(img)

hue_img = hsv_img[:, :, 0]
sat_img = hsv_img[:, :, 1]
value_img = hsv_img[:, :, 2]

fig, ((ax0, ax1), (ax2, ax3)) = plt.subplots(ncols=2, nrows=2, figsize=(8, 6))


im0 = ax0.imshow(hsv_img)
ax0.set_title('original')
ax0.axis('off')

im1 = ax1.imshow(hue_img, cmap='hsv', vmin=0, vmax=1)
ax1.set_title('hue channel')
ax1.axis('off')
fig.colorbar(im1, ax=ax1)

im2 = ax2.imshow(value_img, cmap="gray", vmin=0, vmax=1)
ax2.set_title('value channel')
ax2.axis('off')
fig.colorbar(im2, ax=ax2)

im3 = ax3.imshow(sat_img, cmap="gray", vmin=0, vmax=1)
ax3.set_title('sat channel')
ax3.axis('off')
fig.colorbar(im3, ax=ax3)

plt.show()