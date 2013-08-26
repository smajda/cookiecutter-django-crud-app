from django.views.generic import DetailView, ListView, UpdateView, CreateView

from .models import {{ cookiecutter.model_name }}
from .forms import {{ cookiecutter.model_name }}Form


class {{ cookiecutter.model_name }}ListView(ListView):
    model = {{ cookiecutter.model_name }}

{{ cookiecutter.model_name|lower }}_list = {{ cookiecutter.model_name }}ListView.as_view()


class {{ cookiecutter.model_name }}CreateView(CreateView):
    model = {{ cookiecutter.model_name }}
    form_class = {{ cookiecutter.model_name }}Form

{{ cookiecutter.model_name|lower }}_create = {{ cookiecutter.model_name }}CreateView.as_view()


class {{ cookiecutter.model_name }}DetailView(DetailView):
    model = {{ cookiecutter.model_name }}

{{ cookiecutter.model_name|lower }}_detail = {{ cookiecutter.model_name }}DetailView.as_view()


class {{ cookiecutter.model_name }}UpdateView(UpdateView):
    model = {{ cookiecutter.model_name }}
    form_class = {{ cookiecutter.model_name }}Form

{{ cookiecutter.model_name|lower }}_update = {{ cookiecutter.model_name }}UpdateView.as_view()
