from gamerraterapi.models import game_category
from django.db import models

class Game(models.Model):
    title = models.CharField(max_length=55)
    description = models.CharField(max_length=55)
    designer = models.CharField(max_length=55)
    year_released = models.IntegerField()
    num_players = models.IntegerField()
    time_to_play = models.IntegerField()
    age_rec = models.IntegerField()
    categories = models.ManyToManyField("Category", through="GameCategory", related_name="categories")