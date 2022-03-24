from django.shortcuts import render
from blog.models import Post

# Create your views here.
def home_view(request):
    recent_posts = Post.objects.filter(status='PUBLISHED').order_by('-created')[:3]
    context = {
        'recent_posts': recent_posts
    }
    return render(request, 'home.html', context)