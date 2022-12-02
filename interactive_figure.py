import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from matplotlib.widgets import Button
from itertools import count

x_values = []
y_values = []

fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)

index = count()

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


def stop_animation(event):
    global anim
    anim.event_source.stop()


startax = plt.axes([0.3, 0.1, 0.1, 0.05])
startbutton = Button(startax, label='Start', hovercolor='0.5')

stopax = plt.axes([0.5, 0.1, 0.1, 0.05])
stopbutton = Button(stopax, label='Stop', hovercolor='0.5')

startbutton.on_clicked(start_animation)
stopbutton.on_clicked(stop_animation)
plt.show()  
