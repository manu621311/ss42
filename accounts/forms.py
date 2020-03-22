from  django import forms
from . models import  signupModel
from django.contrib.auth.models import User
from django.core.validators import validate_email

class SignForm(forms.ModelForm):
    username = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=30)
    password = forms.PasswordInput()
    password2 = forms.PasswordInput()

    class Meta():
        model = signupModel
        fields = ['username','email','password','password2']


    def clean_username(self):
        user = self.cleaned_data['username']
        try:
            match = signupModel.objects.get(username=user)
        except:
            return self.cleaned_data['username']
        raise forms.ValidationError('username already exist')

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            ema = validate_email(email)
        except:
            return forms.ValidationError('Email is not correct')
        return email
    def clean_password2(self):
        pas = self.cleaned_data['password']
        cpas = self.cleaned_data['password2']
        MIn_LENGTH = 8
        if pas and cpas:
            if pas != cpas:
                raise forms.ValidationError('password and conforimpassword is not matched')
            else:
                if len(pas) < MIn_LENGTH:
                    raise forms.ValidationError('password should have atleast %d character' %MIn_LENGTH)
                if pas.isdigit():
                    raise forms.ValidationError('password should not all numeric')
