from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import HttpRequest, HttpResponse, JsonResponse, Http404
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import TemplateView, ListView
from account_module.models import User
from order_module.models import order, order_detail
from account_module.views import Login
from . import forms
from .forms import ChangePasswordForm


# Create your views here.

@method_decorator(login_required, name='dispatch')
class UserPanelProfileView(TemplateView):
    template_name = 'user_panel_module/user_panel_page.html'


@method_decorator(login_required, name='dispatch')
class EditProfileView(View):

    def get(self, request: HttpRequest):
        # current_user = request.user.id # be user feli mishe az tariqe request dastresi dasht vali khob ma mikhaim user az database fetch beshe chon ke momkene user feli ke toye cooki hast up   date nashode bashe
        current_user = User.objects.filter(id=request.user.id).first()  # midonim ke yeki bishtar vojod nadare dige
        # form_model = forms.EditUserProfileForm(initial={
        #     'first_name': 'محمدسجاد',
        #     'last_name': current_user.last_name
        # })
        form_model = forms.EditUserProfileForm(
            instance=current_user)  # bayad havaset bashe ke instanci ke eijad mikoni ba on chizi ke toye model formet be onvane model estefade shode yeki bashe
        context = {
            'form_model': form_model,
            'current_user': current_user
        }
        return render(request, 'user_panel_module/edit-profile.html', context)

    def post(self, request: HttpRequest):
        # dar vahle aval moshkeli ke in model form dare ine ke saii mikone on user jadid ro besaze darsoriti ke bayad virayeshesh knoe
        current_user = User.objects.filter(id=request.user.id).first()
        form_model = forms.EditUserProfileForm(request.POST, request.FILES,
                                               instance=current_user)  # age filee upload mishe bayad tavajoh koni ke request.Files ro dashte bashi
        if form_model.is_valid():
            form_model.save(
                commit=True)  # in code be error mikhore chon ke saii mikone user feli ro roye data base save knoe na virayesh
            # commit vaqti true bashe mostaqiman roye database emal mishe
        context = {
            'form_model': form_model,
            'current_user': current_user
        }
        return render(request, 'user_panel_module/edit-profile.html', context)


@method_decorator(login_required, name='dispatch')
class ChangeProfilePassword(View):

    def get(self, request: HttpRequest):
        context = {
            'change_pass_form': ChangePasswordForm()
        }
        return render(request, 'user_panel_module/change_password_page.html', context)

    def post(self, request: HttpRequest):
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            current_user: User = User.objects.filter(id=request.user.id).first()
            if current_user.check_password(form.cleaned_data.get('current_password')):
                current_user.set_password(form.cleaned_data.get('password'))
                current_user.save()
                logout(request)
                return redirect(reverse('login-page'))
            else:
                form.add_error('password', 'رمز عبور فعلی وارد شده صحیح نمیباشد')
        context = {
            'change_pass_form': form
        }
        return render(request, 'user_panel_module/change_password_page.html', context)


@method_decorator(login_required, name='dispatch')
class order_history(ListView):
    model = order
    template_name = 'user_panel_module/order_history.html'

    def get_queryset(self):
        query = super().get_queryset()
        request = self.request
        query = query.filter(user_id=request.user.id, is_paid=True)
        return query


@login_required(login_url='login-page')  # methode 1
def user_panel_component(request: HttpRequest):
    return render(request, 'user_panel_module/components/user_panel_component.html', {})


@login_required  # method 2
def user_panel_basket(request: HttpRequest):
    current_order, bool = order.objects.prefetch_related('order_detail_set').get_or_create(is_paid=False,
                                                                                           user_id=request.user.id)
    total = current_order.calculate_total()
    context = {
        'order': current_order,
        'sum': total
    }
    return render(request, 'user_panel_module/user_basket.html', context)


@login_required
def remove_order_detail(request: HttpRequest):
    detail_id = request.GET.get('detailId')
    if detail_id is None:
        return JsonResponse({
            'status': 'not-valid-id-number',
        })
    # current_order, bool = order.objects.prefetch_related('order_detail_set').get_or_create(is_paid=False,user_id=request.user.id)
    # detail = current_order.order_detail_set.filter(pk=detail_id).first()
    detail_count, detail_dict = order_detail.objects.filter(pk=detail_id, order__is_paid=False,
                                                            order__user_id=request.user.id).delete()

    # bejaye dota query be database ye query mizane ba ye delete

    # if detail is None:
    #     return JsonResponse({
    #         'status':'order-detail-notfound'
    #     })

    if detail_count == 0:
        return JsonResponse({
            'status': 'order-detail-notfound'
        })
    # detail.delete()

    # delete ke mishe cash mishe baraye hamon ye query dige be database zade mishe

    current_order, bool = order.objects.prefetch_related('order_detail_set').get_or_create(is_paid=False,
                                                                                           user_id=request.user.id)
    total = current_order.calculate_total()
    context = {
        'order': current_order,
        'sum': total
    }
    html = render_to_string('user_panel_module/order-detail-component.html', context)
    return JsonResponse({
        'status': 'success',
        'html': html
    })


@login_required
def change_order_detail(request: HttpRequest):
    detail_id = request.GET.get('detailId')
    state = request.GET.get('state')
    if detail_id is None or state is None:
        return JsonResponse({
            'status': 'not-valid-id-number-or-state'
        })
    detail: order_detail = order_detail.objects.filter(order__user_id=request.user, order__is_paid=False,
                                                       id=detail_id).first()
    if detail is None:
        return JsonResponse({
            'status': 'not-found-such-detail'
        })
    if state == 'increase':
        detail.count += 1
        detail.save()
    elif state == 'decrease':
        if detail.count == 1:
            detail.delete()
        else:
            detail.count -= 1
            detail.save()
    else:
        return JsonResponse({
            'status': 'error'
        })
    current_order, bool = order.objects.prefetch_related('order_detail_set').get_or_create(is_paid=False,
                                                                                           user_id=request.user.id)
    total = current_order.calculate_total()
    context = {
        'order': current_order,
        'sum': total
    }
    html = render_to_string('user_panel_module/order-detail-component.html', context)
    return JsonResponse({
        'status': 'success',
        'html': html
    })


def full_order_history(request: HttpRequest , id):
    current_order, bool = order.objects.prefetch_related('order_detail_set').get_or_create(is_paid=True , pk=id , user_id=request.user.id)
    if id is None:
        raise Http404
    return render(request,'user_panel_module/more-detail-info.html',{
        'current_order': current_order,
    })