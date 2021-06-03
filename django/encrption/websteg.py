from PIL import Image
import numpy as np
#################################3
##################################

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


##################################3
#################################

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
    i=1
    while True:
        pxbytes = np.concatenate((imgArr[3*(i)-3],imgArr[3*(i)-2],imgArr[3*(i)-1]))
        i = i+1
        bval, flag = pix2bin(pxbytes)
        ascval = int(bval,2)
        mssg += chr(ascval)

        if flag=='0':
            break
        
    return mssg

        

####################################
##################################

def encrypt(name, mssg):
    file_path = "media/enc/input/"+name
    try:
        img = Image.open(file_path)
        img.save("media/enc/comp/"+name, optimize = True, quality=10)
        img = Image.open('media/enc/comp/'+name)
 
        img_en = encode(img, mssg)
        name = name.split('.')[0]+"-en.png"
        file_out = "media/enc/output/"+name
        img_en.save(file_out)
        return True,name
    except:
        return False,name

def decrypt(name):
    file_path = "media/dec/"+name
    try:
        img = Image.open(file_path, 'r')
        mssg = decode(img)
        return True,mssg
    except:
        return False,None
