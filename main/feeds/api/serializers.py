from rest_framework.serializers import ModelSerializer
from rest_framework.fields import SerializerMethodField

from feeds.models import Action
from common.util.generic_fields import ActionGenericRelatedField


class ActionSerializer(ModelSerializer):
    content_object = ActionGenericRelatedField(read_only=True)
    content_type = SerializerMethodField()

    class Meta:
        model = Action
        fields = (
            'id', 'action_type', 'timestamp', 'actor',
            'content_object', 'content_type'
        )

    def get_content_type(self, obj):
        return obj.content_type.model
