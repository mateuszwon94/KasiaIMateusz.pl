from django.shortcuts import render
# from KasiaIMateusz.utils import get_item_from_onedrive

# Create your views here.


def gallery(request):
    # photos = { photo: next(gen) for photo in [photo.share_with_link("embed").share_id for photo in get_item_from_onedrive("/Zdjęcia/Lwów").get_items(limit=40) if photo.is_photo or photo.is_image]}
    photos = {"2019_10_16_kasia_mateusz_{0:0=3d}.jpg".format(i): "mb-3 pics animation all" for i in range(1, 65)}

    return render(request, "Gallery/gallery.html", {"photos": photos})
    