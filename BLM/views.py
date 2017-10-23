from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import generics
from .models import MatchesBulkData
from .serializers import MatchDaySerializer
from .tasks import tasktest


@csrf_exempt
def check_celery(request):
    #tasktest('da vidim')
    return JsonResponse({'1': '2'}, status=200)

