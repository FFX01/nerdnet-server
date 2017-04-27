from rest_framework.serializers import ModelSerializer
from rest_framework.fields import ImageField, SerializerMethodField
from dry_rest_permissions.generics import DRYPermissionsField

from media.models import Image


class ImageSerializer(ModelSerializer):
    permissions = DRYPermissionsField()
    image = ImageField()
    image_thumb = ImageField(read_only=True)
    image_small = ImageField(read_only=True)
    image_medium = ImageField(read_only=True)
    image_large = ImageField(read_only=True)
    owner_name = SerializerMethodField()

    class Meta:
        model = Image
        fields = (
            'id', 'title', 'description',
            'owner', 'image_thumb', 'image_small',
            'image', 'image_medium', 'image_large',
            'created', 'updated', 'permissions',
            'owner_name'
        )

    def get_owner_name(self, obj):
        return obj.owner.username
