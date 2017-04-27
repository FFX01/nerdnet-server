from django.contrib.auth import get_user_model

from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import detail_route
from dry_rest_permissions.generics import DRYPermissions

from .serializers import UserSerializer
from feeds.models import Action
from feeds.api.serializers import ActionSerializer


User = get_user_model()


class UserViewSet(ModelViewSet):
    queryset = User.objects.order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = (DRYPermissions, )

    @detail_route(methods=['get'], url_name='feed')
    def feed(self, request, pk=None):
        actions = Action.objects.filter(actor__id=pk).order_by('-timestamp')
        page = self.paginate_queryset(actions)
        serializer = ActionSerializer(page, many=True)
        serializer.context['request'] = request
        return self.get_paginated_response(
            data=serializer.data
        )
