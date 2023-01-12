# Imports for visualization
import PIL.Image
from io import StringIO 
from IPython.display import clear_output, Image, display
import scipy.ndimage as nd
import scipy.signal
import tensorflow as tf
import numpy as np
np.set_printoptions(suppress=True)

sess = tf.compat.v1.InteractiveSession()



def display_array(a, fmt='jpeg', rng=[0,1]):
  """Display an array as a picture."""
  a = (a - rng[0])/float(rng[1] - rng[0])*255
  a = np.uint8(np.clip(a, 0, 255))
  f = StringIO()
  PIL.Image.fromarray(a).save(f, fmt)
  display(Image(data=f.getvalue()))

