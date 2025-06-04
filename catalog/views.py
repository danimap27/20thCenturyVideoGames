from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from django_filters.views import FilterView

from .models import Console, Computer, VideoGame, BoardGame
from .forms import ConsoleForm, ComputerForm, VideoGameForm, BoardGameForm
from .filters import ConsoleFilter, ComputerFilter, VideoGameFilter, BoardGameFilter


class IndexView(generic.TemplateView):
    template_name = "catalog/index.html"


class ConsoleListView(FilterView):
    model = Console
    paginate_by = 10
    filterset_class = ConsoleFilter
    template_name = "catalog/console_list.html"


class ConsoleDetailView(generic.DetailView):
    model = Console
    template_name = "catalog/console_detail.html"


class ConsoleCreateView(LoginRequiredMixin, generic.CreateView):
    model = Console
    form_class = ConsoleForm
    template_name = "catalog/console_form.html"
    success_url = reverse_lazy("catalog:console_list")


class ConsoleUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Console
    form_class = ConsoleForm
    template_name = "catalog/console_form.html"
    success_url = reverse_lazy("catalog:console_list")


class ConsoleDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Console
    template_name = "catalog/confirm_delete.html"
    success_url = reverse_lazy("catalog:console_list")


class ComputerListView(FilterView):
    model = Computer
    paginate_by = 10
    filterset_class = ComputerFilter
    template_name = "catalog/computer_list.html"


class ComputerDetailView(generic.DetailView):
    model = Computer
    template_name = "catalog/computer_detail.html"


class ComputerCreateView(LoginRequiredMixin, generic.CreateView):
    model = Computer
    form_class = ComputerForm
    template_name = "catalog/computer_form.html"
    success_url = reverse_lazy("catalog:computer_list")


class ComputerUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Computer
    form_class = ComputerForm
    template_name = "catalog/computer_form.html"
    success_url = reverse_lazy("catalog:computer_list")


class ComputerDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Computer
    template_name = "catalog/confirm_delete.html"
    success_url = reverse_lazy("catalog:computer_list")


class VideoGameListView(FilterView):
    model = VideoGame
    paginate_by = 10
    filterset_class = VideoGameFilter
    template_name = "catalog/videogame_list.html"


class VideoGameDetailView(generic.DetailView):
    model = VideoGame
    template_name = "catalog/videogame_detail.html"


class VideoGameCreateView(LoginRequiredMixin, generic.CreateView):
    model = VideoGame
    form_class = VideoGameForm
    template_name = "catalog/videogame_form.html"
    success_url = reverse_lazy("catalog:videogame_list")


class VideoGameUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = VideoGame
    form_class = VideoGameForm
    template_name = "catalog/videogame_form.html"
    success_url = reverse_lazy("catalog:videogame_list")


class VideoGameDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = VideoGame
    template_name = "catalog/confirm_delete.html"
    success_url = reverse_lazy("catalog:videogame_list")


class BoardGameListView(FilterView):
    model = BoardGame
    paginate_by = 10
    filterset_class = BoardGameFilter
    template_name = "catalog/boardgame_list.html"


class BoardGameDetailView(generic.DetailView):
    model = BoardGame
    template_name = "catalog/boardgame_detail.html"


class BoardGameCreateView(LoginRequiredMixin, generic.CreateView):
    model = BoardGame
    form_class = BoardGameForm
    template_name = "catalog/boardgame_form.html"
    success_url = reverse_lazy("catalog:boardgame_list")


class BoardGameUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = BoardGame
    form_class = BoardGameForm
    template_name = "catalog/boardgame_form.html"
    success_url = reverse_lazy("catalog:boardgame_list")


class BoardGameDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = BoardGame
    template_name = "catalog/confirm_delete.html"
    success_url = reverse_lazy("catalog:boardgame_list")


class ConsoleTimelineView(generic.ListView):
    model = Console
    template_name = "catalog/timeline.html"
    paginate_by = 20
    ordering = ["release_year"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["timeline_type"] = "consoles"
        return context


class ComputerTimelineView(generic.ListView):
    model = Computer
    template_name = "catalog/timeline.html"
    paginate_by = 20
    ordering = ["release_year"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["timeline_type"] = "computers"
        return context


class VideoGameTimelineView(generic.ListView):
    model = VideoGame
    template_name = "catalog/timeline.html"
    paginate_by = 20
    ordering = ["release_year"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["timeline_type"] = "videogames"
        return context


class BoardGameTimelineView(generic.ListView):
    model = BoardGame
    template_name = "catalog/timeline.html"
    paginate_by = 20
    ordering = ["release_year"]
