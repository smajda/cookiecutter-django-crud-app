from django.db import models
from django.core.urlresolvers import reverse

from autoslug import AutoSlugField


class {{ cookiecutter.model_name }}(models.Model):
    name = models.CharField(max_length=255)
    slug = AutoSlugField(
        populate_from='name',
        blank=True,
        editable=True,
        )
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        ordering = ('-created', )

    def __unicode__(self):
        return self.slug

    def get_absolute_url(self):
        return reverse('{{ cookiecutter.app_name }}_{{ cookiecutter.model_name|lower }}_detail', args=(self.slug, ))
