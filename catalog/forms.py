from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .openai_helper import ask_assistant

from .models import Console, Computer, VideoGame, BoardGame


class BaseCollectibleForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Save'))

    def save(self, commit=True):
        instance = super().save(commit=False)
        if not instance.description:
            prompt = f"Provide a short description for {instance.name} ({instance.company})."
            try:
                instance.description = ask_assistant(prompt)
            except Exception:
                pass
        if commit:
            instance.save()
            self.save_m2m()
        return instance


class ConsoleForm(BaseCollectibleForm):
    class Meta:
        model = Console
        fields = '__all__'


class ComputerForm(BaseCollectibleForm):
    class Meta:
        model = Computer
        fields = '__all__'


class VideoGameForm(BaseCollectibleForm):
    class Meta:
        model = VideoGame
        fields = '__all__'


class BoardGameForm(BaseCollectibleForm):
    class Meta:
        model = BoardGame
        fields = '__all__'
