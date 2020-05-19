from edc_constants.constants import NOT_APPLICABLE, OTHER

from .constants import NOT_WORKING_FOR_PAY, WORKING_FOR_PAY

EMPLOYMENT_STATUS = (
    (WORKING_FOR_PAY, "Working for pay / Employed"),
    (NOT_WORKING_FOR_PAY, "Not working for pay / Unemployed"),
)

EMPLOYMENT = (
    ("professional", "Professional (e.g. office"),
    ("labourer", "Labourer"),
    ("self_employed", "Small business, self-employed"),
    (NOT_APPLICABLE, "Not applicable"),
    (OTHER, "Other, specify below"),
)


UNPAID_WORK = (
    ("volunteer", "Volunteer"),
    ("unpaid_intern", "Unpaid Intern"),
    ("housewife", "Housewife"),
    ("retired", "Retired"),
    (NOT_APPLICABLE, "Not applicable"),
    (OTHER, "Other, specify below"),
)

EDUCATION_LEVELS = (
    ("primary", "Up to primary"),
    ("secondary", "Up to secondary"),
    ("tertiary", "Tertiary (University, college)"),
    ("no_education", "No education"),
)

HEALTH_INSURANCE = (
    ("work_scheme", "Work scheme health insurance"),
    ("private", "Private health insurance"),
    ("no_insurance", "No insurance, I pay"),
    (OTHER, "Other, please specify below"),
)

HEALTH_OPINION = (
    ("excellent", "Excellent"),
    ("good", "Good"),
    ("fair", "Fair"),
    ("poor", "Poor"),
)

WORRY_SCALE = (
    ("very", "Very worried"),
    ("somewhat", "Somewhat worried"),
    ("a_little", "A little worried"),
    ("not_at_all", "Not worried at all"),
)

LIKELIHOOD_SCALE = (
    ("very", "Very likely"),
    ("somewhat", "Somewhat likely"),
    ("unlikely", "Not very likely, unlikely"),
    ("not_at_all", "Not at all"),
)
