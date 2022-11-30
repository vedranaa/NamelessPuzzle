#%%
import numpy as np
import matplotlib.pyplot as plt
import PIL.Image
import matplotlib
matplotlib.use('Qt5Agg')  # choose a suitable backend 


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
            if b > 0:
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

def move_status(status, key):
    '''Key can be 'up', 'down', 'right' or 'left' '''
    
    H, W = status.shape
    y = np.where(status==0)[0][0] 
    x = np.where(status==0)[1][0]

    if key=='down' and y+1<H:
        new_x = x
        new_y = y + 1         
    elif key=='up' and y>0:
        new_x = x
        new_y = y - 1
    elif key=='right' and x+1<W:
        new_x = x + 1
        new_y = y 
    elif key=='left' and x>0:
         new_x = x - 1
         new_y = y 
 
    status[y,x] = status[new_y, new_x]
    status[new_y, new_x] = 0

    return status




def noname_puzzle(image, H, W=None):
    '''Main function for noname puzzle.'''

    def key_press(event):
        nonlocal status
        if event.key == 'm':
            status = shuffle_status(status)
        if event.key in ['up', 'down', 'right', 'left']:
            status = move_status(status, event.key)

        ax.imshow(join_image(blocks, status))
        fig.canvas.draw()

    if W is None:
        W = H

    fig, ax = plt.subplots()
    ax.imshow(image)
    blocks = divide_image(image, (H, W))
    status = initiate_status((H, W))
    
    fig.canvas.mpl_connect('key_press_event', key_press)
    plt.axis('off')
    plt.show()


DTU_image = np.array(PIL.Image.open('DTU_700x350.jpg'))
noname_puzzle(DTU_image, 4)
