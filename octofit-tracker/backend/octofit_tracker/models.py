from djongo import models
from django.contrib.auth.models import AbstractUser

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name

class Activity(models.Model):
    name = models.CharField(max_length=100)
    user_email = models.EmailField()
    team = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.name} ({self.user_email})"

class Leaderboard(models.Model):
    user_email = models.EmailField()
    team = models.CharField(max_length=100)
    score = models.IntegerField()
    def __str__(self):
        return f"{self.user_email} - {self.score}"

class Workout(models.Model):
    name = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.name} ({self.difficulty})"
