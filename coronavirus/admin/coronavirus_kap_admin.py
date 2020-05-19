from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from ..forms import CoronavirusKapForm
from ..models import CoronavirusKap
from .modeladmin_mixin import CoronaKapModelAdminMixin

@admin.register(CoronavirusKap)
class CoronavirusKapAdmin(CoronaKapModelAdminMixin, SimpleHistoryAdmin, admin.ModelAdmin):
    form = CoronavirusKapForm

    list_filter = ("report_datetime", "user_created", "created")
