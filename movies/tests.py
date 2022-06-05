from datetime import datetime

from django.db import IntegrityError
from django.test import TestCase
from django.urls import reverse
from django.utils.text import slugify

from .models import Genre, Movie


class TestMovie(TestCase):

    MOVIE_TITLE = "test movie"
    RELEASE_DATE = datetime.strptime("2022-01-06", "%Y-%m-%d")

    def setUp(self):
        self.movie = Movie.objects.create(
            title=self.MOVIE_TITLE,
            release_date=self.RELEASE_DATE,
            api_id=1
        )

    def test_instance(self):
        self.assertEqual(self.movie.title, self.MOVIE_TITLE)
        self.assertEqual(self.movie.api_id, 1)

    def test_unique_api_id_is_enforced(self):
        """ Test that two movies with same api_id are not allowed."""
        with self.assertRaises(IntegrityError):
            Movie.objects.create(
                title="another movie",
                release_date=self.RELEASE_DATE,
                api_id=1
            )

    def test_slug_value(self):
        """
        Test that the slug is automatically added to the movie on creation.
        """
        expected = slugify(self.movie.title)
        actual = self.movie.slug
        self.assertEqual(expected, actual)

    def test_slug_value_for_duplicate_title(self):
        """
        Test that two movies with identical titles get unique slugs.
        """
        movie2 = Movie.objects.create(
            title=self.movie.title,
            release_date=self.RELEASE_DATE,
            api_id=99
        )

        self.assertNotEqual(self.movie.slug, movie2.slug)

    def test_added_date_automatically(self):
        """ Test that the date is automatically saved on creation"""
        self.assertTrue(type(self.movie.added), datetime)

    def test_active_false_by_default(self):
        """ Test that our booleans are set to false by default"""
        self.assertTrue(type(self.movie.active) == bool)
        self.assertFalse(self.movie.active)

    def test_deleted_false_by_default(self):
        """ Test that our booleans are set to false by default"""
        self.assertTrue(type(self.movie.deleted) == bool)
        self.assertFalse(self.movie.deleted)

    def test_str(self):
        """ Test the __str__ method"""
        expected = "test movie"
        actual = str(self.movie)

        self.assertEqual(expected, actual)

    def test_get_absolute_url(self):
        """ Test that get_absolute_url returns the expected URL"""

        expected = reverse("movie_detail", kwargs={"slug": self.movie.slug})
        actual = self.movie.get_absolute_url()

        self.assertEqual(expected, actual)


class TestGenre(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.genre = Genre.objects.create(name="Western", api_id=1)

    def test_has_name(self):
        self.assertEqual(self.genre.name, "Western")

    def test_has_api_id(self):
        self.assertEqual(self.genre.api_id, 1)

    def test_str(self):
        expected = "Western"
        actual = str(self.genre)

        self.assertEqual(expected, actual)
