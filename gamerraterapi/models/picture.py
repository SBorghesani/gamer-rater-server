from django.db import models

class Picture(models.Model):
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    player = models.ForeignKey("Player", on_delete=models.CASCADE)
    pic_url = models.CharField(max_length=55)