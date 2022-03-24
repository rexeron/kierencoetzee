from django.urls import path
from about.views import about_view

urlpatterns = [
    path(r'', about_view, name='about'),
]