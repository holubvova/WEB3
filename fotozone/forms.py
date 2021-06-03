from django import forms

from .models import User
GENDER=[('man','Man'),('woman','Woman')]

class Sign_in(forms.Form):

    # class Meta:
    #     model =User
    #     fields = ['user_email','user_password']
    #
    #     widgets ={
    #         'user_email': forms.EmailInput(attrs={
    #             'class': 'form-control',
    #             'placeholder': 'Email'
    #         }),
    #         'user_password':
    #               forms.PasswordInput(attrs={
    #                   'class': 'form-control'
    #         })
    #     }
    #



    Email_sign = forms.EmailField(label='Input email', max_length=25,widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    Password = forms.CharField(label='Password', max_length=25,
                                   widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class Register(forms.Form):

    Name = forms.CharField(label='Name', max_length=25 ,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}))
    Email = forms.EmailField(label='Input email', max_length=45,
                             widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email...'}))
    Password = forms.CharField(label='Password', max_length=25,
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    R_Password = forms.CharField(label='Password', max_length=25,
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    gender=forms.CharField(widget=forms.RadioSelect(choices=GENDER, attrs={'value' : 'man'}))

    birthday = forms.DateField(label='Input date of birth(dd.mm.yyyy):',widget=forms.DateInput(attrs={'class':'form-control'}))

class Forgot_password(forms.Form):
    Email = forms.EmailField(label='Input email',max_length=45,  widget=forms.EmailInput(attrs={'class': 'form-control','placeholder': 'Email...' }))
    New_password = forms.CharField(label='New password', max_length=25,widget=forms.PasswordInput(attrs={'class': 'form-control' }))
    R_New_password = forms.CharField(label='Repeat new password',max_length=25, widget=forms.PasswordInput(attrs={'class': 'form-control' }))


class Edit(forms.Form):

    Name = forms.CharField(label='Name', max_length=25 ,
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}))
    SurName = forms.CharField(label='SurName', max_length=25,
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'SurName'}))
    Email = forms.EmailField(label='Input email', max_length=45,
                             widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email...'}))

    gender=forms.CharField(widget=forms.RadioSelect(choices=GENDER, attrs={'value' : 'man'}))

    birthday = forms.DateField(label='Input date of birth(dd.mm.yyyy):',widget=forms.DateInput(attrs={'class':'form-control'}))

    booking = forms.DateField(label='Input booking date  (dd.mm.yyyy):',
                               widget=forms.DateInput(attrs={'class': 'form-control'}))

    Number = forms.IntegerField(label="Number",widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '3800000000'}))