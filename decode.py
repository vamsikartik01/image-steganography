from encode import Img2Arr
from PIL import Image
import numpy as np

def pix2bin(Arr):
    bval = ""
    for p in Arr:
        if p%2 == 0:
            bval += '0'
        else:
            bval += '1'
    flag = bval[-1]
    bval = bval[:-1]
    return bval,flag
    

#if __name__=="__main__":
def decode(img):
    #img = Image.open("outputImage/blackhole-en.png",'r')
    imgArr, imgLen = Img2Arr(img)
    #print(imgArr)
    mssg = ""
    for Arr in imgArr:
        bval, flag = pix2bin(Arr)
        ascval = int(bval,2)
        mssg += chr(ascval)

        if flag=='0':
            break
        
    return mssg
        
