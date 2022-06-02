from django.test import TestCase
from .models import Movie

from datetime import datetime

class TestMovie(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.movie = Movie.objects.create(
            title="test movie",
            release_date=datetime.strptime("2022-01-06", "%Y-%m-%d"),
            api_id=1
        )

    def test_movie_not_active_by_default(self):
        self.assertFalse(self.movie.active)

    def test_movie_not_deleted_by_default(self):
        self.assertFalse(self.movie.deleted)

    def test_date_automatically_added(self):
        added_date = self.movie.added
        self.assertTrue(type(added_date) == datetime)

    def test_str(self):
        expected = "test movie"
        actual = self.movie.title

        self.assertEqual(expected, actual)
