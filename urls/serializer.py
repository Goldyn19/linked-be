from rest_framework import serializers
from .models import URL


class URLSerializer(serializers.ModelSerializer):
    class Meta:
        model = URL
        fields = ["id", "original_url", "short_url", "created_by", "description"]
        read_only_fields = ['id', 'created_by']

