import scipy.misc as scm
from scipy.misc.pilutil import Image
orig_image = Image.open('./test.jpg')

image1 = scm.fromimage(orig_image)
inv_image = 255 - image1
inverted_image = scm.toimage(inv_image)
inverted_image.save('./test01.jpg')