# Generated by Django 5.0.4 on 2024-05-02 18:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='footer_links_title',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان دسته بندی')),
            ],
            options={
                'verbose_name': 'عنوان دسته بندی',
                'verbose_name_plural': 'عنوان دسته بندی ها',
            },
        ),
        migrations.CreateModel(
            name='site_setting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(blank=True, max_length=200, null=True, verbose_name='ایمیل')),
                ('address', models.CharField(blank=True, max_length=200, null=True, verbose_name='آدرس')),
                ('fax', models.CharField(blank=True, max_length=200, null=True, verbose_name='فکس')),
                ('phone_number', models.CharField(max_length=200, verbose_name='تلفن')),
                ('logo', models.ImageField(upload_to='images/site_setting', verbose_name='تصویر لوگو')),
                ('domain', models.CharField(max_length=200, verbose_name='دامنه')),
                ('name', models.CharField(max_length=200, verbose_name='نام')),
                ('copy_right', models.TextField(verbose_name='متن کپی رایت سایت')),
                ('about_us', models.TextField(verbose_name='متن درباره سایت')),
                ('is_main_setting', models.BooleanField(verbose_name='تنظیمات اصلی')),
                ('url_logo', models.URLField(max_length=500, null=True, verbose_name='آدرس لوگو')),
            ],
            options={
                'verbose_name': 'تظیمات سایت',
                'verbose_name_plural': 'تنظیمات',
            },
        ),
        migrations.CreateModel(
            name='SiteBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان بنر')),
                ('url_title', models.URLField(max_length=400, verbose_name='آدرس الکترونیک بنر')),
                ('image', models.ImageField(upload_to='images/site_banner')),
                ('is_active', models.BooleanField(verbose_name='فعال / غیر فعال')),
                ('position', models.CharField(choices=[('product_list', 'لیست محصولات'), ('product_detail', 'جرئیات محصولات'), ('about_us', 'درباره ما')], max_length=200, verbose_name='جایگاه عکس')),
            ],
            options={
                'verbose_name': 'بنر تبلیغاتی',
                'verbose_name_plural': 'بنرهای تبلیغاتی',
            },
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان اصلی')),
                ('sub_title', models.CharField(max_length=200, verbose_name='عنوان')),
                ('description', models.TextField(verbose_name='توضیحات')),
                ('Image', models.ImageField(upload_to='images/sliders', verbose_name='تصویر اسلاید')),
                ('url_button', models.CharField(max_length=200, verbose_name='عنوان دکمه')),
                ('url', models.URLField(max_length=500, verbose_name='آدرس دکمه')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال / غیرفعال')),
            ],
            options={
                'verbose_name': 'اسلایدر',
                'verbose_name_plural': 'اسلایدها',
            },
        ),
        migrations.CreateModel(
            name='footer_link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان لینک')),
                ('url', models.URLField(max_length=500, verbose_name='آدرس url')),
                ('footer_link_box', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='footer_link', to='site_module.footer_links_title', verbose_name='جدول دسته بندی')),
            ],
            options={
                'verbose_name': 'عنوان url',
                'verbose_name_plural': 'عناوین url',
            },
        ),
    ]
