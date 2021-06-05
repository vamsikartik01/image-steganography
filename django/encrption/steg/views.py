from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.core.files.storage import FileSystemStorage
from websteg import encrypt, decrypt
# Create your views here.

def index(request):
    return render(request, 'steg/index.html')

def encode(request):
    if request.method == "POST" and request.FILES['myimage']:
        myimage = request.FILES['myimage']
        fs = FileSystemStorage()
        filename = fs.save("enc/input/"+myimage.name, myimage)
        messg = request.POST['messg']
        event = Event(imageName=myimage.name, messege=messg, status="Unsecure")
        event.save()
        stat, name = encrypt(myimage.name, messg)
        print("status: ", stat)
        if stat:
            event.status = 'Secure'
            event.save()
            fs.delete("enc/input/"+myimage.name)
            fs.delete("enc/comp/"+myimage.name)
            uploaded_file_url = '/media/enc/output/'+name
            return render(request, 'steg/encode.html', {
                'uploaded_file_url': uploaded_file_url
            })
        else:
            return render(request, 'steg/encode.html', {'erm':"error encoding"})
    elif request.method == "POST" and not request.FILES['myimage']:
        return render(request, 'steg/encode.html', {'erm':"error encoding"})
    return render(request, 'steg/encode.html')

def decode(request):
    if request.method == "POST" and request.FILES['myimage']:
        fs = FileSystemStorage()
        myimage = request.FILES['myimage']
        fs.save("dec/"+myimage.name, myimage)
        event = Event(imageName=myimage.name, messege="DECODING", status="Secure")
        event.save()
        stat, messg = decrypt(myimage.name)
        if stat:
            event.status = 'Unsecure'
            event.save()
            fs.delete("dec/"+myimage.name)
            return render(request, "steg/decode.html", {'messege':messg})
        else:
            return render(request, "steg/decode.html", {'messege':"Decoding failed!"})

    return render(request, 'steg/decode.html')
