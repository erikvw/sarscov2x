from pprint import pprint

from django.test import TestCase
from django.urls import reverse
from edc_utils import get_utcnow
from model_bakery.baker import make_recipe, prepare_recipe

from .forms import CoronavirusKapForm
from .baker_recipes import coronaviruskap_options
from .models import CoronavirusKap


class TestCorona(TestCase):

    def test_model(self):
        obj = prepare_recipe("coronavirus.coronaviruskap")
        obj.save()

    def test_form(self):
        screening_identifier = "12345"
        coronaviruskap_options.update(
            subject_identifier=screening_identifier,
            screening_identifier=screening_identifier,
        )
        form = CoronavirusKapForm(
            data=coronaviruskap_options,
        )
        form.is_valid()
        self.assertEqual(form._errors, {})

    def test_form_get(self):
        screening_identifier = "12345"
        coronaviruskap_options.update(
            subject_identifier=screening_identifier,
            screening_identifier=screening_identifier,
        )
        opts = {k: v for k, v in coronaviruskap_options.items() if v is not None}
        url = reverse("admin:coronavirus_coronaviruskap_add")
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)

django_webtest