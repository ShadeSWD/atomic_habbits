from django.db import models
from config import settings

NULLABLE = {"null": True, "blank": True}


class Habit(models.Model):
    PERIODICITY = [(i, i) for i in range(1, 8)]

    created_at = models.DateTimeField(verbose_name='creation date', auto_now_add=True)
    changed_at = models.DateTimeField(verbose_name='change date', auto_now=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='owner')
    place = models.CharField(max_length=50, verbose_name='place of action')
    time = models.TimeField(verbose_name='time of action')
    action = models.CharField(max_length=50, verbose_name='action')
    period = models.IntegerField(verbose_name='periodicity', default=1, choices=PERIODICITY)
    time_for_action = models.DurationField(verbose_name='time for action')
    is_public = models.BooleanField(verbose_name='is public')
    is_pleasant = models.BooleanField(verbose_name='is pleasant')
    connected_habit = models.ForeignKey(on_delete=models.PROTECT, to="Habit", verbose_name='connected pleasant habit',
                                        **NULLABLE)
    award = models.CharField(max_length=50, verbose_name='award', **NULLABLE)

    def __str__(self):
        return f'I will {self.action} at {self.time} at {self.place}'

    class Meta:
        verbose_name = 'habit'
        verbose_name_plural = 'habits'
