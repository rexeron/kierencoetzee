"""kierencoetzee URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include
from django.views.generic.base import TemplateView
from home.views import home_view
from about.models import AboutStaticSitemap
from blog.models import BlogSitemap, BlogStaticSitemap
from home.models import HomeStaticSitemap


sitemaps = {
    'about_static': AboutStaticSitemap,
    'blog': BlogSitemap,
    'blog_static': BlogStaticSitemap,
    'home_static': HomeStaticSitemap,
}

urlpatterns = [
    # third party specific
    path(r'admin/', admin.site.urls),
    path(r'summernote/', include('django_summernote.urls')),

    # my routes
    path(r'', home_view, name='home'),
    path(r'about/', include('about.urls')),
    path(r'blog/', include('blog.urls')),
    path(r'robots.txt', TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
    path(r'sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),

]

# https://github.com/summernote/django-summernote
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)