from django.http import HttpRequest, JsonResponse, HttpResponse
from django.shortcuts import render

from order_module.models import order, order_detail
from product_module.models import product


# Create your views here.


def Add_to_order(request: HttpRequest):
    if request.user.is_authenticated:
        product_id = int(request.GET.get('product_id'))
        product_count = int(request.GET.get('count'))
        if product_count < 1 :
            return JsonResponse({
                'status': 'not-valid-number',
                'text': 'تعداد محصول وارد شده معتبر نیست',
                'icon': 'error',
                'confirmButtonText' : 'فهمیدم'
            })
        Product = product.objects.filter(pk=product_id, is_active=True, is_delete=False).first()
        if Product is not None:
            current_order, bool = order.objects.get_or_create(is_paid=False, user_id=request.user.id)
            current_order_detail = current_order.order_detail_set.filter(product_id=product_id).first()
            if current_order_detail is not None:
                current_order_detail.count += int(product_count)
                current_order_detail.save()
            else:
                new_detail = order_detail(order_id=current_order.id, product_id=product_id, count=product_count)
                # deqat kon field hayii ke hast ro inja por koni
                new_detail.save()

        else:
            return JsonResponse({
                'status' : 'product-error',
                'text' : 'محصول مورد نظر پیدا نشد',
                'icon' : 'error',
                'confirmButtonText': 'فهمیدم'
            })

        return JsonResponse({
            'status' : 'success',
            'text': 'محصول با موفقیت به سبد خرید شما اضافه شد',
            'icon': 'success',
            'confirmButtonText': 'متوجه شدم'
        })
    else:
        return JsonResponse({
            'status': 'not-authenticated',
            'text': 'برای افزودن محصول به سبد خرید ابتدا باید لاگین نمایید',
            'icon': 'warning',
            'confirmButtonText': 'ورود به حساب کاربری'

        })


