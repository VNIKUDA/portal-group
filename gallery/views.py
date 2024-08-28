from django.shortcuts import render, get_object_or_404
from gallery.models import Image

def gallery_home(request):
    images = Image.objects.all()
    return render(request, 'gallery/gallery_home.html', {'images': images})

def image_detail(request, id):
    image = get_object_or_404(Image, id=id)
    return render(request, 'gallery/image_detail.html', {'image': image})
