#%%
import numpy as np
import matplotlib.pyplot as plt
import PIL.Image
import matplotlib
import random


possible_dir = []
matplotlib.use('Qt5Agg')  # choose a suitable backend
direction_to_movement = {
    
    }

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
            status = shuffle_n2(status)
        if event.key in ['up', 'down', 'right', 'left']:
            status = move_status(status, event.key)

        ax.images[0].set_array(join_image(blocks, status))
        fig.canvas.draw()
        print(status)

    if W is None:
        W = H

    fig, ax = plt.subplots()
    ax.imshow(image)
    blocks = divide_image(image, (H, W))
    status = initiate_status((H, W))
    
    fig.canvas.mpl_connect('key_press_event', key_press)
    plt.axis('off')
    plt.show()

    def shuffle_n2(status):
        global possible_dir
        possible_dir.clear()
        y = (np.where(status==0)[0])
        x = (np.where(status==0)[1])
        if y < 4:
            possible_dir.append("down")
        if y > 0:
            possible_dir.append("up")
        if x < 4:
            possible_dir.append("right")
        if x > 0:
            possible_dir.append("left")
        for k in range(50):
            choice = random.choice(possible_dir)
            move_status(status, choice)
            
            
DTU_image = np.array(PIL.Image.open('DTU_700x350.jpg'))
noname_puzzle(DTU_image, 3)
