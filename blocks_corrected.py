#%%
import numpy as np
import matplotlib.pyplot as plt
import PIL.Image

def divide_image(image, blocks_shape):
    '''Divides image into blocks of shape blocks_shape = (H, W)'''
    H, W = blocks_shape
    h, w, l = image.shape
    bH = h // H
    bW = w // W
    blocks = np.empty(blocks_shape + (bH, bW, l), dtype=image.dtype)
    for i in range(H):
        for j in range(W):
            blocks[i, j] = image[i * bH : (i + 1) * bH, j * bW : (j + 1) * bW]
    return blocks

def join_image(blocks, status):
    '''Joins image block according to the status matrix.'''
    H, W, bH, bW, l = blocks.shape
    h = bH * H
    w = bW * W

    image = np.zeros((h, w, l), dtype=blocks.dtype)
    for i in range(H):
        for j in range(W):
            b = status[i, j]
            bi = b//W
            bj = b%W
            image[i * bH : (i + 1) * bH, j * bW : (j + 1) * bW] = blocks[bi, bj]
    return image

def shuffle_status(status):
    '''Shuffles elements of the status matrix.'''
    status = np.random.permutation(status.ravel()).reshape(status.shape)
    return status

def initiate_status(blocks_shape):
    '''Initiates status matrix acoording to the blocks shape = (H, M).'''
    H, W = blocks_shape
    status = np.arange(H*W).reshape((H, W))
    return status


#%% Testing the functions

filename = 'DTU_700x350.jpg'
DTU_image = np.array(PIL.Image.open(filename))
H, W  = (5, 6)  # blocks shape
blocks = divide_image(DTU_image, (H, W))

#  Showing blocks
fig, ax = plt.subplots(H, W)
for i in range(H):
    for j in range(W):
        ax[i][j].imshow(blocks[i][j])
plt.show()

status0 = initiate_status((H, W))
image0 = join_image(blocks, status0)

fig, ax = plt.subplots()
ax.imshow(image0)
plt.show()

status = shuffle_status(status0)
image = join_image(blocks, status)

#%%

def display_status(ax, status, blocks_shape):
    H, W, bH, bW, l = blocks_shape
    for i in range(H):
        for j in range(W):
            x = j * bW + bW / 2
            y = i * bH + bH / 2
            nr = str(status[i, j])
            ax.text(x, y, nr, 
                    horizontalalignment='center', verticalalignment='center', 
                    fontsize=20, color='r')  #  backgroundcolor='w')


fig, ax = plt.subplots()
ax.imshow(image)
display_status(ax, status, blocks.shape)
print(ax.texts)

plt.show()


# %%
