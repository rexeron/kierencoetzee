from django.db import models
from django.contrib.sitemaps import Sitemap
from django.urls import reverse

# Create your models here.
class HomeStaticSitemap(Sitemap):
    priority = 0.5
    changefreq = 'weekly'
    protocol = 'https'

    def items(self):
        return ['home']

    def location(self, item):
        return reverse(item)