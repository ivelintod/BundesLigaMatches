from rest_framework import serializers
from .models import MatchesBulkData, Team, Match


class MatchesBulkDataSerializer(serializers.Serializer):
    current_matchday_data = serializers.JSONField()
    all_season_matches = serializers.JSONField()
    last_update = serializers.DateTimeField()

    def create(self, validated_data):
        return MatchesBulkData.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.current_matchday_data = \
            validated_data.get('current_matchday_data',
                               instance.current_matchday_data)
        instance.all_season_matches = \
            validated_data.get('all_season_matches',
                               instance.all_season_matches)
        instance.last_update = validated_data.get('last_update',
                                                  instance.last_update)
        instance.save()
        return instance


class TeamSerializer(serializers.ModelSerializer):
    #matches = serializers.PrimaryKeyRelatedField(many=True, queryset=Match.objects.all())

    class Meta:
        model = Team
        fields = '__all__'


class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = '__all__'
