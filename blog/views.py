from django.shortcuts import render
from blog.models import Post

# Create your views here.
def posts_view(request):
    posts = Post.objects.filter(status='PUBLISHED').order_by('-created')[:20]
    context = {
        'posts': posts
    }
    return render(request, 'posts.html', context)

def single_view(request, permalink):
    post = Post.objects.get(permalink=permalink)
    other_posts = Post.objects.filter(status='PUBLISHED').exclude(id=post.id).order_by('-created')[:4]
    context = {
        'post': post,
        'posts': other_posts
    }
    return render(request, 'single.html', context)