from django.conf.urls import url
from . import views

matches_bulk_data_list = views.MatchViewSet.as_view({
    'get': 'list'
})

matches_bulk_data_detail = views.MatchViewSet.as_view({
    'get': 'retrieve'
})

team_list = views.TeamViewSet.as_view({
    'get': 'list'
})

team_detail = views.TeamViewSet.as_view({
    'get': 'retrieve'
})

match_list = views.MatchViewSet.as_view({
    'get': 'list'
})

match_detail = views.MatchViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = [
    url(r'^matches-data/$', matches_bulk_data_list,
        name='matches-bulk-data-list'),
    url(r'^matches-data/(?P<pk>[0-9]+)/$', matches_bulk_data_detail,
        name='matches-bulk-data-detail'),
    url(r'^match/$', match_list, name='match-list'),
    url(r'^match/(?P<pk>[0-9]+)/$', match_detail, name='match-detail'),
    url(r'^team/$', team_list, name='team-list'),
    url(r'^team/(?P<pk>[0-9]+)/$', team_detail, name='team-detail'),
]
