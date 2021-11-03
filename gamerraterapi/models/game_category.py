from django.db import models

class GameCategory(models.Model):
    cat = models.ForeignKey("Category", on_delete=models.CASCADE)
    game = models.ForeignKey("Game", on_delete=models.CASCADE)