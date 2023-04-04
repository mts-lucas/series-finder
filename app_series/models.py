from django.db import models

# Create your models here.


class Serie(models.Model):
    title = models.CharField(max_length=80)
    description = models.CharField(max_length=300)
    premiere_date = models.DateField(null=False, blank=False)
    is_published = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title


class Season(models.Model):

    number = models.IntegerField(null=False, blank=False, default=1)
    description = models.CharField(max_length=300)
    premiere_date = models.DateField(null=False, blank=False)
    episodes = models.ForeignKey(
        Serie,
        on_delete=models.CASCADE,
        null=True,
        blank=False,
        default=None,)

    def __str__(self) -> str:
        return f'season {self.number}'


class Episode(models.Model):

    number = models.IntegerField(null=False, blank=False, default=1)
    title = models.CharField(max_length=80)
    premiere_date = models.DateField(null=False, blank=False)
    description = models.CharField(max_length=300)
    season = models.ForeignKey(
        Season,
        on_delete=models.CASCADE,
        null=True,
        blank=False,
        default=None,)

    def __str__(self) -> str:
        return f'{self.number} - {self.title}'
