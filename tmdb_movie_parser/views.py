import json
from django.http import HttpResponse
from tmdb_movie_parser.movie_parser.tmdb_movie_parser import TmdbMovieParser


def parse_movie(request, name):
    """
    :param name: str
    :type request: HttpRequest
    """
    return HttpResponse(json.dumps(TmdbMovieParser().get_info(unicode(name))))
