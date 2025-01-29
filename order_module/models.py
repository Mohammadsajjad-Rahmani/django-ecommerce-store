from django.db import models

from account_module.models import User
from product_module.models import product


# Create your models here.


class order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    is_paid = models.BooleanField(verbose_name='نهایی شده / نشده ')
    order_date = models.DateTimeField(blank=True, null=True, verbose_name='تاریخ پرداخت')

    def calculate_total(self):
        total = 0
        if self.is_paid:
            for order_detail in self.order_detail_set.all():
                total += order_detail.final_price * order_detail.count
        else:
            for order_detail in self.order_detail_set.all():
                total += order_detail.product.price * order_detail.count
        return total

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = 'سبد خرید'
        verbose_name_plural = 'سبد های خرید'


class order_detail(models.Model):
    order = models.ForeignKey(order, on_delete=models.CASCADE, verbose_name='سبد خرید')
    product = models.ForeignKey(product, on_delete=models.CASCADE, verbose_name='محصول')
    final_price = models.IntegerField(null=True , blank=True , verbose_name='قیمت نهایی تکی محصول')
    count = models.IntegerField(verbose_name='تعداد')
    def get_multiply(self):
        return self.count * self.product.price

    def __str__(self):
        return str(self.order)

    class Meta:
        verbose_name = 'جزییات محصول'
        verbose_name_plural = 'جزییات محصولات'
