from collections import OrderedDict

from django.core.exceptions import ObjectDoesNotExist

from rest_framework.serializers import RelatedField
from rest_framework.exceptions import ValidationError

from media.models import Image
from media.api.serializers import ImageSerializer


class ImageRelatedField(RelatedField):

    queryset = Image.objects.all()

    def to_representation(self, value):
        serializer = ImageSerializer(value)
        serializer.context['request'] = self.context.get('request')
        return serializer.data

    def to_internal_value(self, data):
        image_id = data.get('id', None)
        if image_id is None:
            raise ValidationError("Image Id must be provided to update avatar.")
        try:
            return Image.objects.get(id=image_id)
        except ObjectDoesNotExist:
            raise ValidationError("Image object not found.")

    def get_choices(self, cutoff=None):
        queryset = self.get_queryset()
        if queryset is None:
            # Ensure that field.choices returns something sensible
            # even when accessed with a read-only field.
            return {}

        if cutoff is not None:
            queryset = queryset[:cutoff]

        return OrderedDict([
            (
                str(item),
                self.display_value(item)
            )
            for item in queryset
        ])
