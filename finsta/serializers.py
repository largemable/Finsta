from rest_framework import serializers
from .models import FinstaEntry


class FinstaEntrySerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
    )

    class Meta:
        model = FinstaEntry
        fields = ['id', 'title', 'caption', 'image', 'user', ]
