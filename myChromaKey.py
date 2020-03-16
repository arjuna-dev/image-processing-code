from skimage import data, exposure, transform, io
from skimage.color import rgb2hsv, hsv2rgb
import matplotlib.pyplot as plt
import numpy as np

# img = data.astronaut()
img_file = "./darth.jpg"
img = io.imread(img_file)

img_file2 = "./amuse.jpg"
img2 = io.imread(img_file2)
# img2 = plt.imread(img_file2)


# Aprox hue is 0.32217573 - 0.3213628


def get_greens (image1, image2):
    img1          = image1.copy()
    img2          = image2.copy()
    resized_img2  = (transform.resize(img2, img1.shape)*255).astype(np.uint8)
    hsv_img       = rgb2hsv(img1)

    for x in range(image1.shape[0]):
        for y in range(image1.shape[1]):
            if hsv_img[x,y][0] <=0.33 and hsv_img[x,y][0]>=0.31:
                img1[x,y]=resized_img2[x,y]
    return img1

# def get_greens (img, img2):
#     img2 = transform.resize(img2, img.shape)
#     hsv_img = rgb2hsv(img)
#     greens_mask =  np.logical_and(hsv_img[:,:,0]<=0.34, hsv_img[:,:,0]>=0.31)
#     hsv_img[greens_mask] = img2[greens_mask]
#     greens = hsv2rgb(hsv_img)
#     return greens


new_img = get_greens(img, img2)

fig, (ax0, ax1, ax2) = plt.subplots(ncols=3, figsize=(12, 5))


ax0.imshow(img)
ax1.imshow(img2)
ax2.imshow(new_img)

fig.tight_layout()
plt.show()
