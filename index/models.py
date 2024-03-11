from django.db import models

# Create your models here.

class Game(models.Model):
    game_name = models.CharField(max_length = 20)
    description = models.CharField(max_length = 50)
    times_played = models.IntegerField(default = 0)

    def __str__(self) -> str:
        return self.game_name + "-> " + self.description + " (" + str(self.times_played) + " veces jugado)"
    
    def is_popular(self) -> bool:
        return self.times_played > 10
    