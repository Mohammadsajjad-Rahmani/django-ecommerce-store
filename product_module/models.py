from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.shortcuts import redirect
from django.views import View
from jalali_date import date2jalali

from account_module.models import User


# Create your models here.

class product_brand(models.Model):
    title = models.CharField(max_length=300, verbose_name='نام برند')
    is_active = models.BooleanField(default=False, verbose_name='فعال / غیرفعال')

    class Meta:
        verbose_name = 'نام برند'
        verbose_name_plural = 'نام برند ها'

    def __str__(self):
        return self.title


class product(models.Model):
    image = models.ImageField(upload_to='images/product-pic', blank=True, null=True, verbose_name='تصویر محصول')
    title = models.CharField(max_length=300, verbose_name='عنوان محصول')
    price = models.IntegerField(verbose_name='قیمت')
    description = models.TextField(verbose_name='توضیحات اصلی', db_index=True)
    short_description = models.CharField(verbose_name='توضیحات کوتاه', db_index=True, max_length=360, null=True)
    slug = models.SlugField(default="", null=False, db_index=True, blank=True, max_length=200, unique=True,
                            verbose_name='عنوان در url')
    is_active = models.BooleanField(default=False, verbose_name='فعال / غیرفعال')
    is_delete = models.BooleanField(verbose_name='حذف شده / حذف نشده')
    brand = models.ForeignKey(product_brand, null=True, blank=True, verbose_name='برند', on_delete=models.CASCADE, )

    # color = models.CharField(verbose_name='رنگ',null=True,blank=True, max_length=300)

    def get_absolute_url(self):
        return reverse('produt-detail', args=[self.slug])
        # return reverse('produt-detail', args=[self.id])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

    def __str__(self):
        return f"{self.title} {self.price}"


class product_category(models.Model):
    title = models.CharField(max_length=300, db_index=True, verbose_name='عنوان')
    url_title = models.CharField(max_length=300, db_index=True, verbose_name='عنوان در url')
    is_active = models.BooleanField(verbose_name='فعال / غیرفعال')
    is_delete = models.BooleanField(verbose_name='حذف شده / حذف نشده')
    category = models.ManyToManyField(product, related_name='product_categories', verbose_name='دسته بندی ها',
                                      blank=True)

    def __str__(self):
        return f"({self.title} - {self.url_title})"

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'


class product_tag(models.Model):
    caption = models.CharField(max_length=300, verbose_name='عنوان')
    products = models.ForeignKey(product, on_delete=models.CASCADE, related_name='products_tag')

    class Meta:
        verbose_name = 'تگ محصول'
        verbose_name_plural = 'تگ محصولات'

    def __str__(self):
        return self.caption


class product_visit(models.Model):
    product = models.ForeignKey(product, on_delete=models.CASCADE, related_name='product_visit')
    # in related name kardan forigen key toye annotate kardan va toye bedast ovardane zir majmoe ha bedard mikhore
    ip_address = models.GenericIPAddressField(max_length=100, verbose_name='آی پی کاربر')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر', blank=True, null=True)

    def __str__(self):
        return f"{self.ip_address} - {self.product}"

    class Meta:
        verbose_name = 'بازدید محصول'
        verbose_name_plural = 'بازدید های محصول'


class product_gallery(models.Model):
    product = models.ForeignKey(product, on_delete=models.CASCADE, verbose_name='محصول')
    image = models.ImageField(upload_to='images/product-pic', verbose_name='تصویر')

    class Meta:
        verbose_name = 'گالری تصویر'
        verbose_name_plural = 'گالری تصاویر'

    def __str__(self):
        return self.product.title


class productcoment(models.Model):
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ')
    text = models.TextField(verbose_name='متن')
    autour = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    purches = models.ForeignKey(product, on_delete=models.CASCADE, verbose_name='محصول')
    is_accepted = models.BooleanField(verbose_name='رد / قبول', null=True)

    class Meta:
        verbose_name = 'نظر محصول'
        verbose_name_plural = 'نظرات محصولات'

    def __str__(self):
        return self.autour.first_name

