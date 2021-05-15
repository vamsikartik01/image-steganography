from encode import encode
from decode import decode
from PIL import Image
    
def encrypt(name, mssg):
    file_path = "inputImage/"+name
    try:
        img = Image.open(file_path,'r')
        img_en = encode(img, mssg)
        name = name.split('.')[0]+"-en.png"
        file_out = "outputImage/"+name
        img_en.save(file_out)
        return True,name
    except:
        return False,name

def decrypt(name):
    file_path = "outputImage/"+name
    try:
        img = Image.open(file_path, 'r')
        mssg = decode(img)
        return True,mssg
    except:
        return False,None

if __name__=="__main__":
    print("Encode : 1")
    print("Decode : 2")
    resp = int(input().strip())
    if resp==1:
        print("Keep your image file in the folder named inputImage")
        print("Name of the image file with extension:")
        name = str(input().strip())
        print("Enter the Messege to encrypt:")
        mssg = str(input().strip())
        print("Please Wait")
        status,name = encrypt(name, mssg)
        if status:
            print("Messege encrypted succesfully")
            print("Your file is the image with name ",name,"in outputImage folder")
        else:
            print("Image encoding failed! Please try again.")

    elif resp==2:
        print("Keep your image file in folder named outputImage and also make sure the image is not compressed by any means")
        print("Name of your image file with extension:")
        name = str(input().strip())
        print("Please wait")
        status, mssg = decrypt(name)
        if status:
            print("Messege decryption is successful!")
            print("Your messege is: ")
            print(mssg)
        else:
            print("Image decing failed! please try again")

    else:
        print("Response unidentified. please try again")
        

















            
    
