## This file has the basics of PIL and numpy required for this project

# importing the libraries
from PIL import Image
import numpy as np

## Reading the image file
im = Image.open(r"inputImage/blackhole.jpg")
#im.show()  #uncomment this to view the image

# reading the pixels of the image as an array.
# by default the size of the array is (n, 3).
# n = m*m, for an image of sizde mxm.
im_arr = np.array(im.getdata())
print(im_arr)
# The original size of the image
print(im.size)
im_w, im_h = im.size

# reshaping the numpy array.
print(im_arr.shape)
# im_array is 1440000,3 lets resize it into 1440000*3,1
array_new = im_arr.reshape(1440000*3,1)
print(array_new.shape)
print(array_new)

# Now we need 3 pixels to encrypt a character. so lets reshape it.
array_new = im_arr.reshape(int(1440000/3),9)
print(array_new.shape)
print(array_new)

# after encoding we will reshape to the original size
im_org = array_new.reshape(im_w,im_h,3)
print(im_org.shape)

# convert the array back into image
img_op = Image.fromarray(np.uint8(im_org))

# now the save the new image
img_op.save("outputImage/op1.jpg")


