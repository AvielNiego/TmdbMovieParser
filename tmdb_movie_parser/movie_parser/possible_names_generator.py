# coding=utf-8
import itertools
import requests

GOOGLE_SUGGESTIONS_URL = "http://suggestqueries.google.com/complete/search?client=firefox&q="
BAD_WORDS = {'3D', u'עברית', u'רוסית', u'תלת', u'מדובב'}


class PossibleNamesGenerator:
    def __init__(self, movie_name):
        self._movie_name = movie_name

    def generate(self):
        yield self._movie_name, 'Normal'
        for bad_word_comb in self._get_bad_words_combinations():
            yield (self._clear_bad_words(bad_word_comb), bad_word_comb)

        for bad_word_comb in self._get_bad_words_combinations():
            google_suggest = self._google_suggest(self._clear_bad_words(bad_word_comb))
            if google_suggest:
                for suggest in google_suggest:
                    yield (suggest, 'Normal')
        google_suggest = self._google_suggest(self._movie_name)
        if google_suggest:
            for suggest in google_suggest:
                yield (suggest, 'Normal')
            for suggest in google_suggest:
                for bad_word_comb in self._get_bad_words_combinations(suggest):
                    yield (self._clear_bad_words(bad_word_comb, suggest), bad_word_comb)

    def _google_suggest(self, name):
        try:
            return requests.get(GOOGLE_SUGGESTIONS_URL + name).json()[1]
        except IndexError:
            return None

    def _clear_bad_words(self, bad_word_comb, movie_name=None):
        movie_name = movie_name if movie_name else self._movie_name
        return reduce(lambda m, b: m.replace(b, ''), bad_word_comb, movie_name)

    def _get_bad_words_combinations(self, movie_name=None):
        bad_words_in_movie = self._get_bad_words_in_movie_name(movie_name)
        return [c for i in range(len(bad_words_in_movie)) for c in itertools.combinations(bad_words_in_movie, i + 1)]

    def _get_bad_words_in_movie_name(self, movie_name=None):
        movie_name = movie_name if movie_name else self._movie_name
        movie_name_words = movie_name.split()
        return [movie_word for movie_word in movie_name_words for bad_word in BAD_WORDS
                if bad_word in movie_word]
