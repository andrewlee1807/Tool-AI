from skimage import io
import numpy as np
import matplotlib.pyplot as plt

path_image = "Dataset/IM-0001-000130.jpg"
img = io.imread(path_image, as_gray=True)  # Read the Image like Gray Scale
image = np.array(img, copy=True) * 255.0

bps = [(np.uint8(image) >> i) % 2 for i in range(8)]


def generate_image(outImg):
    for i, p in enumerate(bps):
        outImg += (p * np.power(2, i))
    outImg /= np.max(outImg)
    return outImg


lsImg = [img]
for i in range(7, 0, -1):
    outImg = 0 * image
    bps[i] *= 0
    lsImg.append(generate_image(outImg))

# Size of an Image in the Grid
w = 10
h = 10

# Size of GridImage
fig = plt.figure(figsize=(10, 5))

# Column and row
columns = 4
rows = 2

axes = []
titles = [2 ** i for i in range(1, 8)]
titles.append(256)
titles = titles[::-1]

for i, img, title in zip(range(1, columns * rows + 1), lsImg, titles):
    axes.append(fig.add_subplot(rows, columns, i))
    subplot_title = (str(title) + " intensity levels")
    axes[-1].set_title(subplot_title)
    plt.imshow(img, cmap='gray')
plt.show()

