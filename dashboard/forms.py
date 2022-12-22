from django import forms
from dashboard.models import Driver,User

GENDER_CHOICES = (
    ("MALE", "MALE"),
    ("FEMALE", "FEMALE"),
    ("OTHER","OTHER"),
    )


class UserForms(forms.ModelForm):
    name = forms.CharField(max_length=100, 
        widget = forms.TextInput(attrs={'type': 'text', 'class': 'form-control'})
    )
    gender = forms.ChoiceField(choices=GENDER_CHOICES, 
        
    )
    date_of_birth = forms.DateField( 
        widget = forms.DateInput(attrs={'type': 'text', 'class': 'form-control'})
    )
    phone_number= forms.IntegerField( 
        widget = forms.NumberInput(attrs={'type': 'text', 'class': 'form-control'})
    )
    user_image= forms.ImageField( 
        widget = forms.FileInput(attrs={'type': 'image', 'class': 'form-control'})
    )
    home_address = forms.CharField( max_length=100, 
        widget = forms.TextInput(attrs={'type': 'text', 'class': 'form-control'})
    )


    class Meta:
        model = User
        fields =  ['name','date_of_birth','gender','phone_number','user_image','home_address']

class DriverForms(forms.ModelForm):
    name       = forms.CharField(max_length=100, 
        widget = forms.TextInput(attrs={'type': 'text', 'class': 'form-control'})
    )
    gender = forms.ChoiceField(choices=GENDER_CHOICES, 
        
    )
    date_of_birth = forms.DateField( 
        widget = forms.DateInput(attrs={'type': 'text', 'class': 'form-control'})
    )
    phone_number= forms.IntegerField( 
        widget = forms.NumberInput(attrs={'type': 'text', 'class': 'form-control'})
    )
    vehicle_no = forms.CharField( max_length=100, 
        widget = forms.TextInput(attrs={'type': 'text', 'class': 'form-control'})
    )
    vehicle_name = forms.CharField( max_length=100, 
        widget = forms.TextInput(attrs={'type': 'text', 'class': 'form-control'})
    )
    license_no = forms.CharField( max_length=100, 
        widget = forms.TextInput(attrs={'type': 'text', 'class': 'form-control'})
    )
    insurance_no = forms.CharField( max_length=100, 
        widget = forms.TextInput(attrs={'type': 'text', 'class': 'form-control'})
    )
    class Meta:
        model = Driver
        fields =  ['name','date_of_birth','gender','phone_number','vehicle_no','vehicle_name','license_no','insurance_no']
