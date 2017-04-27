from rest_framework.serializers import ModelSerializer
from rest_framework.fields import SerializerMethodField
from dry_rest_permissions.generics import DRYPermissionsField

from articles.models import Article
from common.util.image_fields import ImageRelatedField


class ArticleSerializer(ModelSerializer):
    permissions = DRYPermissionsField()
    main_image = ImageRelatedField()
    images = ImageRelatedField(
        many=True,
        required=False
    )
    author_name = SerializerMethodField()

    class Meta:
        model = Article
        fields = (
            'id', 'title', 'body',
            'created', 'updated', 'is_draft',
            'author', 'author_name', 'images',
            'permissions', 'main_image'
        )

    def get_author_name(self, obj):
        return obj.author.username
