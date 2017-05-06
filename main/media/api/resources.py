from rest_framework.viewsets import ModelViewSet
from dry_rest_permissions.generics import DRYPermissions
import django_filters.rest_framework as filters
from taggit.managers import TaggableManager

from media.models import Image
from .serializers import ImageSerializer


class ImageFilter(filters.FilterSet):
    owner = filters.NumberFilter(name="owner__id", lookup_expr="exact")
    tags = filters.CharFilter(name="tags__name", lookup_expr="iexact")

    class Meta:
        model = Image
        fields = ('owner', 'articles', 'tags')


class ImageViewSet(ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = (DRYPermissions, )
    filter_class = ImageFilter
