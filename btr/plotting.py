import matplotlib
from matplotlib import animation
import matplotlib.pyplot as plt
import numpy as np

def plot_animation(field, figsize=None,
                   cmap="jet", **imshow_args):
  
  matplotlib.rc('animation', html='jshtml')
  
  fig = plt.figure(figsize=figsize)
  ax = plt.axes()
  ax.set_axis_off()
  plt.close() # Prevents extra axes being plotted below animation
  vmax = np.max(field[0, 0, 0])
  vmin = np.min(field[0, 0, 0])
  img = ax.imshow(field[0, 0, 0], vmin=vmin, vmax=vmax, cmap=cmap, **imshow_args)
  cb = fig.colorbar(img, ax=ax)
  tx = ax.set_title('Frame 0')

  def animate(frame):
    img.set_data(field[0, frame, 0])
    vmax     = np.max(field[0, frame, 0])
    vmin     = np.min(field[0, frame, 0])
    img.set_clim(vmin, vmax)
    tx.set_text(f'Frame {frame}')
    return (img,)

  return animation.FuncAnimation(
      fig, animate, frames=field.shape[1], interval=4, blit=False)
  
def plot_subplot(input, output, figsize=None,
                  vmin=0, vmax=10, cmap="jet", **imshow_args):
  fig, axes = plt.subplots(2, 4, figsize=figsize)
  if str(type(output)) == "<class 'torch.Tensor'>":
    output = output.detach().numpy()
  for i in range(4):
    im1 = axes[0, i].imshow(input[0, i, 0], cmap=cmap, vmin=vmin, vmax= vmax, **imshow_args)
    plt.colorbar(im1, ax=axes[0, i])
    
    im2 = axes[1, i].imshow(output[0, i, 0], cmap=cmap, vmin=vmin, vmax= vmax, **imshow_args)
    plt.colorbar(im2, ax=axes[1, i])
  
  return None