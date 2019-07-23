from django.shortcuts import render, get_object_or_404
from .models import Blog
from KasiaIMateusz.utils import get_item_from_onedrive

# Create your views here.

def allblogs(request):
    photos = get_item_from_onedrive("/Inne")

    images = []
    for photo in photos.get_items(limit=10):
        if photo.is_photo or photo.is_image:
            print(dir(photo))
            print(dir(photo.share_with_link("embed")))
            print(photo.dimensions)     # This is dimensions of photo
            print(photo.web_url)        # This is a OneDrive url
            images.append("https://api.onedrive.com/v1.0/shares/" + photo.share_with_link("embed").share_id + "/root/content")
            # https://api.onedrive.com/v1.0/shares/{shareId}/root/content
            # https://api.onedrive.com/v1.0/shares/{shareId}/root/thumbnails/0/[small/medium/large]/content

    print(images)

    return render(request, "Blog/allblogs.html", {"images" : images})

def detail(request, blog_id):
    blog_object = get_object_or_404(Blog, pk=blog_id)
    return render(request, "Blog/detail.html", { "Blog" : blog_object })
