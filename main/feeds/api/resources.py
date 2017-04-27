from rest_framework.viewsets import ModelViewSet

from feeds.models import Action
from .serializers import ActionSerializer


class ActionViewSet(ModelViewSet):
    queryset = Action.objects.order_by('-timestamp')
    serializer_class = ActionSerializer
    filter_fields = (
        'actor', 'type'
    )
