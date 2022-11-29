import numpy as np
import matplotlib.pyplot as plt
import PIL.Image
filename = 'DTU_700x350.jpg'
DTU_image = np.array(PIL.Image.open(filename))
blocks = [[], [], [], []]
def divide_image(image, blocks):
    image_shape = 4, 6
    h, w = image_shape
    bH = h // w
    bW = w // w
    for i in range(h):
        for j in range(w):
            blocks[i][j] = image[i * bH:(i + 1) * bH, j * bW:(j + 1) * bW]
    return blocks
