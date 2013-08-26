from django.conf.urls import patterns, url


urlpatterns = patterns('{{ cookiecutter.app_name }}.views',
    url(r'^$', '{{ cookiecutter.model_name|lower }}_list', name='{{ cookiecutter.app_name }}_{{ cookiecutter.model_name|lower }}_list'),
    url(r'^create/$', '{{ cookiecutter.model_name|lower }}_create', name='{{ cookiecutter.app_name }}_{{ cookiecutter.model_name|lower }}_create'),
    url(r'^(?P<slug>\S+)/update/$', '{{ cookiecutter.model_name|lower }}_update', name='{{ cookiecutter.app_name }}_{{ cookiecutter.model_name|lower }}_update'),
    url(r'^(?P<slug>\S+)/$', '{{ cookiecutter.model_name|lower }}_detail', name='{{ cookiecutter.app_name }}_{{ cookiecutter.model_name|lower }}_detail'),
)
