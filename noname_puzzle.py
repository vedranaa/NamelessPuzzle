#%%
import numpy as np
import matplotlib.pyplot as plt
import PIL.Image
import matplotlib

# just checking whether git is working


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

    move = True
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
    else:
        move = False

    if move:
        status[y,x] = status[new_y, new_x]
        status[new_y, new_x] = 0

    return status



def noname_puzzle(image, H, W=None):
    '''Main function for noname puzzle.'''

    def simulate_swapping_status():
        '''Simulates randomly hitting arrow key neighbourg N times.'''
        nonlocal status
        nonlocal swapping
        swapping = True
        N = 20  # number of steps taken
        pause = 0.1  # length of pause
        keys = ['up', 'down', 'left', 'right']
        rand = (np.random.randint(2, size=(N//2, 2)) + [0, 2]).ravel()
        for r in rand:
            status = move_status(status, keys[r])
            update_display()
            plt.pause(pause)
        swapping = False

    def update_display():

        ax.images[0].set_array(join_image(blocks, status))
        if ds:
            # remove any previously shown texts
            while (ax.texts):
                ax.texts[-1].remove()

            # show status on top of the image
            for i in range(H):
                for j in range(W):
                    x = j * bW + bW / 2
                    y = i * bH + bH / 2
                    nr = str(status[i, j])
                    ax.text(x, y, nr,
                            horizontalalignment='center', verticalalignment='center',
                            fontsize=20, color='r')  #  backgroundcolor='w'
        fig.canvas.draw()

    def key_press(event):
        nonlocal status
        nonlocal ds

        # if event.key == 'm':
        #     status = shuffle_status(status)
        if event.key == 'r' and not swapping:
            simulate_swapping_status()
        if event.key in ['up', 'down', 'right', 'left']:
            status = move_status(status, event.key)
        if event.key =='h':
            ds = not(ds)
            if not ds:
                while (ax.texts):
                    ax.texts[-1].remove()

        update_display()

    if W is None:
        W = H

    image = np.array(image)  # such that image also can be PIL image

    blocks = divide_image(image, (H, W))
    H, W, bH, bW, l = blocks.shape

    status = initiate_status((H, W))
    ds = False  # no status show to begin with
    swapping = False  # to keep track of swapping

    fig, ax = plt.subplots()
    ax.imshow(join_image(blocks, status))
    fig.canvas.mpl_connect('key_press_event', key_press)
    plt.axis('off')
    plt.show()

if __name__  ==  '__main__':

    matplotlib.use('Qt5Agg')  # choose a suitable backend
    DTU_image = np.array(PIL.Image.open('DTU_700x350.jpg'))
    noname_puzzle(DTU_image, 3, 4)

# %%
