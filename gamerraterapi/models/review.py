from django.db import models

class Review(models.Model):
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    player = models.ForeignKey("Player", on_delete=models.CASCADE)
    entry = models.CharField(max_length=55)