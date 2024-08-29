from django.views.generic import ListView, DetailView
from gallery.models import Image

class GalleryHomeView(ListView):
    model = Image
    context_object_name = "images"
    template_name = "gallery/home.html"


class ImageDetailView(DetailView):
    model = Image
    context_object_name = "images"
    template_name = "gallery/image_detail.html"