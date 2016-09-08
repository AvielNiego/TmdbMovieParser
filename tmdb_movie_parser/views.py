import json
from django.http import HttpResponse
from tmdb_movie_parser.movie_parser.tmdb_movie_parser import TmdbMovieParser


def parse_movie(request, name, year=None):
    """
    :param year: int
    :param name: str
    :type request: HttpRequest
    """
    return HttpResponse(json.dumps(TmdbMovieParser(unicode(name), int(year)).get_info()))
