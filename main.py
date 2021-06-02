from encode import encode
from decode import decode
from PIL import Image
import os
    
def encrypt(name, mssg):
    file_path = "inputImage/"+name
    try:
        img = Image.open(file_path)
        img.save("inputImage/comp.jpg", optimize = True, quality=10)
        img = Image.open('inputImage/comp.jpg')
 
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
        img = Image.open(file_path)
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
        #
        print("To enter text press 1 or to add text file press 2")
        respe = int(input().strip())
        if respe==2:
            print("enter file name:")
            fname = str(input().strip())
            print("Please Wait")
            f_read = open("inputImage/"+fname,'r')
            f_read.seek(0)
            mssg = f_read.read()
            f_read.close()
            status,name = encrypt(name, mssg)

        elif respe==1:
            print("Enter the Messege to encrypt:")
            mssg = str(input().strip())
            print("Please Wait")
            status,name = encrypt(name, mssg)

        else:
            print("Error occured select properly!")
    
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
            print("Do you want to save the messege in a file(y/n):")
            respd = str(input().strip())
            if respd=='y':
                print("enter name of the file:")
                fname = str(input().strip())
                f_write = open("outputImage/"+fname+".txt",'w')
                f_write.write(mssg)
                f_write.close()
                
        else:
            print("Image decing failed! please try again")

    else:
        print("Response unidentified. please try again")
