from django import forms

from models import ArticleCommentFormModel


class ArticleCommentForm(forms.ModelForm):

    class Meta:
        model = ArticleCommentFormModel
        fields = ['name', 'email_address', 'text']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'نام و نام خانوادگی'
            }),
            'email_address': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'ایمیل',
            }),
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'id': 'message',
                'placeholder': 'متن پیام',
            }),
        }
        labels = {
            'name': 'نام و نام خانوادگی خود را وارد کنید',
            'email_address': 'ایمیل خود را وارد کنید'
        }
        error_messages = {
            'name': {
                'required': 'لطفا نام و نام خانوادگی خود را وارد کنید',
                'max_length': 'نام و نام خانوادگی نباید بیشتر  از 50 کاراکتر باشد',
            },
            'email_address': {
                'required': 'ایمیل الزامیست'
            }
        }