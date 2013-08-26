from django.contrib import admin
from django.shortcuts import redirect

from .models import {{ cookiecutter.model_name }}
from .forms import {{ cookiecutter.model_name }}Form


class AdminRedirectMixin(object):
    def response_add(self, request, obj, post_url_continue=None):
        if not any(('_continue' in request.POST, '_addanother' in request.POST)):
            return redirect(obj.get_absolute_url())
        return super(AdminRedirectMixin, self).response_add(request, obj, post_url_continue)

    def response_change(self, request, obj):
        if not any(('_continue' in request.POST, '_addanother' in request.POST)):
            return redirect(obj.get_absolute_url())
        return super(AdminRedirectMixin, self).response_change(request, obj)

class {{ cookiecutter.model_name }}Admin(AdminRedirectMixin, admin.ModelAdmin):
    form = {{ cookiecutter.model_name }}Form
    list_display = ('name', 'created', 'updated')


admin.site.register({{ cookiecutter.model_name }}, {{ cookiecutter.model_name }}Admin)
