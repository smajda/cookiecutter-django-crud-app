import unittest

from django.core.urlresolvers import reverse, NoReverseMatch
from django.test import Client

from .models import


class {{ cookiecutter.model_name }}ViewTest(unittest.TestCase):
    "Some basic tests for our views"
    def setUp(self):
        self.client = Client()

    def testIndex(self):
        url = reverse('{{ cookiecutter.app_name }}_{{ cookiecutter.model_name|lower }}_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def testCreate(self):
        #slug = ''
        #url = reverse('{{ cookiecutter.app_name }}_{{ cookiecutter.model_name|lower }}_create')
        pass

    def testDetail(self):
        #slug = ''
        #url = reverse('{{ cookiecutter.app_name }}_{{ cookiecutter.model_name|lower }}_detail', args=[slug, ])
        pass

    def testUpdate(self):
        #slug = ''
        #url = reverse('{{ cookiecutter.app_name }}_{{ cookiecutter.model_name|lower }}_update', args=[slug, ])
        pass
