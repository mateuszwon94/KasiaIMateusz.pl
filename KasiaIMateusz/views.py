from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, "home.html")

def count(request):
    full_text = request.GET["FullText"]
    count = len(full_text.split())

    return render(request, "count.html", {"FullText" : full_text , "Count": count})