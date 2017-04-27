from django.core.exceptions import ObjectDoesNotExist

from rest_framework.serializers import RelatedField
from rest_framework.exceptions import ValidationError

from media.models import Image
from media.api.serializers import ImageSerializer
from articles.models import Article
from articles.api.serializers import ArticleSerializer


class ActionGenericRelatedField(RelatedField):

    def to_representation(self, value):
        serializer = None
        if isinstance(value, Article):
            serializer = ArticleSerializer(value)
        elif isinstance(value, Image):
            serializer = ImageSerializer(value)
        else:
            raise ValidationError("The content object is not of a valid type.")
        serializer.context['request'] = self.context.get('request')
        return serializer.data
