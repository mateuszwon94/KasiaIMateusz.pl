from django.shortcuts import render
from KasiaIMateusz.utils import get_item_from_onedrive
# Create your views here.

layout = [["col-lg-4 col-md-6 col-sm-6 co-xs-12"] * 4 + ["col-lg-8 col-md-12 col-sm-12 co-xs-12"],
          ["col-lg-8 col-md-12 col-sm-12 co-xs-12"] + ["col-lg-4 col-md-6 col-sm-6 co-xs-12"] * 4,
          ["col-lg-6 col-md-12 col-sm-12 co-xs-12"] * 2,
          ["col-lg-4 col-md-6 col-sm-6 co-xs-12"] * 6]

def generate_layout():
    index = 0
    increment = 1
    while True:
        for l in layout[index]:
            yield l
        
        index += increment
        
        if index == 0 or index == len(layout) -1:
            increment = -increment


def gallery(request):
    gen = generate_layout()
    photos = { photo: next(gen) for photo in [photo.share_with_link("embed").share_id for photo in get_item_from_onedrive("/Zdjęcia/Lwów").get_items(limit=40) if photo.is_photo or photo.is_image]}

    return render(request, "Gallery/gallery.html", {"photos": photos})
    