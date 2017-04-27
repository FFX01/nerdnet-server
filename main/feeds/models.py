from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver


User = settings.AUTH_USER_MODEL


ACTION_CHOICES = (
    ('create', 'Create'),
    ('update', 'Update'),
    ('delete', 'Delete')
)


class Action(models.Model):
    action_type = models.CharField(
        max_length=255,
        choices=ACTION_CHOICES,
        blank=False
    )
    timestamp = models.DateTimeField(
        auto_now_add=True,
        blank=True
    )
    actor = models.ForeignKey(
        to=User,
        related_name='actions'
    )
    content_type = models.ForeignKey(
        to=ContentType,
        on_delete=models.CASCADE
    )
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey(
        'content_type',
        'object_id'
    )


"""
Define post save listeners for the objects we would like to create actions for.
"""


@receiver(post_save, sender='articles.Article', dispatch_uid='create_article_action')
def create_article_action(sender, instance, created, **kwargs):
    if created:
        Action.objects.create(
            action_type='create',
            actor=instance.author,
            content_object=instance
        )
    else:
        Action.objects.create(
            action_type='update',
            actor=instance.author,
            content_object=instance
        )


@receiver(post_save, sender='media.Image', dispatch_uid='create_image_action')
def create_image_action(sender, instance, created, **kwargs):
    if created:
        Action.objects.create(
            action_type='create',
            actor=instance.owner,
            content_object=instance
        )
    else:
        Action.objects.create(
            action_type='update',
            actor=instance.owner,
            content_object=instance
        )
