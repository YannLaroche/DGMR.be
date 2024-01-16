import matplotlib
from matplotlib import animation
import matplotlib.pyplot as plt

def plot_animation(field, figsize=None,
                   vmin=0, vmax=10, cmap="jet", **imshow_args):
  fig = plt.figure(figsize=figsize)
  ax = plt.axes()
  ax.set_axis_off()
  plt.close() # Prevents extra axes being plotted below animation
  img = ax.imshow(field[0, 0, 0], vmin=vmin, vmax=vmax, cmap=cmap, **imshow_args)

  def animate(frame):
    img.set_data(field[0, frame, 0])
    return (img,)

  return animation.FuncAnimation(
      fig, animate, frames=field.shape[1], interval=4, blit=False)