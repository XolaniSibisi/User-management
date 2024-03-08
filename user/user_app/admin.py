from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ("email", "is_staff", "is_active",)
    list_filter = ("email", "is_staff", "is_active",)
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal Info", {"fields": ("first_name", "last_name", "contact_number", "birth_date", "id_type", "id_or_passport", "age")}),
        ("More Info", {"fields": ("title", "youth", "gender", "race", "disability", "home_language", "citezenship", "nationality", "employment_status", "unemployed_period", "home_address", "postal_address", "postal_code", "contract_number", "contracted_learning_status", "learner_enrollment_number", "learning_programe_name", "subcategory", "intervention", "start_date", "end_date", "guardian_id_no", "guardian_full_name", "guardian_contact", "province", "municipality", "town_or_city", "urban_or_rural", "occupation_level", "job_title", "OFO_occupation_code", "OFO_specialization", "OFO_occupation", "highest_school_qualification", "highest_qualification", "student_number", "bursary_awarded_date", "bursary_completion_status", "popi_consent", "popi_consent_date")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "is_staff",
                "is_active", "groups", "user_permissions"
            )}
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)


admin.site.register(CustomUser, CustomUserAdmin)
