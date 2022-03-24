from django.shortcuts import render
from blog.models import Post

# Create your views here.
def about_view(request):
    return render(request, 'about.html')