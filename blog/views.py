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
    page_url = f'https://kierencoetzee.com/blog/{post.permalink}'
    page_id = post.id
    context = {
        'post': post,
        'posts': other_posts,
        'page_url': page_url, # for disqus
        'page_id': page_id, # for disqus
    }
    return render(request, 'single.html', context)