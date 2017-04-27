from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import detail_route
from dry_rest_permissions.generics import DRYPermissions

from articles.models import Article
from .serializers import ArticleSerializer


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.order_by('-created')
    serializer_class = ArticleSerializer
    permission_classes = (DRYPermissions, )
    filter_fields = ('author', )
