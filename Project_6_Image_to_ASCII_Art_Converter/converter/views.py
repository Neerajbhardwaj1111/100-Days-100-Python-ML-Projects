from django.shortcuts import render

# Create your views here.
from django.core.files.storage import FileSystemStorage
from .utils import image_to_ascii

def index(request):
    return render(request, 'converter/index.html')

def convert_image(request):
    if request.method == 'POST' and request.FILES['image']:
        img = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(img.name, img)
        img_path = fs.path(filename)
        
        ascii_art = image_to_ascii(img_path)
        
        return render(request, 'converter/result.html', {
            'ascii_art': ascii_art,
            'file_path': filename
        })
    return render(request, 'converter/index.html')