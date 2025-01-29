from django.db import models
# from django.contrib
from django.contrib.auth.models import AbstractUser, AbstractBaseUser


# toye abstrac user alave bar setting default mishe yrkseri item khodrt ezafeh koni
# toye abstracbase user yekseri setting avalie darim va bishtar khodet bayaf customize koni
# Create your models here.

class User(AbstractUser):
    avatar = models.ImageField(verbose_name='آواتار', upload_to='images/author', null=True , blank=True)
    email_active_code = models.CharField(max_length=100, verbose_name='کد فعالسازی ایمیل')
    about_user = models.TextField(verbose_name='درباره نویسنده', null=True, blank=True)
    address = models.TextField(verbose_name='آدرس', null=True, blank=True)

    # user_profile = models.ImageField(upload_to='profile/user-profile', null=True)

    def __str__(self):
        if self.first_name != '' and self.last_name != '':
            return self.get_full_name()
        return self.email

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    # baraye inke betoni az Abstracuser estefade koni bayad toye main setting proje tarifesh koni
    # bad az migration va migrate be moshkel mikhori be khater inke useri ke dari estefade mikoni az qabl tarif shode va age hala bekhay taqir bedi nmitone taqirat jadid ro emal kone pas ya nayad aval proje user ro customize koni ya inke tamam app ha va tanzimat marbot be ionha ro movaqata comment koni va data base qabli ro pak koni va yeki taze besazi
    # migration migrate uncomment migrate
