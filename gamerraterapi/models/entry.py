from django.db import models

class Entry(models.Model):
    entry = models.CharField(max_length=55)
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    player = models.ForeignKey("Player", on_delete=models.CASCADE)