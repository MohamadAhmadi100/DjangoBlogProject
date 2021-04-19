from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField


class PublishManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='public')


class Post(models.Model):
    STATUS = (('draft', 'پیش نویس'), ('public', 'عمومی'))
    title = models.CharField(max_length=120)
    slug = models.SlugField(max_length=120, unique=True)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextUploadingField()
    publish_date = models.DateTimeField(default=timezone.now)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=60, choices=STATUS, default='draft')
    objects = models.Manager()
    public_manager = PublishManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail',
                       args=[self.publish_date.year, self.publish_date.month, self.publish_date.day, self.id,
                             self.slug])
