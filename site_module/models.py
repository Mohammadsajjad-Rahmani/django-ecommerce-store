from django.db import models


# Create your models here.

class site_setting(models.Model):
    email = models.CharField(max_length=200, verbose_name='ایمیل', null=True, blank=True)
    address = models.CharField(max_length=200, verbose_name='آدرس', null=True, blank=True)
    fax = models.CharField(max_length=200, verbose_name='فکس', null=True, blank=True)
    phone_number = models.CharField(max_length=200, verbose_name='تلفن')
    logo = models.ImageField(upload_to='images/site_setting', verbose_name='تصویر لوگو')
    domain = models.CharField(max_length=200, verbose_name='دامنه')
    name = models.CharField(max_length=200, verbose_name='نام')
    copy_right = models.TextField(verbose_name='متن کپی رایت سایت')
    about_us = models.TextField(verbose_name='متن درباره سایت')
    is_main_setting = models.BooleanField(verbose_name='تنظیمات اصلی')
    url_logo = models.URLField(max_length=500, verbose_name='آدرس لوگو', null=True)

    class Meta:
        verbose_name = 'تظیمات سایت'
        verbose_name_plural = 'تنظیمات'

    def __str__(self):
        return self.name


class footer_links_title(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان دسته بندی')

    class Meta:
        verbose_name = 'عنوان دسته بندی'
        verbose_name_plural = 'عنوان دسته بندی ها'

    def __str__(self):
        return self.title


class footer_link(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان لینک')
    url = models.URLField(max_length=500, verbose_name='آدرس url')
    footer_link_box = models.ForeignKey(footer_links_title, on_delete=models.CASCADE, verbose_name='جدول دسته بندی',
                                        related_name='footer_link')

    class Meta:
        verbose_name = 'عنوان url'
        verbose_name_plural = 'عناوین url'

    def __str__(self):
        return f"{self.title} {self.url}"


class Slider(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان اصلی')
    sub_title = models.CharField(max_length=200, verbose_name='عنوان')
    description = models.TextField(verbose_name='توضیحات')
    Image = models.ImageField(upload_to='images/sliders', verbose_name='تصویر اسلاید')
    url_button = models.CharField(max_length=200, verbose_name='عنوان دکمه')
    url = models.URLField(max_length=500, verbose_name='آدرس دکمه')
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیرفعال')

    class Meta:
        verbose_name = 'اسلایدر'
        verbose_name_plural = 'اسلایدها'

    def __str__(self):
        return self.title


# site_banner_positions = [
#     ('position_list', 'صحفه لیست محصولات '),
#     ('product_detail , حزئیات محصولات')
#
#     # in ravesh toye tedad bala baes mishe be moshkel bokhorim baraye hamin az sub class text choices estefade mikonim
# ]


class SiteBanner(models.Model):
    class SiteBannerPosition(models.TextChoices):
        # avali to database save mishe va dovomi dovomi be user neshon dade mishe
        product_list = 'product_list', 'لیست محصولات'
        product_detail = 'product_detail', 'جرئیات محصولات'
        about_us = 'about_us', 'درباره ما'

    title = models.CharField(max_length=200, verbose_name='عنوان بنر')
    url_title = models.URLField(max_length=400, verbose_name='آدرس الکترونیک بنر')
    image = models.ImageField(upload_to='images/site_banner')
    is_active = models.BooleanField(verbose_name='فعال / غیر فعال')
    # position = models.CharField(max_length=200,choices=site_banner_positions , verbose_name='جایگاه عکس')
    position = models.CharField(max_length=200, choices=SiteBannerPosition.choices, verbose_name='جایگاه عکس')

    class Meta:
        verbose_name = 'بنر تبلیغاتی'
        verbose_name_plural = 'بنرهای تبلیغاتی'

    def __str__(self):
        return self.title
