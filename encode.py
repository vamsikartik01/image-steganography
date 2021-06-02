from PIL import Image
import numpy as np

def Img2Arr(img):
    imgArr = np.array(img.getdata())
    return imgArr, int(imgArr.shape[0]/3)


def char2bin(char):
    charVal = ord(char)
    charBin = format(charVal, "08b")
    return charBin
    
def convert(byte, pxbytes, flag):
    if flag:
        byte += '1'
    else:
        byte += '0'

    bytes = [byte[:3], byte[3:6], byte[6:9]]

    for i in range(3):
        byte = bytes[i]
        pxbyte = pxbytes[i]
        for pnt, bit in enumerate(byte):
            pxv = pxbyte[pnt]
            if bit=='0':
                if pxv%2==0:
                    pass
                else:
                    pxv -= 1
            elif bit=='1':
                if pxv%2==0:
                    pxv -= 1
                else:
                    pass
            else:
                pass
            pxbyte[pnt] = pxv
        pxbytes[i] = pxbyte

    return pxbytes
        

#if __name__ == "__main__":
def encode(img, mssg):
    #img = Image.open("inputImage/blackhole.jpg",'r')
    #mssg = "Hello I am black hole! :)"
    imgW, imgH = img.size
    arr,length = Img2Arr(img)
    lenm = len(mssg)
    if lenm > length:
        print("messege length is more than the image size.")
        #return None
    for lenUsed,char in enumerate(mssg):
        #pixbyte = arr[lenUsed]
        pxbyte = arr[3*(lenUsed+1)-3: 3*(lenUsed+1)]
        byte = char2bin(char)

        if lenUsed < lenm-1:
            flag = True
        else:
            flag = False
        
        pxbytes = convert(byte, pxbyte, flag)
        arr[3*(lenUsed+1)-3: 3*(lenUsed+1)] = pxbytes
   
    #print(arr[11])
    arr = arr.reshape(imgH, imgW, 3)
    img_en = Image.fromarray(np.uint8(arr))

    return img_en
    
        
            
        
    
