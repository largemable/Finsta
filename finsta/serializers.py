from rest_framework import serializers
from .models import FinstaEntry, User


class FinstaEntrySerializer(serializers.ModelSerializer):
    # user_name = serializers.StringRelatedField(
    #     source='user',
    #     read_only=True
    # )

    class Meta:
        model = FinstaEntry
        fields = ['id', 'title', 'caption', 'image', 'user']


class UserSerializer(serializers.ModelSerializer):
    entries = FinstaEntrySerializer(many=True, read_only=True)

    class Meta:
        model = User
