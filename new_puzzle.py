#%%

import matplotlib
import matplotlib.pyplot as plt
import PIL
import noname_puzzle

matplotlib.use('Qt5Agg')  # choose a suitable backend 

image = PIL.Image.open('captn_zenitsu.jpg')

image = image.resize((int(0.5 * s) for s in image.size))
noname_puzzle.noname_puzzle(image, 4, 3)
# %%
