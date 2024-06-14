from django import forms
 
class PropertySearchForm(forms.Form):
    location = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Location'}))