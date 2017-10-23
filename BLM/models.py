from django.db import models
from django_mysql.models import JSONField
from django.utils import timezone


def default_val():
    return {}


class MatchesBulkData(models.Model):
    current_matchday_data = JSONField(default=default_val)
    all_season_matches = JSONField(default=default_val)
    last_update = models.DateTimeField(default=timezone.now)

    def recently_updated(self):
        return timezone.now() - self.last_update >= 2


class Team(models.Model):
    name = models.CharField(max_length=128, null=True)
    team_id = models.IntegerField()
    fixtures = JSONField(default=default_val)
    win_loss_ratio = models.DecimalField(default=0.0, decimal_places=4, max_digits=4)


class Match(models.Model):
    host = models.ForeignKey(Team, related_name='host')
    guest = models.ForeignKey(Team, related_name='guest')
    host_goals = models.IntegerField(default=-1)
    guest_goals = models.IntegerField(default=-1)
