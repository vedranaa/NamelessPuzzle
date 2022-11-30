<<<<<<< Updated upstream
#%%
import matplotlib
=======
>>>>>>> Stashed changes
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from matplotlib.widgets import Button
from itertools import count

<<<<<<< Updated upstream
matplotlib.use('Qt5Agg')  # choose a suitable backend 
=======
x_values = []
y_values = []
>>>>>>> Stashed changes

fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)

<<<<<<< Updated upstream
    def arrow_navigation(event, i, I):
        if event.key == 'up':
            i = (i+1) % I
        elif event.key == 'down':
            i = (i-1) % I 
        elif event.key == 'right':
            i = (i+1) % I
        elif event.key == 'left':
            i = (i-1) % I
        return i
=======
index = count()
>>>>>>> Stashed changes

def update_animation(i):
    ax.clear()
    t = next(index)
    x_values.append(t)
    y_values.append(np.sin(t))
    ax.plot(x_values, y_values)


def start_animation(event):
    global anim
    anim = animation.FuncAnimation(fig, update_animation, interval=0)
    anim.event_source.start()


<<<<<<< Updated upstream
image1 = np.array(PIL.Image.open('DTU_700x350.jpg'))
cz = np.array(PIL.Image.open('captn_zenitsu.jpg'))
=======
def stop_animation(event):
    global anim
    anim.event_source.stop()

>>>>>>> Stashed changes

startax = plt.axes([0.3, 0.1, 0.1, 0.05])
startbutton = Button(startax, label='Start', hovercolor='0.5')

stopax = plt.axes([0.5, 0.1, 0.1, 0.05])
stopbutton = Button(stopax, label='Stop', hovercolor='0.5')

<<<<<<< Updated upstream
switch_images(images)


   
# %%
=======
startbutton.on_clicked(start_animation)
stopbutton.on_clicked(stop_animation)
plt.show()  
>>>>>>> Stashed changes
