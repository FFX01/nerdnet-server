from rest_framework.viewsets import ModelViewSet
from dry_rest_permissions.generics import DRYPermissions

from media.models import Image
from .serializers import ImageSerializer


class ImageViewSet(ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = (DRYPermissions, )
    filter_fields = ('owner', 'articles')
