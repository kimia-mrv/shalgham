from django.shortcuts import render, redirect
from PIL import Image
from fileuploader.models import photo
from io import BytesIO
from django.core.files.base import ContentFile


def index(request):
    try:
        if request.POST['share']!='n':
            a=photo.objects.filter(id=int(request.POST['share']))
            b=a[0]
            b.share()
            b.save()
    except (KeyError): a=5
    return render(request, 'fileuploader/index.html')


def details(request):
    wtd=request.POST["whatToDo"]
    if wtd=='b_w': return render(request, 'fileuploader/BWUp.html')
    if wtd=='crop':return render(request, 'fileuploader/CropUp.html')
    if wtd=='resize':return render(request, 'fileuploader/ResizeUp.html')
    if wtd=='rotate':return render(request, 'fileuploader/RotateUp.html')

def result(request):
    img=Image.open(request.FILES['fileToUpload'])
    try:
        t=tuple(map(int,[request.POST['left'],request.POST['upper'],
                         request.POST['right'],request.POST['lower']]))
        res=img.crop(t)
    except(KeyError):
        try:
            t=tuple(map(int,
                        [request.POST['width'],request.POST['height']]))
            res=img.resize(t)
        except(KeyError):
            try:
                res=img.rotate(int(request.POST['degrees']))
            except(KeyError):
                res=img.convert("L")
    thumb_io = BytesIO()
    res.save(thumb_io, format='JPEG')
    p = ContentFile(thumb_io.getvalue())
    i=photo()
    i.img.save('img.jpg',p)
    i.save()
    return render(request, 'fileuploader/result.html', {'object':i})

def shared (request):
    objects=photo.objects.filter(sharing=1)
    return render(request, 'fileuploader/shared files.html',
                  {'objects':objects})