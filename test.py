import numpy as np
from PIL import Image

file_path = "inputImage/car.jpg"

img = Image.open(file_path)

img.save("inputImage/comp.jpg", optimize = True, quality=10)
