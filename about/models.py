from django.db import models
from django.contrib.sitemaps import Sitemap
from django.urls import reverse

# Create your models here.
class AboutStaticSitemap(Sitemap):
    priority = 0.5
    changefreq = 'never'
    protocol = 'https'

    def items(self):
        return ['about']

    def location(self, item):
        return reverse(item)