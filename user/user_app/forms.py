from django import forms
from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm,UserChangeForm
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
import datetime

class CustomUserCreationForm(forms.ModelForm ):
    
    first_name = forms.CharField(
        required=True,
        max_length=100,
        validators=[
            RegexValidator(
                regex=r'^[a-zA-Z]{3,20}$',
                message='First name must contain alphabets and be between 3 and 20 characters long.',
                code='invalid_first_name'
            ),
        ],
        widget=forms.TextInput(attrs={'placeholder': 'First Name', 'class': 'form-control'})
    )
    
    last_name = forms.CharField(
        required=True,
        max_length=100,
        validators=[
            RegexValidator(
                regex=r'^[a-zA-Z]{3,20}$',
                message='Last name must contain alphabets and be between 3 and 20 characters long.',
                code='invalid_last_name'
            ),
        ],
        widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'class': 'form-control'})
    )
    
    email = forms.EmailField(
        required=True,
        max_length=100,
        validators=[
            RegexValidator(
                regex=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
                message='Please enter a valid email address.',
                code='invalid_email'
            ),
        ],
        widget=forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control'})
    )
    
    contact_number = forms.CharField(
        required=True,
        max_length=10,
        validators=[
            RegexValidator(
                regex=r'^(?:\+?27|0)(\d{9})$',
                message='Please enter a valid South African phone number starting with the area code.',
                code='invalid_phone_number'
            ),
        ],
        widget=forms.TextInput(attrs={'placeholder': 'Contact Number', 'class': 'form-control'})
    )
    
    birth_date = forms.DateField(
        required=True,
        input_formats=['%Y-%m-%d'],
        widget=forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD', 'class': 'form-control datepicker'}),
        help_text='Enter your birth date in the format YYYY-MM-DD.',
    )
    
    def clean_birth_date(self):
        birth_date = self.cleaned_data.get('birth_date')
        if birth_date:
            
            if birth_date > timezone.now().date():
                raise ValidationError("Birth date cannot be in the future.")
        return birth_date
    
    id_or_passport = forms.CharField(
        required=True,
        max_length=13,
        validators=[
            RegexValidator(
                regex=r'^\d{13}$',
                message='Enter a valid 13-digit ID number.',
                code='invalid_id_number'
            ),
        ],
        widget=forms.TextInput(attrs={'placeholder': 'ID Number', 'class': 'form-control'})
    )
    
    id_type = forms.ChoiceField(choices=[('select', 'Select'), ('national id', 'National ID'), ('passport', 'Passport')], required=True,
                                widget=forms.Select(attrs={'placeholder': 'ID Type',
                                    'class': 'form-control'}))
                                

    age = forms.IntegerField(required=True,
                                widget=forms.NumberInput(attrs={'placeholder': 'Age',
                                                            'class': 'form-control'}))
    
    title = forms.ChoiceField(choices=[('select', 'Select'), ('mr', 'Mr'), ('mrs', 'Mrs'), ('miss','Miss'), ('dr', 'Dr'), ('prof', 'Prof'), ('rev', 'Rev')], required=True,
                                widget=forms.Select(attrs={'class': 'form-control'}))
        
    youth = forms.CharField(required=True, max_length=3,
                                widget=forms.TextInput(attrs={'placeholder': 'Youth',
                                                            'class': 'form-control'}))
    
    gender = forms.ChoiceField(choices=[('select', 'Select'), ('male', 'Male'),('female', 'Female'), ('choose', 'Choose Not To Identify')], required=True,
                                widget=forms.Select(attrs={'class': 'form-control'}))
    
    race = forms.ChoiceField(choices=[('select', 'Select'), ('african', 'African'), ('coloured', 'Coloured'), ('indian', 'Indian'), ('white', 'White')], required=True,
                                widget=forms.Select(attrs={'class': 'form-control'}))
    
    disability = forms.ChoiceField(choices=[('select', 'Select'), ('none', 'None'), ('sight', 'Sight (even with glasses)'), ('hearing', 'Hearing (even with h. aid)'), ('speech', 'Speech'), ('physical', 'Physical'), ('mental', 'Mental'), ('other', 'Other')], 
                                   required=True, widget=forms.Select(attrs={'class': 'form-control'}))
    
    home_language = forms.ChoiceField(choices=[('select', 'Select') ,('afrikaans', 'Afrikaans'), ('english', 'English'), ('isindebele',  'IsiNdebele'), ('isixhosa', 'IsiXhosa'), ('isizulu', 'IsiZulu'), ('sepedi', 'Sepedi'), ('sesotho', 'Sesotho'), ('setswana', 'Setswana'), ('siswati', 'SiSwati'), ('tshivenda', 'Tshivenda'), ('xitsonga', 'Xitsonga')], required=True,
                                widget=forms.Select(attrs={'class': 'form-control'}))
    
    citezenship = forms.ChoiceField(choices=[('select', 'Select') ,('south africa', 'South Africa'), ('other', 'Other')], required=True,
                                widget=forms.Select(attrs={'class': 'form-control'}))
    
    nationality = forms.ChoiceField(choices=[('select', 'Select'),('afghanistan', 'Afghanistan'), ('albania', 'Albania'), ('algeria', 'Algeria')] ,required=True,
                                widget=forms.Select(attrs={'class': 'form-control'}))
    
    employment_status = forms.ChoiceField(choices=[('select', 'Select'), ('employed-permanent', 'Employed-Permanent'), ('employed-temporary', 'Employed-Temporary'), ('employed-contractor', 'Employed-Contractor'), ('unemployed', 'Unemployed')], required=True,
                                widget=forms.Select(attrs={'class': 'form-control'}))
    
    unemployed_period = forms.ChoiceField(choices=[('choose_period', "Choose Period"), ('0 - 1 year', '0 - 1 Year'), ('1 - 5 year', '1 - 5 Year'), ('5 - 10 year', '5 - 10 Year'), ('10+ year', '10+ Year')], required=True,
                                widget=forms.Select(attrs={'class': 'form-control'}))
    
    address_pattern = r'^[a-zA-Z0-9\s,.-]+$'
    home_address = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Home Address', 'class': 'form-control'}),
        help_text='Enter your home address.',
        validators=[RegexValidator(
            regex=address_pattern,
            message='Please enter a valid address.',
            code='invalid_address'
        )]
    )

    postal_address = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Postal Address', 'class': 'form-control'}),
        help_text='Enter your postal address.',
        validators=[RegexValidator(
            regex=address_pattern,
            message='Please enter a valid address.',
            code='invalid_address'
        )]
    )
    
    postal_code_pattern = r'^\d{4,5}$'

    postal_code = forms.CharField(
        max_length=5,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Postal Code', 'class': 'form-control'}),
        help_text='Enter your postal code.',
        validators=[RegexValidator(
            regex=postal_code_pattern,
            message='Please enter a valid postal code (4 or 5 digits).',
            code='invalid_postal_code'
        )]
    )
    
    contract_number = forms.CharField(required=False, max_length=100,
                                widget=forms.TextInput(attrs={'placeholder': 'Contract Number',
                                                            'class': 'form-control'}))
    
    contracted_learning_status = forms.CharField(required=False ,max_length=100,
                                                 widget=forms.TextInput(attrs={'placeholder': 'Contracted Learning Status',
                                                            'class': 'form-control'}))
    
    learner_enrollment_number = forms.CharField(required=False, max_length=100,
                                                  widget=forms.TextInput(attrs={'placeholder': 'Learner Enrollment Number',
                                                                'class': 'form-control'}))
    
    learning_programe_name = forms.CharField(required=False, max_length=100,
                                                widget=forms.TextInput(attrs={'placeholder': 'Learning Programe Name',
                                                                'class': 'form-control'}))
    subcategory = forms.CharField(required=False, max_length=100,
                                    widget=forms.TextInput(attrs={'placeholder': 'Subcategory',
                                                                'class': 'form-control'}))
    intervention = forms.CharField(required=False, max_length=100,
                                   widget=forms.TextInput(attrs={'placeholder': 'Intervention',
                                                                'class': 'form-control'}))
    
    date_pattern = r'^\d{4}-\d{2}-\d{2}$'

    start_date = forms.DateField(required=True,
        widget=forms.DateInput(attrs={'placeholder': 'Start Date', 'class': 'form-control datepicker'})
    )

    end_date = forms.DateField(
        widget=forms.DateInput(attrs={'placeholder': 'End Date', 'class': 'form-control datepicker'})
    )
    
    id_number_pattern = r'^\d{13}$'

    guardian_id_no = forms.CharField(
        max_length=13,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Guardian ID Number', 'class': 'form-control'}),
        help_text='Enter the guardian ID number (13 digits).',
        validators=[RegexValidator(
            regex=id_number_pattern,
            message='Please enter a valid 13-digit ID number.',
            code='invalid_id_number_format'
        )]
    )
    
    full_name_pattern = r'^[A-Za-z\s]{3,50}$'

    guardian_full_name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Guardian Full Name', 'class': 'form-control'}),
        help_text='Enter the guardian\'s full name (3-50 characters, alphabets and spaces only).',
        validators=[RegexValidator(
            regex=full_name_pattern,
            message='Please enter a valid full name (3-50 characters, alphabets and spaces only).',
            code='invalid_full_name_format'
        )]
    )
    
    contact_number_pattern = r'^\d{10}$'

    guardian_contact = forms.CharField(
        max_length=10,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Guardian Contact', 'class': 'form-control'}),
        help_text='Enter the guardian\'s contact number (10 digits).',
        validators=[RegexValidator(
            regex=contact_number_pattern,
            message='Please enter a valid 10-digit contact number.',
            code='invalid_contact_number_format'
        )]
    )
    
    province = forms.ChoiceField(choices=[('select', 'Select'), ('eastern_cape', 'Eastern Cape'), ('free_state', 'Free State'), ('gauteng', 'Gauteng'), ('kwazulu_natal', 'KwaZulu Natal'), ('limpopo', 'Limpopo'), ('mpumalanga', 'Mpumalanga'), ('northern_cape', 'Northen Cape'), ('north_west', 'Noth West'), ('western_cape', 'Western Cape')], required=True,
                                widget=forms.Select(attrs={'class': 'form-control'}))
    
    municipality = forms.ChoiceField(choices=[('select', 'Select'), ('Dr Kenneth Kaunda District Municipality-DC40', 'Dr Kenneth Kaunda District Municipality-DC40'), ('City of Matlosana Local Municipality-NW403', 'City of Matlosana Local Municipality-NW403'), ('Ditsobotla Local Municipality-NW384', 'Ditsobotla Local Municipality-NW384')], required=True,
                                widget=forms.Select(attrs={'class': 'form-control'}))
                                                            
    town_or_city_pattern = r'^[a-zA-Z\s]+$'

    town_or_city = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Town/City', 'class': 'form-control'}),
        help_text='Enter the town or city name (alphabets and spaces only).',
        validators=[RegexValidator(
            regex=town_or_city_pattern,
            message='Please enter a valid town or city name (alphabets and spaces only).',
            code='invalid_town_or_city_format'
        )]
    )
    
    urban_or_rural = forms.ChoiceField(choices=[('select', 'Select'), ('urban', 'Urban'), ('rural', 'Rural')], required=True,
                                widget=forms.Select(attrs={'class': 'form-control'}))
                                                            
    occupation_level = forms.ChoiceField(choices=[('select', 'Select'), ('Top management', 'Top management'), ('Senior management', 'Senior management'), ('Professionally qualified and experienced specialists and mid-management', 'Professionally qualified and experienced specialists and mid-management'), 
                                                  ('Skilled technical and academically qualified workers, junior management, supervisors, foremen and superintendents', 'Skilled technical and academically qualified workers, junior management, supervisors, foremen and superintendents'), ('Semi-skilled and discretionary decision makers', 'Semi-skilled and discretionary decision makers'), ('Unskilled and defined decision makers', 'Unskilled and defined decision makers')], required=True,
                                widget=forms.Select(attrs={'placeholder': 'Occupation Level',
                                                            'class': 'form-control'}))
    
    job_title = forms.CharField(max_length=100, required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'Job Title',
                                                            'class': 'form-control'}))
    
    OFO_occupation_code = forms.CharField(max_length=10, required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'Occupation Code',
                                                            'class': 'form-control'}))
    
    OFO_specialization = forms.CharField(max_length=100, required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'Specialization',
                                                            'class': 'form-control'}))
    
    OFO_occupation = forms.CharField(max_length=100, required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'Occupation',
                                                            'class': 'form-control'}))
    
    highest_school_qualification = forms.ChoiceField(choices=[('select', 'Select'), ('gr1', 'Grade 1'), ('gr2', 'Grade 2'), ('gr3', 'Grade 3'), ('gr4', 'Grade 4'), ('gr5', 'Grade 5'), ('gr6', 'Grade 6'), ('gr7', 'Grade 7'), ('gr8', 'Grade 8'), ('gr9', 'Grade 9'), ('gr10', 'Grade 10'), ('gr11', 'Grade 11'), ('gr12', 'Grade 12')], required=True,
                                widget=forms.Select(attrs={'placeholder': 'Highest School Qualification',
                                                            'class': 'form-control'}))
    
    highest_qualification = forms.ChoiceField(choices=[('select', 'Select'), ('National Certificate', 'National Certificate'), ('National Diploma', 'National Diploma'), ('National First Degree', 'National First Degree'), ('Post-doctoral Degree', 'Post-doctoral Degree'), ('Doctoral Degree', 'Doctoral Degree'), ('Masters Degree', 'Masters Degree'), ('Professional Qualification', 'Professional Qualification'), ('Honours Degree', 'Honours Degree'), ('National Higher Diploma', 'National Higher Diploma'), ('National Masters Diploma', 'National Masters Diploma'), ('National Higher Certificate', 'National Higher Certificate'), ('Further Diploma', 'Further Diploma')], required=True,
                                widget=forms.Select(attrs={'placeholder': 'Highest Qualification',
                                                            'class': 'form-control'}))
    
    student_number_pattern = r'^\d{9}$'
    
    student_number = forms.CharField(
        max_length=9,
        min_length=9,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Student Number', 'class': 'form-control'}),
        help_text='Enter a student number with exactly 9 digits.',
        validators=[RegexValidator(
            regex=student_number_pattern,
            message='Please enter a valid student number with exactly 9 digits.',
            code='invalid_student_number_format'
        )]
    )
    
    bursary_awarded_date = forms.DateField(required=False,
                                           widget=forms.DateInput(attrs={'placeholder': 'Bursary Awarded Date',
                                                            'class': 'form-control datepicker'}))
    
    bursary_completion_status = forms.ChoiceField(choices=[('select', 'Select'), ('First Year', 'First Year'), ('Second Year', 'Second Year'), ('Third Year', 'Third Year'), ('Fourth Year', 'Fourth Year')], required=True,
                                                widget=forms.Select(attrs={'placeholder': 'Bursary Completion Status',
                                                            'class': 'form-control'}))
    
    popi_consent = forms.ChoiceField(required=True, choices=[('select', 'Select'), ('agree', 'Agree'), ('disagree', 'Disagree')],
                                     widget=forms.Select(attrs={'class': 'form-control'}))
    
    popi_consent_date = forms.DateField(required=True,
                                widget=forms.DateInput(attrs={'placeholder': 'POPI Consent Date',
                                                            'class': 'form-control datepicker'}))
    
    class Meta:
        model = CustomUser
        fields = ('email','first_name', 'last_name', 'contact_number', 'birth_date', 'id_type', 'id_or_passport', 'age', 'title', 'youth', 'gender',
                  'race', 'disability', 'home_language', 'citezenship', 'nationality', 'employment_status', 'unemployed_period', 'home_address', 'postal_address',
                  'postal_code', 'contract_number', 'contracted_learning_status', 'learner_enrollment_number', 'learning_programe_name', 'subcategory', 'intervention',
                  'start_date', 'end_date', 'guardian_id_no', 'guardian_full_name', 'guardian_contact', 'province', 'municipality', 'town_or_city', 'urban_or_rural',
                  'occupation_level', 'job_title', 'OFO_occupation_code', 'OFO_specialization', 'OFO_occupation', 'highest_school_qualification', 'highest_qualification',
                  'student_number', 'bursary_awarded_date', 'bursary_completion_status', 'popi_consent', 'popi_consent_date')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(self.data)  # Print form data to debug
        

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("email",)
        
class Login(AuthenticationForm):
    email = forms.EmailField(max_length=100, required=True,
                                widget=forms.EmailInput(attrs={'placeholder': 'Email',
                                                            'class': 'form-control'}))
    password = forms.CharField(max_length=100, required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  'name': 'password',
                                                                  }))
    remember_me = forms.BooleanField(required=False)
    
    class Meta:
        model = CustomUser
        fields = ['email', 'password', 'remember_me']
    
                                              
    
    
    
    