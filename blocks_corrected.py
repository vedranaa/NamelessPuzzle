import numpy as np
import matplotlib.pyplot as plt
import PIL.Image
filename = 'DTU_700x350.jpg'
DTU_image = np.array(PIL.Image.open(filename))

def divide_image(image, blocks_shape):
    H, W = blocks_shape
    h, w, l = image.shape
    bH = h // H
    bW = w // W
    
    blocks = np.empty(blocks_shape + (bH, bW, l), dtype=image.dtype)
    
    for i in range(H):
        for j in range(W):
            blocks[i][j] = image[i * bH : (i + 1) * bH, j * bW : (j + 1) * bW]
    return blocks


H, W = blocks_shape = (5, 6)
blocks = divide_image(DTU_image, blocks_shape)

fig, ax = plt.subplots(H, W)

for i in range(H):
    for j in range(W):
        ax[i][j].imshow(blocks[i][j])