from django.db import models
from django.conf import settings


User = settings.AUTH_USER_MODEL


class Article(models.Model):
    title = models.CharField(
        max_length=255,
        blank=False
    )
    created = models.DateTimeField(
        auto_now_add=True
    )
    updated = models.DateTimeField(
        auto_now=True
    )
    is_draft = models.BooleanField(
        default=False
    )
    author = models.ForeignKey(
        to=User,
        related_name='authored_articles'
    )
    main_image = models.ForeignKey(
        to='media.Image',
        blank=True,
        null=True,
        related_name='article_mains'
    )
    images = models.ManyToManyField(
        to='media.Image',
        related_name='articles'
    )
    body = models.TextField()

    @staticmethod
    def has_read_permission(request):
        return True

    @staticmethod
    def has_write_permission(request):
        return request.user.is_authenticated()

    def has_object_read_permission(self, request):
        if request.user != self.author:
            return not self.is_draft
        return True

    def has_object_write_permission(self, request):
        return request.user == self.author
