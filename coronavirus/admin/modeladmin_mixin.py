from django.contrib import admin
from django.utils.safestring import mark_safe
from django_audit_fields import audit_fieldset_tuple

fieldsets = [
    (
        "Coronavirus Knowledge, Attitudes, and Practices",
        {"fields": ("screening_identifier", "report_datetime")},
    ),
    (
        "Disease Burden: HIV",
        {
            "fields": (
                "hiv_pos",
                "hiv_pos_year",
                "hiv_year_started_art",
                "hiv_missed_doses",
            )
        },
    ),
    (
        "Disease Burden: Diabetes",
        {
            "fields": (
                "diabetic",
                "diabetic_dx_year",
                "diabetic_on_meds",
                "diabetic_missed_doses",
            )
        },
    ),
    (
        "Disease Burden: Hypertension",
        {
            "fields": (
                "hypertensive",
                "hypertensive_dx_year",
                "hypertensive_on_meds",
                "hypertensive_missed_doses",
            )
        },
    ),
    (
        "Indicators",
        {"fields": ("height", "weight", "sys_blood_pressure", "dia_blood_pressure",)},
    ),
    (
        "Economics",
        {
            "fields": (
                "married",
                "employment_status",
                "employment",
                "employment_other",
                "unpaid_work",
                "unpaid_work_other",
                "education",
                "household_size",
                "nights_away",
                "health_insurance",
                "health_insurance_other",
                "personal_health_opinion",
            )
        },
    ),
    (
        "Awareness and Concerns",
        {
            "fields": (
                "perceived_threat",
                "corona_concern",
                "personal_infection_likelihood",
                "family_infection_likelihood",
                "perc_die",
                "perc_mild_symptom",
            )
        },
    ),
    (
        "Knowledge of Coronavirus",
        {
            "description": mark_safe(
                "<h5><font color='orange'>[Interviewer]:</font> For the "
                "questions in this section ask the patient the following:"
                "</h5><h5><BR><B>What do you know about coronavirus "
                "Answer True, False or you don't know</B></h5>"
            ),
            "fields": (
                "spread_droplets",
                "spread_touch",
                "spread_sick",
                "spread_asymptomatic",
                "severity_age",
                "hot_climate",
                "lives_on_materials",
                "spread_touch2",
            ),
        },
    ),
    (
        "Symptoms of Coronavirus",
        {
            "description": mark_safe(
                "<h5><font color='orange'>[Interviewer]:</font> For the "
                "questions in this section ask the patient the following:"
                "</h5><h5><BR><B>Do you think any of the following symptoms are "
                "linked with coronavirus infection? Answer True, False or you "
                "don't know</B></h5>"
            ),
            "fields": (
                "symptoms_fever",
                "symptoms_headache",
                "symptoms_dry_cough",
                "symptoms_body_aches",
                "symptoms_smell",
                "symptoms_breathing",
                "know_other_symptoms",
                "symptoms_other",
            ),
        },
    ),
    (
        "Protecting yourself",
        {
            "description": mark_safe(
                "<h5><font color='orange'>[Interviewer]:</font> For the questions "
                "in this section ask the patient the following:</h5><h5><BR><B>"
                "Do you think the following can protect <u>you</u> "
                "against the coronavirus? True, False or you don't know.</B></h5>"
            ),
            "fields": (
                "hot_drinks",
                "alcohol",
                "wash_hands",
                "hand_sanitizer",
                "take_herbs_prevention",
                "avoid_crowds",
                "face_masks",
                "stay_indoors",
                "social_distance",
                "other_actions_prevention",
            ),
        },
    ),
    (
        "Your response to symptoms",
        {
            "description": mark_safe(
                "<h5><font color='orange'>[Interviewer]:</font> For the questions "
                "in this section ask the patient the following:</h5><h5><BR><B>If "
                "you had symptoms of coronavirus, how likely are you to do any of "
                "the following?</B></h5>"
            ),
            "fields": (
                "stay_home",
                "visit_clinic",
                "call_nurse",
                "take_meds",
                "take_herbs_symptoms",
                "stop_chronic_meds",
                "visit_religious",
                "visit_traditional",
                "other_actions_symptoms",
            ),
        },
    ),
    audit_fieldset_tuple,
]


class CoronaKapModelAdminMixin:

    fieldsets = fieldsets

    filter_horizaontal = ("information_sources",)

    radio_fields = {
        "alcohol": admin.VERTICAL,
        "avoid_crowds": admin.VERTICAL,
        "call_nurse": admin.VERTICAL,
        "corona_concern": admin.VERTICAL,
        "hiv_pos": admin.VERTICAL,
        "diabetic": admin.VERTICAL,
        "diabetic_on_meds": admin.VERTICAL,
        "hypertensive": admin.VERTICAL,
        "hypertensive_on_meds": admin.VERTICAL,
        "education": admin.VERTICAL,
        "employment_status": admin.VERTICAL,
        "face_masks": admin.VERTICAL,
        "family_infection_likelihood": admin.VERTICAL,
        "hand_sanitizer": admin.VERTICAL,
        "health_insurance": admin.VERTICAL,
        "hot_climate": admin.VERTICAL,
        "hot_drinks": admin.VERTICAL,
        "know_other_symptoms": admin.VERTICAL,
        "lives_on_materials": admin.VERTICAL,
        "married": admin.VERTICAL,
        "personal_health_opinion": admin.VERTICAL,
        "personal_infection_likelihood": admin.VERTICAL,
        "employment": admin.VERTICAL,
        "severity_age": admin.VERTICAL,
        "social_distance": admin.VERTICAL,
        "spread_asymptomatic": admin.VERTICAL,
        "spread_droplets": admin.VERTICAL,
        "spread_sick": admin.VERTICAL,
        "spread_touch": admin.VERTICAL,
        "spread_touch2": admin.VERTICAL,
        "stay_home": admin.VERTICAL,
        "stay_indoors": admin.VERTICAL,
        "stop_chronic_meds": admin.VERTICAL,
        "symptoms_body_aches": admin.VERTICAL,
        "symptoms_breathing": admin.VERTICAL,
        "symptoms_dry_cough": admin.VERTICAL,
        "symptoms_fever": admin.VERTICAL,
        "symptoms_headache": admin.VERTICAL,
        "symptoms_smell": admin.VERTICAL,
        "take_herbs_prevention": admin.VERTICAL,
        "take_herbs_symptoms": admin.VERTICAL,
        "take_meds": admin.VERTICAL,
        "unpaid_work": admin.VERTICAL,
        "visit_clinic": admin.VERTICAL,
        "visit_religious": admin.VERTICAL,
        "visit_traditional": admin.VERTICAL,
        "wash_hands": admin.VERTICAL,
    }

    list_display = (
        "human_screening_identifier",
        "report_datetime",
        "protocol",
        "user_created",
        "created",
    )

    search_fields = [
        "screening_identifier",
        "subject_identifier",
    ]

    def human_screening_identifier(self, obj):
        return f"{obj.screening_identifier[0:4]}-{obj.screening_identifier[4:]}"

    human_screening_identifier.short_description = "screening identifier"
