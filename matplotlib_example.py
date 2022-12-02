#%%
import matplotlib.pyplot as plt
import PIL.Image
import numpy as np

# reading and displaying the image
filename = 'DTU_700x350.jpg'
DTU_image = np.array(PIL.Image.open(filename))
fig, ax = plt.subplots()
ax.imshow(DTU_image)

#%% extracting columns from the image
print(DTU_image.shape)
h, w, l = DTU_image.shape
print(w//3)


column0 = DTU_image[:, 0:233, :]
column1 = DTU_image[:, 233:466, :]
column2 = DTU_image[:, 466:, :]

mosaic = np.column_stack((column2, column1, column0))

fig, ax = plt.subplots()
ax.imshow(mosaic)


#%% making a red background and pasting a part of the image
red_image = np.zeros((350, 350, 3), dtype=np.uint8)
red_image[:,:,0] = 255

red_image[50:300, 50:300, :] = DTU_image[100:350, 100:350, :]

fig, ax = plt.subplots()
ax.imshow(red_image)

# %%

def extract_image_blocks(image, blocks_shape):
    h, w, l = image.shape
