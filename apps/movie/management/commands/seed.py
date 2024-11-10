from django.core.management.base import BaseCommand

from apps.movie.models import Genre

class Command(BaseCommand):
    help = 'Seed the database with initial data'

    def handle(self, *args, **kwargs):
        self.seed_genre()
    
    def seed_genre(self):
        genres=['Action','Comedy','Documentary','Drama','Fantasy','Horror','Musical','Mystery','Romance','Science Fiction','Thriller']
        for genre in genres:
            Genre.objects.get_or_create(title=genre)