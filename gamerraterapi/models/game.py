from gamerraterapi.models import game_category
from django.db import models
from .rating import Rating

class Game(models.Model):
    title = models.CharField(max_length=55)
    description = models.CharField(max_length=55)
    designer = models.CharField(max_length=55)
    year_released = models.IntegerField()
    num_players = models.IntegerField()
    time_to_play = models.IntegerField()
    age_rec = models.IntegerField()
    categories = models.ManyToManyField("Category", through="GameCategory", related_name="categories")

    @property
    def average_rating(self):
        """Average rating calculated attribute for each game"""
        ratings = Rating.objects.filter(game=self)

        # Sum all of the ratings for the game
        total_rating = 0
        for rating in ratings:
            total_rating += rating.rating

        if total_rating == 0:
            return 0
        else:
        # Calculate the averge and return it.
            average_rating = total_rating / len(ratings)
        return average_rating