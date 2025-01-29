from django.db import models
from django import forms


# Create your models here.


class contact_us_models(models.Model):
    title = models.CharField(max_length=300, verbose_name='عنوان')
    email = models.EmailField(max_length=300, verbose_name='ایمیل')
    full_name = models.CharField(max_length=50, verbose_name='نام و نام خانوادگی')
    message = models.TextField(verbose_name='متن تماس با ما')
    response = models.TextField(verbose_name='پاسخ ادمین')
    is_read_by_admin = models.BooleanField(verbose_name='خوانده شده توسط ادمین', default=False)
    created_date = models.DateTimeField(verbose_name='تاریخ ایچاد', null=True, blank=True, auto_now_add=True)

    # auto_now_add khodesh khodkar time mide

    class Meta:
        verbose_name = 'تماس با ما'
        verbose_name_plural = 'لیست تماس با ما'

    def __str__(self):
        return self.title


class user_profile_data_base(models.Model):
    image = models.ImageField(upload_to='images')
