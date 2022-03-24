from django.shortcuts import render
from blog.models import Post

# Create your views here.
def posts_view(request):
    posts = Post.objects.all().order_by('-created')[:20]
    context = {
        'posts': posts
    }
    return render(request, 'posts.html', context)

def single_view(request, permalink):
    post = Post.objects.get(permalink=permalink)
    context = {
        'post': post
    }
    return render(request, 'single.html', context)