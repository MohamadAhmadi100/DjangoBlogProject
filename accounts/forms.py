from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class UserLoginForm(forms.Form):
    username = forms.CharField(label='نام کاربری یا آدرس ایمیل', max_length=30,
                               widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='رمز عبور', max_length=30,
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class UserRegistrationForm(forms.Form):
    username = forms.CharField(label='نام کاربری', max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='پست الکترونیک', max_length=50,
                             widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='رمز عبور', max_length=30,
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='تکرار رمز عبور', max_length=30,
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean_email(self):
        email = self.cleaned_data['email']
        user = User.objects.filter(email=email)
        if user.exists():
            raise ValidationError('حساب کاربری با ایمیل وارد شده موجود است')
        return email

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if password1 and password2:
            if password1 != password2:
                raise ValidationError('کلمات عبور مطابقت ندارند')
