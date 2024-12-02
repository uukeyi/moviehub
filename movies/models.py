from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from core.models import TimestampModel
from django.utils.translation import gettext_lazy as _

class FilmWork(TimestampModel):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, verbose_name=_('Title'))
    description = models.TextField(blank=True, null=True, verbose_name=_('Description'))
    data_release = models.DateField(verbose_name=_('Release Date'))
    duration_min = models.PositiveIntegerField(verbose_name=_('Duration (minutes)'))
    rating = models.DecimalField(
        default=1, blank=True, null=True, max_digits=3, decimal_places=1, validators=[
            MinValueValidator(0),
            MaxValueValidator(10)
        ], verbose_name=_('Rating')
    )
    age_limit = models.CharField(max_length=4, choices=[
        ('7+', _('7+')),
        ('12+', _('12+')),
        ('16+', _('16+')),
        ('18+', _('18+')),
    ], verbose_name=_('Age Limit'))
    type = models.CharField(max_length=50, verbose_name=_('Type'))
    language_original = models.CharField(max_length=50, blank=True, null=True, verbose_name=_('Original Language'))
    country = models.CharField(max_length=50, blank=True, null=True, verbose_name=_('Country'))
    budget = models.BigIntegerField(validators=[MinValueValidator(0)], verbose_name=_('Budget'))
    box_office = models.BigIntegerField(validators=[MinValueValidator(0)], verbose_name=_('Box Office'))
    preview = models.CharField(max_length=255, verbose_name=_('Preview'))
    total_views = models.BigIntegerField(validators=[MinValueValidator(0)], default=0, verbose_name=_('Total Views'))
    genres = models.ManyToManyField('Genre', verbose_name=_('Genres'))
    actors = models.ManyToManyField('Actor', verbose_name=_('Actors'))

    class Meta:
        db_table = "content.filmwork"
        verbose_name = _('Film')
        verbose_name_plural = _('Films')

    def __str__(self):
        return f"{self.title} , id:{self.id}"


class Genre(TimestampModel):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, verbose_name=_('Title'))
    description = models.TextField(blank=True, null=True, verbose_name=_('Description'))
    target_audience = models.CharField(choices=[
        ('Kids', _('Kids')),
        ('Teenagers', _('Teenagers')),
        ('Adult', _('Adult'))
    ], max_length=10, verbose_name=_('Target Audience'))

    class Meta:
        db_table = "content.genre"
        verbose_name = _('Genre')
        verbose_name_plural = _('Genres')

    def __str__(self):
        return f"{self.title} , id:{self.id}"


class Actor(TimestampModel):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=150, verbose_name=_('Full Name'))
    birth_date = models.DateField(verbose_name=_('Birth Date'))
    birth_city = models.CharField(max_length=100, verbose_name=_('Birth City'))
    birth_county = models.CharField(max_length=100, verbose_name=_('Birth County'))
    short_bio = models.TextField(blank=True, null=True, verbose_name=_('Short Bio'))
    role = models.CharField(max_length=50, verbose_name=_('Role'))
    nationality = models.CharField(max_length=50, verbose_name=_('Nationality'))
    gender = models.CharField(choices=[('female', _('Female')), ('male', _('Male'))], max_length=6, verbose_name=_('Gender'))
    photo = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('Photo'))  # URL or Image
    start_year = models.PositiveIntegerField(verbose_name=_('Start Year'))
    end_year = models.PositiveIntegerField(blank=True, null=True, verbose_name=_('End Year'))

    class Meta:
        db_table = "content.actor"
        verbose_name = _('Actor')
        verbose_name_plural = _('Actors')

    def __str__(self):
        return f"{self.full_name} , id:{self.id}"
