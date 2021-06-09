from rest_framework import serializers
from .models import FinstaEntry


class FinstaEntrySerializer(serializers.ModelSerializer):
    # user_name = serializers.StringRelatedField(
    #     source='user',
    #     read_only=True
    # )

    class Meta:
        model = FinstaEntry
        fields = ['id', 'title', 'caption', 'image', 'user']
