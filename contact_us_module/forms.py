from turtle import width
from django import forms
from django.db.migrations.state import _get_app_label_and_model_name
from .models import contact_us_models


# class contact_us(forms.Form):
#     # required = False ba estefade az in hata error message ham neshon dade nmishe
#     full_name = forms.CharField(label='نام و نام خانوادگی', max_length=50,
#                                 error_messages={
#                                     'required': 'لطفا نام و نام خانوادگی خود را وارد کنید',
#                                     'max_length': 'نام و نام خانوادگی نباید بیشتر  از 50 کاراکتر باشد'
#                                 },
#                                 widget=forms.TextInput(attrs={
#                                     'class': 'form-control',
#
#                                 }))
#     email = forms.EmailField(label='ایمیل', widget=forms.EmailInput(attrs={
#         'class': 'form-control',
#         'placeholder': 'ایمیل'
#     }))
#     title = forms.CharField(label='عنوان',
#                             widget=forms.TextInput(attrs={
#                                 'class': 'form-control',
#                                 'placeholder': 'عنوان'
#                             }))
#     message = forms.CharField(label='متن پیام', widget=forms.Textarea(attrs={
#         'class': 'form-control',
#
#         'id': 'message'
#     }))
#

# by default text area nadarim bayad hamintori azash estefade koni


class new_model_contact_us(forms.ModelForm):
    # sakhtan in model form in qabeliato behet mide ke hamon chizyii ke to data base dorost kardi ro be in fotmi ke dorost kardi vasl mikoni va az hamon mavared data baset toye front endet estefade mikoni
    class Meta:
        model = contact_us_models
        fields = ['full_name', 'email', 'title', 'message']  # onayii ke mikhay neshon mide
        # fields = '__all__' hamaro miare namayesh mide
        # exclude = ['' kodomaro nmikhay neshon bede]
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'نام و نام خانوادگی'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'ایمیل',
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'id': 'message',
                'placeholder': 'متن پیام',
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'عنوان'
            })
        }
        labels = {
            'full_name': 'نام و نام خانوادگی خود را وارد کنید',
            'email': 'ایمیل خود را وارد کنید'
        }
        error_messages = {
            'full_name': {
                'required': 'لطفا نام و نام خانوادگی خود را وارد کنید',
                'max_length': 'نام و نام خانوادگی نباید بیشتر  از 50 کاراکتر باشد',
            },
            'email': {
                'required': 'ایمیل الزامیست'
            }
        }



# class profile_form(forms.Form):
#     user_image = forms.ImageField()