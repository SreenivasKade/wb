from django.db import models

# Create your models here.

movement = (
    ('up', 'up'),
    ('down', 'down'),
    ('left', 'left'),
    ('right', 'right'),
    ('stop', 'stop'),
)

class Move(models.Model):
    time = models.DecimalField(decimal_places= 6 , help_text = 'Enter time in seconds', max_digits=20)
    movement = models.CharField(max_length=10, choices = movement)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Move'
        verbose_name_plural = 'Moves'
        ordering = ('-id',)

    def __str__(self):
        return '{}'.format(str(self.id)+" "+self.movement)

    def get_url(self):
        pass