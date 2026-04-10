from django.test import TestCase
from django.contrib.auth.models import User
from .models import Team, Activity, Leaderboard, Workout

class BasicModelTests(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(str(team), 'Test Team')
    def test_activity_creation(self):
        activity = Activity.objects.create(name='Test', user_email='test@example.com', team='Test Team')
        self.assertEqual(str(activity), 'Test (test@example.com)')
    def test_leaderboard_creation(self):
        lb = Leaderboard.objects.create(user_email='test@example.com', team='Test Team', score=42)
        self.assertEqual(str(lb), 'test@example.com - 42')
    def test_workout_creation(self):
        workout = Workout.objects.create(name='Test Workout', difficulty='Easy')
        self.assertEqual(str(workout), 'Test Workout (Easy)')
