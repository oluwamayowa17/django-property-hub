from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core import validators
from django.contrib.auth.models import User
from AppTwo.models import *

class RegistrationForm(UserCreationForm):
    username = forms.CharField(
        label='Username*',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
            }
        )
    )
    email = forms.EmailField(
        label='Email*',
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
            }
        )
    )
    password1 = forms.CharField(
        label='Password*',
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
            }
        )
    )
    password2 = forms.CharField(
        label='Confirm Password*',
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
            }
        )
    )

    first_name = forms.CharField(
        required=False,
        label='Firstname',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
            }
        )
    )

    last_name = forms.CharField(
        required=False,
        label='Lastname',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
            }
        )
    )
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

    class Meta():
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
            return user
        
class AddLocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ('name', 'state')
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'state': forms.TextInput(attrs={'class':'form-control'}),
        }

class AddPropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = '__all__'
        exclude = ('agent', )
        widgets = {
            'location': forms.Select(attrs={'class':'form-control'}),
            'category': forms.Select(attrs={'class':'form-control'}),
            'price': forms.TextInput(attrs={'class':'form-control'}),
            'address': forms.TextInput(attrs={'class':'form-control'}),
            'image1': forms.ClearableFileInput(attrs={'class':'form-control'}),
            'image2': forms.ClearableFileInput(attrs={'class':'form-control'}),
            'image3': forms.ClearableFileInput(attrs={'class':'form-control'}),
            'status':forms.Select(attrs={'class':'form-control'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),
            'num_of_rooms': forms.NumberInput(attrs={'class':'form-control'}),
            'num_of_baths': forms.NumberInput(attrs={'class':'form-control'}),
            'featured': forms.CheckboxInput()
        }

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'
        exclude = ('user', )
        widgets = {
            'profile_picture': forms.ClearableFileInput(attrs={'class':'form-control'}),
            'profession': forms.TextInput(attrs={'class':'form-control'}),
            'about': forms.Textarea(attrs={'class':'form-control'}),
            'instagram': forms.URLInput(attrs={'class':'form-control'}),
            'twitter': forms.URLInput(attrs={'class':'form-control'}),
            'facebook': forms.URLInput(attrs={'class':'form-control'}),
            'linkedin': forms.URLInput(attrs={'class':'form-control'}),
            'your_cv': forms.ClearableFileInput(attrs={'class':'form-control'})
        }

        