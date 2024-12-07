# tenentapp/forms.py
from django import forms
from .models import TenentProfile

class TenentProfileForm(forms.ModelForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-input','placeholder': 'Enter your email'}))
    phone_number = forms.CharField(required=True,widget=forms.TextInput(attrs={'class': 'form-input','placeholder': 'Enter your phone number'}))
    address = forms.CharField(required=True,widget=forms.Textarea(attrs={'class': 'form-input','placeholder': 'Enter your address','rows': 3}))
    profile_image = forms.ImageField(required=False,widget=forms.FileInput(attrs={'class': 'form-input-file','accept': 'image/*'}))

    class Meta:
        model = TenentProfile
        fields = ['profile_image','email','phone_number', 'address']

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if not phone_number:
            raise forms.ValidationError("Phone number is required.")
        if not phone_number.isdigit():
            raise forms.ValidationError("Phone number should only contain digits.")
        if len(phone_number) < 10:
            raise forms.ValidationError("Phone number should be at least 10 digits.")
        return phone_number

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError("Email is required.")
        return email

    def clean_address(self):
        address = self.cleaned_data.get('address')
        if not address:
            raise forms.ValidationError("Address is required.")
        return address
