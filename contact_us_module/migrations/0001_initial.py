# Generated by Django 5.0.4 on 2024-05-02 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact_us_models',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='عنوان')),
                ('email', models.EmailField(max_length=300, verbose_name='ایمیل')),
                ('full_name', models.CharField(max_length=50, verbose_name='نام و نام خانوادگی')),
                ('message', models.TextField(verbose_name='متن تماس با ما')),
                ('response', models.TextField(verbose_name='پاسخ ادمین')),
                ('is_read_by_admin', models.BooleanField(default=False, verbose_name='خوانده شده توسط ادمین')),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='تاریخ ایچاد')),
            ],
            options={
                'verbose_name': 'تماس با ما',
                'verbose_name_plural': 'لیست تماس با ما',
            },
        ),
        migrations.CreateModel(
            name='user_profile_data_base',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
    ]
