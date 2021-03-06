import requests
import datetime
from celery import shared_task
from .models import MatchesBulkData, Team, Match


CURRENT_MATCHDAY_URL = 'https://www.openligadb.de/api/getmatchdata/bl1'
SELECTED_MATCHDAY_URL = 'https://www.openligadb.de/api/getmatchdata/bl1/{year}/{round}'
ALL_MATCHES_URL = 'https://www.openligadb.de/api/getmatchdata/bl1/{year}'

CURRENT_MATCHDAY_DATA = requests.get(CURRENT_MATCHDAY_URL).json()
current_year = datetime.datetime.now().year
ALL_SEASON_MATCHES = requests.get(ALL_MATCHES_URL.format(year=current_year)).json()


@shared_task
def tasktest(param):
    print('The task executed with argument {}'.format(param))
    return 1


@shared_task
def populate_matchday():
    try:
        matches_data = MatchesBulkData.objects.get(pk=1)
    except MatchesBulkData.DoesNotExist:
        matches_data = MatchesBulkData(current_matchday_data=CURRENT_MATCHDAY_DATA,
                                       all_season_matches=ALL_SEASON_MATCHES)
        matches_data.save()
    else:
        if not matches_data.recently_updated():
            matches_data.current_matchday_data = CURRENT_MATCHDAY_DATA
            matches_data.all_season_matches = ALL_SEASON_MATCHES
            matches_data.save()


@shared_task
def populate_teams():
    Team.objects.all().delete()
    for match in CURRENT_MATCHDAY_DATA:
        for nr_team in ('1', '2'):
            team_db = Team(name=match['Team{}'.format(nr_team)]['TeamName'],
                           team_id=match['Team{}'.format(nr_team)]['TeamId'])
            team_db.save()


@shared_task
def populate_matches():
    Match.objects.all().delete()
    for match in ALL_SEASON_MATCHES:
        host = Team.objects.get(name=match['Team1']['TeamName'])
        guest = Team.objects.get(name=match['Team2']['TeamName'])
        host_goals, guest_goals = -1, -1
        if match['Goals']:
            host_goals = match['Goals'][-1]['ScoreTeam1']
            guest_goals = match['Goals'][-1]['ScoreTeam2']
        match_db = Match(host=host, guest=guest,
                         host_goals=host_goals, guest_goals=guest_goals)
        match_db.save()


@shared_task
def populate_team_fixtures():
    for team in Team.objects.all():
        fixtures_data = {}
        team_host_matches = Match.objects.filter(host=team.pk)
        team_guest_matches = Match.objects.filter(guest=team.pk)
        fixtures_data['host_matches'] = []
        fixtures_data['guest_matches'] = []
        for match in team_host_matches:
            fixtures_data['host_matches'].\
                append({'opponent': match.guest.name,
                        'host_goals': match.host_goals,
                        'guest_goals': match.guest_goals})
        for match in team_guest_matches:
            fixtures_data['guest_matches'].\
                append({'opponent': match.host.name,
                        'host_goals': match.host_goals,
                        'guest_goals': match.guest_goals})
        team.fixtures = fixtures_data
        team.save()


'''
class ImmediateSingleRun:

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        populate_matchday.delay()
        populate_teams.delay()
        populate_matches.delay()


ImmediateSingleRun()
'''
