import django_filters

from .models import Console, Computer, VideoGame, BoardGame


class CollectibleFilter(django_filters.FilterSet):
    release_year = django_filters.NumberFilter(field_name='release_year')
    region = django_filters.ChoiceFilter(field_name='region', choices=Console.Region.choices)
    edition = django_filters.ChoiceFilter(field_name='edition', choices=Console.Edition.choices)
    condition = django_filters.ChoiceFilter(field_name='condition', choices=Console.Condition.choices)


class ConsoleFilter(CollectibleFilter):
    class Meta:
        model = Console
        fields = ['release_year', 'region', 'edition', 'condition']


class ComputerFilter(CollectibleFilter):
    class Meta:
        model = Computer
        fields = ['release_year', 'region', 'edition', 'condition']


class VideoGameFilter(CollectibleFilter):
    class Meta:
        model = VideoGame
        fields = ['release_year', 'region', 'edition', 'condition', 'platform']


class BoardGameFilter(CollectibleFilter):
    class Meta:
        model = BoardGame
        fields = ['release_year', 'region', 'edition', 'condition']
