from django import forms
from django.core import validators
from django.core.exceptions import ValidationError


class Register_form(forms.Form):
    # profile = forms.ImageField(
    #     label='انتخاب پروفایل',
    #     widget=forms.FileInput()
    #

    email = forms.EmailField(
        label='ایمیل',
        widget=forms.EmailInput(),
        validators=[
            validators.MaxLengthValidator(100),
            validators.EmailValidator
        ]
    )
    password = forms.CharField(
        label='رمزعبور',
        widget=forms.PasswordInput(),
        validators=[
            validators.MaxLengthValidator(100),
            validators.EmailValidator
        ]
    )
    confirm_password = forms.CharField(
        label='تکرار رمز عبور',
        widget=forms.PasswordInput(),
        validators=[
            validators.MaxLengthValidator(100),
            validators.EmailValidator
        ]
    )

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise ValidationError('طول رمز عبور کمتر از 8 کاراکتر است ')
        else:
            return password

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if 'yahoo' in email:
            raise ValidationError('ایمیل از نوع یاهو معتبر نیست')
        else:
            return email

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password == confirm_password:
            return confirm_password

        raise ValidationError('رمزعبور و تکرار رمز عبور مغایرت دارند')


class Login_form(forms.Form):
    # profile = forms.ImageField(
    #     label='انتخاب پروفایل',
    #     widget=forms.FileInput()
    # )

    email = forms.EmailField(
        label='ایمیل',
        widget=forms.EmailInput(),
        validators=[
            validators.MaxLengthValidator(100),
            validators.EmailValidator
        ]
    )
    password = forms.CharField(
        label='رمزعبور',
        widget=forms.PasswordInput(),
        validators=[
            validators.MaxLengthValidator(100),
        ]
    )
    remember_me = forms.BooleanField(
        required=False
    )



class Forget_form(forms.Form):
    email = forms.EmailField(
        label='ایمیل',
        widget=forms.EmailInput(),
        validators=[
            validators.MaxLengthValidator(100),
            validators.EmailValidator
        ]
    )


class Reset_form(forms.Form):

    password = forms.CharField(
        label='رمزعبور',
        widget=forms.PasswordInput(),
        validators=[
            validators.MaxLengthValidator(100),
            validators.EmailValidator
        ]
    )
    confirm_password = forms.CharField(
        label='تکرار رمز عبور',
        widget=forms.PasswordInput(),
        validators=[
            validators.MaxLengthValidator(100),
            validators.EmailValidator
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
