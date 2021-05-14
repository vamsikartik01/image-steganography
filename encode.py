from PIL import Image
import numpy as np

def Img2Arr(img):
    imgArr = np.array(img.getdata())
    #print(imgArr.shape)
    imgArr = imgArr.reshape(int(imgArr.shape[0]/3),9)
    #print(imgArr.shape)
    return imgArr, imgArr.shape[0]


def char2bin(char):
    charVal = ord(char)
    charBin = format(charVal, "08b")
    return charBin
    
def convert(byte,pixbyte,flag):
    pixbyten = pixbyte
    if flag:
        byte += '1'
    else:
        byte += '0'

    for pnt,bit in enumerate(byte):
        pixval = pixbyte[pnt]
        if pixval%2 == 0:
            if bit=='0':
                pass
            elif bit=='1':
                pixval -= 1
        else:
            if bit=='0':
                pixval -= 1
            elif bit=='1':
                pass
        pixbyten[pnt] = pixval

    return pixbyten
        

def encode(img, mssg):
    #img = Image.open("inputImage/blackhole.jpg")
    imgW, imgH = img.size
    arr,length = Img2Arr(img)
    #print(arr[11])
    #mssg = "Hello World!"
    lenm = len(mssg)
    if lenm > length:
        print("messege length is more than the image.")
        return None

    for lenUsed,char in enumerate(mssg):
        pixbyte = arr[lenUsed]
        byte = char2bin(char)
        if lenUsed < lenm-1:
            flag = True
        else:
            flag = False
        
        pixbyten = convert(byte, pixbyte, flag)
        arr[lenUsed] = pixbyten
   
    #print(arr[11])
    arr = arr.reshape(imgW, imgH, 3)
    img_en = Image.fromarray(np.uint8(arr))

    return img_en
    
        
            
        
    
