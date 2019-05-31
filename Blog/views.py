from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.

def allblogs(request):
    all_blogs = Blog.objects
    return render(request, "Blog/allblogs.html", {"Blogs" : all_blogs})

def detail(request, blog_id):
    blog_object = get_object_or_404(Blog, pk=blog_id)
    return render(request, "Blog/detail.html", { "Blog" : blog_object })
