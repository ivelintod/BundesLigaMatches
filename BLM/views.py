from rest_framework import viewsets
from .models import MatchesBulkData, Team, Match
from .serializers import MatchesBulkDataSerializer, TeamSerializer, MatchSerializer
from .tasks import tasktest


class MatchesBulkDataViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MatchesBulkData.objects.all()
    serializer_class = MatchesBulkDataSerializer


class TeamViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class MatchViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
