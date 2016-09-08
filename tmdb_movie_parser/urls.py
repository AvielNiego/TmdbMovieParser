from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'(?P<name>.*)/(?P<year>[0-9]{4})', views.parse_movie, name='parse_movie'),
    url(r'(?P<name>.*)', views.parse_movie, name='parse_movie'),
]

