from django.db import models


class Picture(models.Model):
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    player = models.ForeignKey("Player", on_delete=models.CASCADE)
    pic_url = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)