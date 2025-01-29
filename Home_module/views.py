from django.db.models import Count , Sum
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from account_module.utils.create_list import group_list
from product_module.models import product, product_visit, product_category
from site_module.models import site_setting, footer_links_title, Slider



# Create your views here.

# estefade az class base view ha point haye mosbat khodesho dare masalan mishe az template view estefade kard ya in ke beshe rahat yeser function az qabl tarif shode tosh estefade kard


# def index(request):
#     return render(request, 'Home_module/index_page.html')
# class HomeView(View):
#     def get(self, request):
#         context = {
#             'data': 'This is data'
#         }
#         return render(request, 'Home_module/index_page.html', context)
#


class HomeView(TemplateView):
    # ba ers bari az madoule templateview mibnim ke chqadar rahat mishe yek sahfe jadi  ro render kard ya inke ye context ferstad
    template_name = 'Home_module/index_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slider: Slider = Slider.objects.filter(is_active=True)
        latest_product = product.objects.filter(is_active=True, is_delete=False).order_by('-id')[:8]
        most_visited_product = product.objects.filter(is_active=True, is_delete=False).annotate(
            visitcount=Count('product_visit')).order_by('-visitcount')[:8]
        # command ii ke inja minevisi aval tabdil be qury mishe va bad roye data base emal mishe yanai nemire 5 ta product ro one by one biare
        categories = list(product_category.objects.filter(is_active=True, is_delete=False)[:5])
        # vaqti ye method mesle ye list be query eemal mikoni hamonja ejra mishe sabr nmikone ke to load koni ya niaz be data dashte bashi
        categories_product = []
        for category in categories:
            item = {
                'id': category.id,
                'title': category.title,
                'products': list(category.category.all())
            }
            categories_product.append(item)
        most_bought_product = product.objects.annotate(order_sum_count=Sum('order_detail__count')).filter(order_detail__order__is_paid=True).order_by('-order_sum_count')[:8]
        #darvaqe annotate lahze vakeshi ye soton be satr mored nazar ezafe mikone
        # for products in most_bought_product:
        #     print(products.order_sum_count)
        context['most_bought_product'] = group_list(most_bought_product)
        context['categories'] = categories_product
        context['latest_product'] = group_list(latest_product)
        context['most_visited_product'] = group_list(most_visited_product)

        context['slider'] = slider
        return context


def contact_page(request):
    return render(request, 'Home_module/contact_page.html')


def site_header(request):
    setting: site_setting = site_setting.objects.filter(is_main_setting=True).first()
    return render(request, 'shared/header_component.html', {
        'site_setting': setting
    })


def site_footer(request):
    setting: site_setting = site_setting.objects.filter(is_main_setting=True).first()
    footer_link_box = footer_links_title.objects.all()
    for item in footer_link_box:
        item.footer_link  # eshare mikone be majmoe link haye tarif shode

    return render(request, 'shared/footer_component.html', {
        'site_setting': setting,
        'footer_link_box': footer_link_box
    })


class About_page(TemplateView):
    template_name = 'Home_module/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        setting: site_setting = site_setting.objects.filter(is_main_setting=True).first()
        context['site_setting'] = setting
        return context
