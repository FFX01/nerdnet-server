from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.conf import settings


User = settings.AUTH_USER_MODEL


class Image(models.Model):
    image = models.ImageField(
        upload_to='img/%Y/%m/%d',
        blank=False,
        null=False
    )
    image_thumb = ImageSpecField(
        source='image',
        processors=[ResizeToFill(64, 64)],
        format='JPEG',
        options={
            'quality': 60
        }
    )
    image_small = ImageSpecField(
        source='image',
        processors=[ResizeToFill(128, 128)],
        format='JPEG',
        options={
            'quality': 80
        }
    )
    image_medium = ImageSpecField(
        source='image',
        processors=[ResizeToFill(256, 256)],
        format='JPEG',
        options={
            'quality': 90
        }
    )
    image_large = ImageSpecField(
        source='image',
        processors=[ResizeToFill(528, 528)],
        format='JPEG',
        options={
            'quality': 100
        }
    )
    title = models.CharField(
        max_length=255,
        blank=True
    )
    description = models.TextField(
        blank=True
    )
    owner = models.ForeignKey(
        to=User,
        related_name='images'
    )
    created = models.DateTimeField(
        auto_now_add=True,
        blank=True
    )
    updated = models.DateTimeField(
        auto_now=True,
        blank=True
    )

    def __str__(self):
        return "{0}: {1} [{2}]".format(self.id, self.title, self.image.url)

    @staticmethod
    def has_read_permission(request):
        return True

    @staticmethod
    def has_write_permission(request):
        return request.user.is_authenticated()

    def has_object_read_permission(self, request):
        return True

    def has_object_write_permission(self, request):
        return request.user == self.owner
