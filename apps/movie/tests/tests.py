from django.test import TestCase
from django.urls import reverse, reverse_lazy
from apps.movie.models import Movie, Genre
from apps.user.models import User
class MovieTests(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client.login(username='testuser', password='password')
        self.genre1 = Genre.objects.create(title="Action")
        self.genre2 = Genre.objects.create(title="Comedy")

        self.movie = Movie.objects.create(title="Test Movie",director="Test Director", imdb_rating=5.5)
        self.movie.genre.set([self.genre1, self.genre2])
        self.movie.save()

    def test_movie_list_view(self):
        response = self.client.get(reverse('movies'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'movie/list.html')
        self.assertContains(response, self.movie.title)

    def test_movie_create_view(self):
        genre = Genre.objects.create(title="Drama")
        response = self.client.post(reverse('create-movie'), {
            'title': 'New Movie',
            'genre': [genre.id],
            'director':"Test Director", 
            'imdb_rating':5.5,
            'poster': '',
        })
        self.assertRedirects(response, reverse_lazy('movies'))
        self.assertTrue(Movie.objects.filter(title="New Movie").exists())

    def test_movie_update_view(self):
        response = self.client.get(reverse('update-movie', args=[self.movie.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'movie/update.html')

        response = self.client.post(reverse('update-movie', args=[self.movie.id]), {
            'title': 'Updated Movie Title',
            'genre': [genre.id for genre in self.movie.genre.all()],
            'director':"Test Director", 
            'imdb_rating':5.5,
        })

        self.assertRedirects(response, reverse_lazy('movies'))
        self.movie.refresh_from_db()
        self.assertEqual(self.movie.title, 'Updated Movie Title')

    def test_movie_delete_view(self):
        response = self.client.get(reverse('delete-movie', args=[self.movie.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'movie/delete.html')

        response = self.client.post(reverse('delete-movie', args=[self.movie.id]))
        self.assertRedirects(response, reverse_lazy('movies'))
        self.assertFalse(Movie.objects.filter(id=self.movie.id).exists())