from django import forms
from django.apps import apps as django_apps
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from edc_constants.constants import YES
from edc_form_validators.form_validator import FormValidator

from ..constants import NOT_WORKING_FOR_PAY, WORKING_FOR_PAY


class CoronaKapFormValidator(FormValidator):
    def clean(self):

        self.validate_identifier()

        self.required_if(YES, field="hiv_pos", field_required="hiv_pos_year")
        self.required_if(YES, field="hiv_pos", field_required="hiv_year_started_art")
        self.required_if(
            YES,
            field="hiv_pos",
            field_required="hiv_missed_doses",
            field_required_evaluate_as_int=True,
        )
        self.required_if(YES, field="diabetic", field_required="diabetic_dx_year")
        self.applicable_if(YES, field="diabetic", field_applicable="diabetes_on_meds")
        self.required_if(
            YES,
            field="diabetic",
            field_required="diabetic_missed_doses",
            field_required_evaluate_as_int=True,
        )
        self.required_if(
            YES, field="hypertensive", field_required="hypertensive_dx_year"
        )
        self.applicable_if(
            YES, field="hypertensive", field_applicable="hypertensive_on_meds"
        )
        self.required_if(
            YES,
            field="hypertensive",
            field_required="hypertensive_missed_doses",
            field_required_evaluate_as_int=True,
        )

        self.applicable_if(
            WORKING_FOR_PAY, field="employment_status", field_applicable="employment"
        )
        self.validate_other_specify(field="employment")

        self.applicable_if(
            NOT_WORKING_FOR_PAY,
            field="employment_status",
            field_applicable="unpaid_work",
        )
        self.validate_other_specify(field="unpaid_work")

        self.validate_other_specify(field="health_insurance")
        self.required_if(
            YES, field="know_other_symptoms", field_required="symptoms_other"
        )

    @property
    def unformatted_screening_identifier(self):
        return (
            self.cleaned_data.get("screening_identifier")
            .replace("-", "")
            .replace(" ", "")
        )

    def validate_identifier(self):
        subject_screening_model = getattr(settings, "SUBJECT_SCREENING_MODEL", None)
        if subject_screening_model and self.cleaned_data.get("screening_identifier"):
            model_cls = django_apps.get_model(subject_screening_model)
            try:
                model_cls.objects.get(
                    screening_identifier=self.unformatted_screening_identifier
                )
            except ObjectDoesNotExist:
                raise forms.ValidationError(
                    {"screening_identifier": "Unknown screening identifier"}
                )
