from django.db import models

# Create your models here.


class Serie(models.Model):
    title = models.CharField(max_length=80)
    description = models.CharField(max_length=300)
    premiere_date = models.DateField()


class Season(models.Model):

    description = models.CharField(max_length=300)
    premiere_date = models.DateField()
    episodes = models.ForeignKey(
        Serie,
        on_delete=models.CASCADE,
        null=True,
        blank=False,
        default=None,)


class Episode(models.Model):
    title = models.CharField(max_length=80)
    premiere_date = models.DateField()
    description = models.CharField(max_length=300)
    season = models.ForeignKey(
        Season,
        on_delete=models.CASCADE,
        null=True,
        blank=False,
        default=None,)
