from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.db import connection

from djongo import models

# Define models inline for demonstration; in a real project, these would be in models.py
class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    class Meta:
        app_label = 'octofit_tracker'

class Activity(models.Model):
    name = models.CharField(max_length=100)
    user_email = models.EmailField()
    team = models.CharField(max_length=100)
    class Meta:
        app_label = 'octofit_tracker'

class Leaderboard(models.Model):
    user_email = models.EmailField()
    team = models.CharField(max_length=100)
    score = models.IntegerField()
    class Meta:
        app_label = 'octofit_tracker'

class Workout(models.Model):
    name = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=50)
    class Meta:
        app_label = 'octofit_tracker'

User = get_user_model()

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear collections
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Users
        users = [
            User.objects.create_user(username='superman', email='superman@dc.com', password='password', first_name='Clark', last_name='Kent'),
            User.objects.create_user(username='batman', email='batman@dc.com', password='password', first_name='Bruce', last_name='Wayne'),
            User.objects.create_user(username='ironman', email='ironman@marvel.com', password='password', first_name='Tony', last_name='Stark'),
            User.objects.create_user(username='spiderman', email='spiderman@marvel.com', password='password', first_name='Peter', last_name='Parker'),
        ]

        # Activities
        Activity.objects.create(name='Flight', user_email='superman@dc.com', team='DC')
        Activity.objects.create(name='Martial Arts', user_email='batman@dc.com', team='DC')
        Activity.objects.create(name='Engineering', user_email='ironman@marvel.com', team='Marvel')
        Activity.objects.create(name='Web Swinging', user_email='spiderman@marvel.com', team='Marvel')

        # Leaderboard
        Leaderboard.objects.create(user_email='superman@dc.com', team='DC', score=100)
        Leaderboard.objects.create(user_email='batman@dc.com', team='DC', score=90)
        Leaderboard.objects.create(user_email='ironman@marvel.com', team='Marvel', score=95)
        Leaderboard.objects.create(user_email='spiderman@marvel.com', team='Marvel', score=85)

        # Workouts
        Workout.objects.create(name='Strength Training', difficulty='Hard')
        Workout.objects.create(name='Agility Drills', difficulty='Medium')
        Workout.objects.create(name='Tech Lab', difficulty='Easy')
        Workout.objects.create(name='Stealth Practice', difficulty='Medium')

        # Create unique index on email for users
        with connection.cursor() as cursor:
            cursor.execute('db.get_collection("auth_user").createIndex({ "email": 1 }, { "unique": true })')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
