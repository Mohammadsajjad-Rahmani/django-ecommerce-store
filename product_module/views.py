from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.db.models import Avg, Count
from django.views import View

from site_module.models import SiteBanner
from .models import product, product_category, product_brand, product_visit, product_gallery, productcoment
from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from account_module.utils.http_serrvice import client_ip
from account_module.utils.create_list import group_list


# Create your views here.

# class product_list_view(TemplateView):
#     template_name = 'product_module/product_list.html'
#
#     def get_context_data(self, **kwargs):
#         product_instance = product.objects.all().order_by('-price')[:5]
#         # context = super(product_list_view, self).get_context_data()
#         context = super().get_context_data(**kwargs)
#         context['products'] = product_instance
#         return context
class product_list_view(ListView):
    template_name = 'product_module/product_list.html'
    model = product
    context_object_name = 'products'
    ordering = ['-price']
    # قیمت کم سمت راست باشه
    paginate_by = 6

    #
    # def get_queryset(self):
    #     query = super(product_list_view,
    #                   self).get_queryset()  # toye estefade az class base view ha to qesmat estefade az function hash in super() . . . bayad ezafe beshe
    #     data = query.filter(is_active=True)
    #     return data
    def get_context_data(self, *, object_list=None, **kwargs):
        # AVAL TABE GET QUERY EJRA MISHE VA ZAMANI KE TOYE TABE CONTEXT DOBARE QUERY HAMIN CLASS RO CALL MIKONIM ON TAQIRATI KE MIKHYM RO ROYE QUERY HAYII EEMAL MIKONIM KE TO TABE GET QUERY BEDst ovordim
        context = super().get_context_data()
        query = self.get_queryset()  # aval tabe query paein bad in tabe va query dobare baraye hamin ye query dige mizanim ro kole mahsolat na roye query qabli
        # engar khate bala dobare tabe query ro ejrash mikone
        query = product.objects.all()
        Product: product = query.order_by('-price').first()
        context[
            'max_value'] = max_value = Product.price if Product is not None else 0  # momkene ke data ii vojod nadashte bashe pas az error ba estefade az shart ha jologiri mikonim
        context['start_price'] = self.request.GET.get('start-price') or 0
        context['end_price'] = self.request.GET.get('end-price') or max_value
        context['banners'] = SiteBanner.objects.filter(is_active=True,
                                                       position__iexact=SiteBanner.SiteBannerPosition.product_list)
        return context

    def get_queryset(self):
        query = super(product_list_view, self).get_queryset()
        request: HttpRequest = self.request
        print(request.GET)
        # vaqti data ii toye url ferestade mishe ba request.GET behesh dastresi darim ?start=100 ye mesale data ferestadane toye url ke sahfe ham beham narize
        category_name = self.kwargs.get('cat')
        brand_name = self.kwargs.get('brand')
        start_price = request.GET.get('start-price')
        end_price = request.GET.get('end-price')
        if start_price is not None:
            # gte grater than equal
            query = query.filter(price__gte=start_price)
        if end_price is not None:
            query = query.filter(price__lte=end_price)
        if category_name is not None:
            # product.objects.filter(product_categories__url_title__iexact=)
            query = query.filter(product_categories__url_title__iexact=category_name)
        if brand_name is not None:
            query = query.filter(brand__title__iexact=brand_name)
        return query


# def product_list(request):
#     products = product.objects.all().order_by('-price')[:5]
#     # mire 5 mahsole akhar ro miare
#     return render(request, 'product_module/product_list.html', {
#         'products': products
#     })


# def product_detail(request, slug):
#     products = get_object_or_404(product, slug=slug)
#     return render(request, 'product_module/product_detail.html', {
#         'product': products
#     })

# class product_detai_view(TemplateView):
#     template_name = 'product_module/product_detail.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         slug = kwargs['slug']
#         # kilide slug
#         products = get_object_or_404(product, slug=slug)
#         context['product'] = products
#         return context


class product_detail_view(DetailView):
    template_name = 'product_module/product_detail.html'
    model = product

    def get_queryset(self):
        query = super(product_detail_view, self).get_queryset()
        return query

    def get_context_data(self, **kwargs):  # in function mahsoli ke alan dare be user neshon dade mishe ro neshon mide
        context = super().get_context_data(**kwargs)
        loaded_product = self.object
        request = self.request
        # query = self.get_queryset()
        # context['query'] = query
        favorite_product_id = request.session.get('favorite_product')
        context['is_favorite'] = favorite_product_id == str(loaded_product.id)
        context['banners'] = SiteBanner.objects.filter(is_active=True,
                                                       position__iexact=SiteBanner.SiteBannerPosition.product_detail)
        galleries = list(product_gallery.objects.filter(product_id__exact=loaded_product.id).all())
        galleries.insert(0, loaded_product)
        context['product_gallery'] = group_list(galleries, 3)
        context['related_products'] = group_list(
            list(product.objects.filter(brand_id__exact=loaded_product.brand.id).exclude(pk=loaded_product.id)[:10]), 3)
        # exclude baraye ine ke begim kodom mahsolat ro nayar
        context['comments'] = productcoment.objects.filter(purches_id__exact=loaded_product.id,
                                                           is_accepted=True).order_by('-created_date')
        context['comments_count'] = productcoment.objects.filter(
            purches_id__exact=loaded_product.id, is_accepted=True).count()
        user_ip = client_ip(self.request)
        if self.request.user.is_authenticated:
            user_id = self.request.user.id
        else:
            user_id = None
        has_been_visited = product_visit.objects.filter(ip_address__iexact=user_ip,
                                                        product_id=loaded_product.id).exists()
        if not has_been_visited:
            new_visit = product_visit(ip_address=user_ip, product_id=loaded_product.id, user_id=user_id)
            new_visit.save()
        return context


class add_favorite(View):

    def post(self, request):
        product_id = request.POST['product_id']
        product_instance = product.objects.get(pk=product_id)
        request.session['favorite_product'] = product_id
        return redirect('product_list')


def product_categories_component(request: HttpRequest):
    product_categories = product_category.objects.filter(is_active=True, is_delete=False)
    context = {
        'product_categories': product_categories
    }
    return render(request, 'product_module/components/product_categories_component.html', context)


def product_brand_component(request: HttpRequest):
    product_brand_ = product_brand.objects.annotate(product_count=Count('product')).filter(is_active=True)
    # dastore annotaate va dastore aggregate hardo barye in estefade mishan ke yesri item custome khodet ezafe koni va az tariqe va on item custome shode ham hamrah ba query asli biad
    # nokteii ke hast ine ke annotate be satr ha eemal mishe masalan 1000 satr bashe be har 1000 ta item custome shode ezafe mikone
    # for brand in product_brand_:
    #     brand.product_set.count()
    context = {
        'product_brand': product_brand_
    }
    return render(request, 'product_module/components/product_brand_component.html', context)


#
def CreateProductDetailComment(request: HttpRequest):
    if request.user.is_authenticated:
        product_comment = request.GET.get('productComment')
        product_id = request.GET.get('productId')
        new_comment = productcoment(purches_id=product_id, text=product_comment, autour_id=request.user.id)
        new_comment.save()
        # context = {
        #     'comments': productcoment.objects.filter(purches_id__exact=product_id).order_by(
        #         '-created_date'),
        #     'comments_count': productcoment.objects.filter(spurches_id__exact=product_id).count()
        # }
        # return render(request, 'includes/product_detail_comments.html', context)
        return JsonResponse({
            'status' : 'success'
        })
    else:
        return JsonResponse({
            'status' : 'not-authenticated'
        })
