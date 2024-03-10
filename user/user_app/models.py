from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=20, null=True, blank=True)
    last_name = models.CharField(max_length=20, null=True, blank=True)
    username = None
    email = models.EmailField(_("email address"), unique=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    contact_number = models.CharField(max_length=10, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    id_or_passport = models.CharField(max_length=13, null=True, blank=True)
    id_type = models.CharField(max_length=20, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    title = models.CharField(max_length=5, null=True, blank=True)
    youth = models.CharField(max_length=3, null=True, blank=True)
    gender = models.CharField(max_length=50, null=True, blank=True)
    race = models.CharField(max_length=50, null=True, blank=True)
    disability = models.CharField(max_length=50, null=True, blank=True)
    home_language = models.CharField(max_length=50, null=True, blank=True)
    citezenship = models.CharField(max_length=50, null=True, blank=True)
    nationality = models.CharField(max_length=50, null=True, blank=True)
    employment_status = models.CharField(max_length=100, null=True, blank=True)
    unemployed_period = models.CharField(max_length=100, null=True, blank=True)
    home_address = models.CharField(max_length=100, null=True, blank=True)
    postal_address = models.CharField(max_length=100, null=True, blank=True)
    postal_code = models.CharField(max_length=10, null=True, blank=True)
    contract_number = models.CharField(max_length=20, null=True, blank=True)
    contracted_learning_status = models.CharField(max_length=50, null=True, blank=True)
    learner_enrollment_number = models.CharField(max_length=20, null=True, blank=True)
    learning_programe_name = models.CharField(max_length=100, null=True, blank=True)
    subcategory = models.CharField(max_length=100, null=True, blank=True)
    intervention = models.CharField(max_length=100, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    guardian_id_no = models.CharField(max_length=13, null=True, blank=True)
    guardian_full_name = models.CharField(max_length=100, null=True, blank=True)
    guardian_contact = models.CharField(max_length=10, null=True, blank=True)
    province = models.CharField(max_length=50, null=True, blank=True)
    municipality = models.CharField(max_length=50, null=True, blank=True)
    town_or_city = models.CharField(max_length=50, null=True, blank=True)
    urban_or_rural = models.CharField(max_length=50, null=True, blank=True)
    occupation_level = models.CharField(max_length=1000, null=True, blank=True)
    job_title = models.CharField(max_length=50, null=True, blank=True)
    OFO_occupation_code = models.CharField(max_length=50, null=True, blank=True)
    OFO_specialization = models.CharField(max_length=50, null=True, blank=True)
    OFO_occupation = models.CharField(max_length=50, null=True, blank=True)
    highest_school_qualification = models.CharField(max_length=50, null=True, blank=True)
    highest_qualification = models.CharField(max_length=50, null=True, blank=True)
    student_number = models.CharField(max_length=20, null=True, blank=True)
    bursary_awarded_date = models.DateField(null=True, blank=True)
    bursary_completion_status = models.CharField(max_length=50, null=True, blank=True)
    popi_consent = models.CharField(max_length=10, null=True, blank=True)
    popi_consent_date = models.DateField(null=True, blank=True)
    must_change_password = models.BooleanField(default=True)
    temporary_password_expires = models.DateTimeField(null=True, blank=True)
    
    
    objects = CustomUserManager()
    
    def __str__(self):
        return f"{self.email}"
