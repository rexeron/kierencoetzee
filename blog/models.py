from django.db import models
from django.conf import settings
from .constants import POST_STATUS_CHOICES, COMMENT_STATUS_CHOICES


class PostCategory(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        db_table = 'blog_post_category'
        ordering = ('name',)

class Post(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()
    blurb = models.TextField()
    status = models.CharField(max_length=16, choices=POST_STATUS_CHOICES, default='DRAFT')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey(PostCategory, on_delete=models.CASCADE, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('title',)


class Comment(models.Model):
    content = models.TextField()
    status = models.CharField(max_length=32, choices=COMMENT_STATUS_CHOICES, default='PENDING')
    created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    parent_post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent_comment_id = models.ForeignKey('Comment', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        ordering = ('content',)