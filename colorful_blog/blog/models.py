from django.conf import settings
from django.db import models
from django.utils import timezone

User = settings.AUTH_USER_MODEL


class BlogPostQuerySet(models.QuerySet):
    def published(self):
        now = timezone.now()
        return self.filter(published_date__lte=now)


class BlogPostManager(models.Manager):
    def queryset(self):
        return BlogPostQuerySet(self.model, using=self._db)

    def published(self):
        return self.get_queryset().published()


class BlogPost(models.Model):
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    content = models.TextField(null=True, blank=True)
    published_date = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    objects = BlogPostManager()

    class Meta:
        ordering: ['-published_date', '-updated', '-timestamp']

    def get_absolute_url(self):
        return F'/blog/{self.slug}'

    def get_absolute_url_update(self):
        return f'{self.get_absolute_url()}/edit'

    def get_absolute_url_delete(self):
        return f'{self.get_absolute_url()}/delete'
