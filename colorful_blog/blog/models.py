from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL


class BlogPost(models.Model):
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    content = models.TextField(null=True, blank=True)

    def get_absolute_url(self):
        return F'/blog/{self.slug}'

    def get_absolute_url_update(self):
        return F'/blog/{self.slug}/edit'

    def get_absolute_url_delete(self):
        return F'/blog/{self.slug}/delete'
