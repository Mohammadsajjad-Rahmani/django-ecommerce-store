from django import forms
from jalali_date import widgets

from account_module.models import User
from django.core import validators
from django.core.exceptions import ValidationError


class EditUserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'avatar', 'address', 'about_user']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'نام '
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': ' نام خانوادگی'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'ایمیل',
            }),
            'address': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'آدرس',
            }),
            'about_user': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3
            }),
            'avatar': forms.FileInput(attrs={
                'class': 'form-control'
            })
        }
        labels = {
            'first_name': 'نام خود را وارد کنید',
            'last_name': ' نام خانوادگی خود را وارد کنید',
            'email': 'ایمیل خود را وارد کنید'
        }
        error_messages = {
            'first_name': {
                'required': 'لطفا نام و نام خانوادگی خود را وارد کنید',
                'max_length': 'نام و نام خانوادگی نباید بیشتر  از 50 کاراکتر باشد',
            },
            'last_name': {
                'required': 'لطفا نام و نام خانوادگی خود را وارد کنید',
                'max_length': 'نام و نام خانوادگی نباید بیشتر  از 50 کاراکتر باشد',
            },
            'email': {
                'required': 'ایمیل الزامیست'
            }
        }


class ChangePasswordForm(forms.Form):
    current_password = forms.CharField(
        label='رمز عبور فعلی',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control'
            }
        ),
        validators=[
            validators.MaxLengthValidator(100),
        ]
    )
    password = forms.CharField(
        label='رمزعبور',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control'
            }
        ),
        validators=[
            validators.MaxLengthValidator(100),
        ]
    )
    confirm_password = forms.CharField(
        label='تکرار رمز عبور',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control'
            }
        ),
        validators=[
            validators.MaxLengthValidator(100),
        ]
    )

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise ValidationError('طول رمز عبور کمتر از 8 کاراکتر است ')
        else:
            return password

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password == confirm_password:
            return confirm_password

        raise ValidationError('رمزعبور و تکرار رمز عبور مغایرت دارند')
