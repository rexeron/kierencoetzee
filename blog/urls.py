from django.urls import path
from blog.views import posts_view, single_view

urlpatterns = [
    path(r'', posts_view, name='posts'),
    path(r'<permalink>', single_view, name='posts'),
]