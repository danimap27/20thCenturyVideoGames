from django.urls import path

from . import views

app_name = "catalog"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("consoles/", views.ConsoleListView.as_view(), name="console_list"),
    path("consoles/<int:pk>/", views.ConsoleDetailView.as_view(), name="console_detail"),
    path("consoles/add/", views.ConsoleCreateView.as_view(), name="console_add"),
    path("consoles/<int:pk>/edit/", views.ConsoleUpdateView.as_view(), name="console_edit"),
    path("consoles/<int:pk>/delete/", views.ConsoleDeleteView.as_view(), name="console_delete"),

    path("computers/", views.ComputerListView.as_view(), name="computer_list"),
    path("computers/<int:pk>/", views.ComputerDetailView.as_view(), name="computer_detail"),
    path("computers/add/", views.ComputerCreateView.as_view(), name="computer_add"),
    path("computers/<int:pk>/edit/", views.ComputerUpdateView.as_view(), name="computer_edit"),
    path("computers/<int:pk>/delete/", views.ComputerDeleteView.as_view(), name="computer_delete"),

    path("videogames/", views.VideoGameListView.as_view(), name="videogame_list"),
    path("videogames/<int:pk>/", views.VideoGameDetailView.as_view(), name="videogame_detail"),
    path("videogames/add/", views.VideoGameCreateView.as_view(), name="videogame_add"),
    path("videogames/<int:pk>/edit/", views.VideoGameUpdateView.as_view(), name="videogame_edit"),
    path("videogames/<int:pk>/delete/", views.VideoGameDeleteView.as_view(), name="videogame_delete"),

    path("boardgames/", views.BoardGameListView.as_view(), name="boardgame_list"),
    path("boardgames/<int:pk>/", views.BoardGameDetailView.as_view(), name="boardgame_detail"),
    path("boardgames/add/", views.BoardGameCreateView.as_view(), name="boardgame_add"),
    path("boardgames/<int:pk>/edit/", views.BoardGameUpdateView.as_view(), name="boardgame_edit"),
    path("boardgames/<int:pk>/delete/", views.BoardGameDeleteView.as_view(), name="boardgame_delete"),

    path("timeline/consoles/", views.ConsoleTimelineView.as_view(), name="console_timeline"),
    path("timeline/computers/", views.ComputerTimelineView.as_view(), name="computer_timeline"),
    path("timeline/videogames/", views.VideoGameTimelineView.as_view(), name="videogame_timeline"),
    path("timeline/boardgames/", views.BoardGameTimelineView.as_view(), name="boardgame_timeline"),
]
