from django.db import models
from jalali_date import date2jalali

from account_module.models import User


# Create your models here.


class ArticleCategory(models.Model):
    # vaqti az ****_set  estefade konim ke ye rabete ijad karde bashim beyne jadavel va ye jorayii sube set dashte bashim age injore nabashe khob inkaro nmikonim
    parent = models.ForeignKey('ArticleCategory', on_delete=models.CASCADE, blank=True, null=True,
                               verbose_name='انتخاب دسته بندی مقاله')
    title = models.CharField(max_length=300, verbose_name='عنوان دسته بندی')
    url_title = models.CharField(max_length=300, verbose_name='عنوان در url', unique=True)
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیر فعال')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته بندی مقاله'
        verbose_name_plural = 'دسته بندی مقالات'


class Article(models.Model):
    title = models.CharField(max_length=300, verbose_name='عنوان مقاله')
    slug = models.SlugField(max_length=400, verbose_name='عنوان در url', db_index=True, allow_unicode=True)
    short_description = models.CharField(max_length=500, verbose_name='توضیحات کوتاه')
    main_description = models.TextField(verbose_name='توضیحات اصلی')
    image = models.ImageField(upload_to='images/aricles', verbose_name='عکس مقاله')
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیرفعال')
    category = models.ManyToManyField(ArticleCategory, verbose_name='دسته بندی مقاله')
    author = models.ForeignKey(User, verbose_name='نویسنده', on_delete=models.CASCADE, null=True, editable=False)
    date = models.DateTimeField(auto_now=True, editable=False, verbose_name='تاریخ')

    def __str__(self):
        return self.title

    def jalali_create_date(self):
        return date2jalali(self.date)

    def jalali_create_time(self):
        return self.date.strftime("%H:%M")

    # badi in ravesh ine ke engar harjayi bekhay estefade koni toye model haye mokhtalef bayaf method dorost koni

    class Meta:
        verbose_name = 'ایجاد مقاله'
        verbose_name_plural = 'ایجاد مقالات'


class ArticleComments(models.Model):
    parent = models.ForeignKey('ArticleComments', on_delete=models.CASCADE, null=True, blank=True, verbose_name='والد')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='مقاله')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ')
    text = models.TextField(verbose_name='متن نظر')

    class Meta:
        verbose_name = 'نظر مقاله'
        verbose_name_plural = 'نظرات مقاله'

    def __str__(self):
        return str(self.user)  # user chon forigen key hast bayad besorat str benevisi ta error nade


class ArticleCommentFormModel(models.Model):
    name = models.CharField(max_length=300, verbose_name='نام کاربری')
    email_address = models.EmailField(max_length=300, verbose_name='ایمیل کاربر')
    text = models.TextField(verbose_name='متن نظر')

    class Meta:
        verbose_name = 'ایحاد نظر مقاله'
        verbose_name_plural = 'ابحاد نظرات مقاله'

    def __str__(self):
        return self.name
