from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.core.files.storage import FileSystemStorage
from websteg import encrypt, decrypt
# Create your views here.

def index(request):
    if request.method == "POST" and request.FILES['myimage']:
        myimage = request.FILES['myimage']
        fs = FileSystemStorage()
        filename = fs.save("input/"+myimage.name, myimage)
        messg = request.POST['messg']
        event = Event(imageName=myimage.name, messege=messg, status="Unsecure")
        event.save()
        stat, name = encrypt(myimage.name, messg)
        if stat:
            event.status = 'Secure'
            event.save()
            uploaded_file_url = '/media/output/'+name
            return render(request, 'steg/index.html', {
                'uploaded_file_url': uploaded_file_url
            })
    return render(request, 'steg/index.html', {'erm':"error encoding"})
