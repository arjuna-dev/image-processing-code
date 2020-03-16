from skimage import data, exposure
from skimage.color import rgb2hsv, hsv2rgb
import matplotlib.pyplot as plt

# img = data.astronaut()
img_file = "./graph.png"
img = plt.imread(img_file)

def change_hue(img, hue):
    hsv_img = rgb2hsv(img)
    hsv_img[:,:,0] = hue
    img = hsv2rgb(hsv_img)
    return img

img2 = change_hue(img, 0.5)

fig, (ax0, ax1) = plt.subplots(ncols=2, figsize=(12, 5))


ax0.imshow(img)
ax1.imshow(img2)

fig.tight_layout()
plt.show()
