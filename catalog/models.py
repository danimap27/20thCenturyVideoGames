from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from django.utils.translation import gettext_lazy as _

from mediafiles.models import Photo


class Collectible(models.Model):
    class Region(models.TextChoices):
        PAL = "PAL", "PAL"
        NTSC = "NTSC", "NTSC"

    class Edition(models.TextChoices):
        STANDARD = "standard", "Standard"
        LIMITED = "limited", "Limited"

    class Condition(models.TextChoices):
        NEW = "new", "New"
        USED = "used", "Used"

    name = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    release_year = models.PositiveIntegerField()
    acquisition_date = models.DateField(null=True, blank=True)
    purchase_price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    market_price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    launch_price = models.DecimalField(max_digits=8, decimal_places=2)
    region = models.CharField(max_length=10, choices=Region.choices)
    edition = models.CharField(max_length=20, choices=Edition.choices, default=Edition.STANDARD)
    condition = models.CharField(max_length=10, choices=Condition.choices)
    description = models.TextField()
    history = models.TextField(blank=True)
    photos = GenericRelation(Photo)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return self.name


class Console(Collectible):
    class FormFactor(models.TextChoices):
        PORTABLE = "portable", "Portable"
        DESKTOP = "desktop", "Desktop"

    form_factor = models.CharField(max_length=20, choices=FormFactor.choices)
    players = models.PositiveIntegerField(default=1)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("catalog:console_detail", args=[self.pk])


class Computer(Collectible):
    cpu = models.CharField(max_length=100)
    ram_kb = models.PositiveIntegerField()

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("catalog:computer_detail", args=[self.pk])


class VideoGame(Collectible):
    platform = models.ForeignKey(Console, on_delete=models.CASCADE)
    developer = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("catalog:videogame_detail", args=[self.pk])


class BoardGame(Collectible):
    players_min = models.PositiveIntegerField()
    players_max = models.PositiveIntegerField()
    playing_time = models.PositiveIntegerField(help_text=_("Minutes"))

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("catalog:boardgame_detail", args=[self.pk])
