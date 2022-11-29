#%%
import matplotlib.pyplot as plt
import PIL.Image
import numpy as np


def switch_images(images):

    def arrow_navigation(event, i, I):
        if event.key == "up":
            i = (i+1) % I
        elif event.key == 'down':
            i = (i-1) % I 
        elif event.key == 'right':
            i = (i+1) % I
        elif event.key == 'left':
            i = (i-1) % I
        return i

    def update_image():
        ax.imshow(images[i])
        ax.set_title(f'image {i}')
        fig.canvas.draw()

    def key_press(event):
        nonlocal i
        i = arrow_navigation(event, i, I)
        update_image()

    fig, ax = plt.subplots()
    i = 0
    I = len(images)
    update_image()
    fig.canvas.mpl_connect('key_press_event', key_press)
    plt.axis('off')
    plt.show()



image1 = np.array(PIL.Image.open('DTU_700x350.jpg'))
cz = np.array(PIL.Image.open('captn_zenitsu.jpg'))

image2 = cz[:350, :700]
image3 = cz[350:700, 600:1300]
image4 = cz[:350, 600:1300]
image5 = cz[350:700, :700]

images = [image1, image2, image3, image4, image5]

switch_images(images)



   

# %%
