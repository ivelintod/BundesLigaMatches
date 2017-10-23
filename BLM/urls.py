from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^kuchi/$', views.check_celery),
]
