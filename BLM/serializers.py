from rest_framework import serializers
from .models import MatchesBulkData


class MatchDaySerializer(serializers.Serializer):
    matchday_data = serializers.JSONField()

    def create(self, validated_data):
        return MatchDay.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.data = validated_data.get('data', instance.data)
        instance.save()
        return instance
