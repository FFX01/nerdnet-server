from django.contrib.auth import get_user_model

from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField
from dry_rest_permissions.generics import DRYPermissionsField

from common.util.image_fields import ImageRelatedField


User = get_user_model()


class UserSerializer(ModelSerializer):
    permissions = DRYPermissionsField()
    avatar = ImageRelatedField(required=False)
    feed = HyperlinkedIdentityField(
        view_name='api:user-feed'
    )

    class Meta:
        model = User
        fields = (
            'id', 'username', 'avatar', 'bio',
            'date_joined', 'permissions', 'feed'
        )
