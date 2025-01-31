# Generated by Django 5.0.4 on 2024-05-02 18:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='product_brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='نام برند')),
                ('is_active', models.BooleanField(default=False, verbose_name='فعال / غیرفعال')),
            ],
            options={
                'verbose_name': 'نام برند',
                'verbose_name_plural': 'نام برند ها',
            },
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/product-pic', verbose_name='تصویر محصول')),
                ('title', models.CharField(max_length=300, verbose_name='عنوان محصول')),
                ('price', models.IntegerField(verbose_name='قیمت')),
                ('description', models.TextField(db_index=True, verbose_name='توضیحات اصلی')),
                ('short_description', models.CharField(db_index=True, max_length=360, null=True, verbose_name='توضیحات کوتاه')),
                ('slug', models.SlugField(blank=True, default='', max_length=200, unique=True, verbose_name='عنوان در url')),
                ('is_active', models.BooleanField(default=False, verbose_name='فعال / غیرفعال')),
                ('is_delete', models.BooleanField(verbose_name='حذف شده / حذف نشده')),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product_module.product_brand', verbose_name='برند')),
            ],
            options={
                'verbose_name': 'محصول',
                'verbose_name_plural': 'محصولات',
            },
        ),
        migrations.CreateModel(
            name='product_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=300, verbose_name='عنوان')),
                ('url_title', models.CharField(db_index=True, max_length=300, verbose_name='عنوان در url')),
                ('is_active', models.BooleanField(verbose_name='فعال / غیرفعال')),
                ('is_delete', models.BooleanField(verbose_name='حذف شده / حذف نشده')),
                ('category', models.ManyToManyField(blank=True, related_name='product_categories', to='product_module.product', verbose_name='دسته بندی ها')),
            ],
            options={
                'verbose_name': 'دسته بندی',
                'verbose_name_plural': 'دسته بندی ها',
            },
        ),
        migrations.CreateModel(
            name='product_gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/product-pic', verbose_name='تصویر')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_module.product', verbose_name='محصول')),
            ],
            options={
                'verbose_name': 'گالری تصویر',
                'verbose_name_plural': 'گالری تصاویر',
            },
        ),
        migrations.CreateModel(
            name='product_tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=300, verbose_name='عنوان')),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products_tag', to='product_module.product')),
            ],
            options={
                'verbose_name': 'تگ محصول',
                'verbose_name_plural': 'تگ محصولات',
            },
        ),
        migrations.CreateModel(
            name='product_visit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.GenericIPAddressField(verbose_name='آی پی کاربر')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_visit', to='product_module.product')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'بازدید محصول',
                'verbose_name_plural': 'بازدید های محصول',
            },
        ),
        migrations.CreateModel(
            name='productcoment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='text')),
                ('autour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
                ('purches', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_module.product', verbose_name='product')),
            ],
            options={
                'verbose_name': 'comment',
                'verbose_name_plural': 'comments',
            },
        ),
    ]
