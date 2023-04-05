from django.db import models

# Create your models here.


class Gender(models.Model):
    name = models.CharField(max_length=45)

    def __str__(self) -> str:
        return self.name


class Serie(models.Model):
    title = models.CharField(max_length=80)
    description = models.CharField(max_length=300)
    premiere_date = models.DateField(null=False, blank=False)

    genders = models.ManyToManyField(Gender, related_name='series')

    def __str__(self) -> str:
        return self.title


class Season(models.Model):

    number = models.IntegerField(null=False, blank=False, default=1)
    description = models.CharField(max_length=300)
    premiere_date = models.DateField(null=False, blank=False)
    serie = models.ForeignKey(
        Serie,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        default=None,
        related_name='seasons',)

    def __str__(self) -> str:
        return f'{self.serie} S{self.number}'


class Episode(models.Model):

    number = models.IntegerField(null=False, blank=False, default=1)
    title = models.CharField(max_length=80)
    premiere_date = models.DateField(null=False, blank=False)
    description = models.CharField(max_length=300)
    season = models.ForeignKey(
        Season,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        default=None,
        related_name='episodes',)

    def __str__(self) -> str:
        return f'{self.season}E{self.number}'
