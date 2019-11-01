from django.shortcuts import render
# from KasiaIMateusz.utils import get_item_from_onedrive
from KasiaIMateusz.settings import STATIC_URL
# Create your views here.

layout = [["mb-3 pics animation all 2"],
          ["mb-3 pics animation all 1"] * 2,
          ["mb-3 pics animation all 2"] * 2,
          ["mb-3 pics animation all 1"]]

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
    # photos = { photo: next(gen) for photo in [photo.share_with_link("embed").share_id for photo in get_item_from_onedrive("/Zdjęcia/Lwów").get_items(limit=40) if photo.is_photo or photo.is_image]}
    photos = {"2019_10_16_kasia_mateusz_{0:0=3d}.jpg".format(i): next(gen) for i in range(1, 65)}

    return render(request, "Gallery/gallery.html", {"photos": photos})
    