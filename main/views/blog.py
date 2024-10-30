from django.shortcuts import render
from main.models.blog import Blog


def blog(request):
    blogs = Blog.objects.all()
    data = {
        'blogs': blogs,
    }
    return render(request, 'main/blog/base.html', data)

def blog_details(request, pk):
    blog = Blog.objects.get(id=pk)
    data = {
        'blog': blog
    }
    return render(request, 'main/blog-details/base.html', data)