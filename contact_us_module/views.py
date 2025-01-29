from django.shortcuts import render, redirect

from site_module.models import site_setting
# from .forms import contact_us, new_model_contact_us
from .forms import new_model_contact_us
from .models import contact_us_models
from django.views import View
from django.views.generic.edit import FormView, CreateView
from django.views.generic import ListView
from .models import user_profile_data_base


# dastor redirect be yek sahfe dige mifrastatet
# status code 301 va 302 baraye redirect kardane

# Create your views here.

# class contact_us_view(View):
#
#     def get(self, request):
#         contact_us_obj = new_model_contact_us()
#         return render(request, 'contact_us_module/contact-us-page.html', {
#             'contact_us_obj': contact_us_obj
#         })
#
#     def post(self, request):
#         contact_us_obj = new_model_contact_us(request.POST)
#         if contact_us_obj.is_valid():
#             contact_us_obj.save()
#             return redirect('home_page')
#         return render(request, 'contact_us_module/contact-us-page.html', {
#             'contact_us_obj': contact_us_obj
#         })

# class contact_us_view(CreateView):
#     model = new_model_contact_us
#     # fields = ['full-name , . . . ']
#     template_name = 'contact_us_module/contact-us-page.html'
#     form_class = new_model_contact_us
#     success_url = '/contact-us'
#
#     def form_valid(self, form):
#         super().form_valid(form)
#         return redirect('home_page')

# toye create view valid bodan mohem nist khodesh khodkar save mikone


class contact_us_view(FormView):
    template_name = 'contact_us_module/contact-us-page.html'
    form_class = new_model_contact_us
    success_url = '/contact-us'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        setting: site_setting = site_setting.objects.filter(is_main_setting=True).first()
        context['site_setting'] = setting
        return context

    # def form_valid(self, form):
    #     form.save()
    #     return super().form_valid(form)


# def post(self, request):
#     contact_us_obj = new_model_contact_us(request.POST)
#     if contact_us_obj.is_valid():
#         contact_us_obj.save()
#         return redirect('home_page')
#     return render(request, 'contact_us_module/contact-us-page.html', {
#         'contact_us_obj': contact_us_obj
#     })


def contact_us_page(request):
    # if request.method == 'POST':
    #     enered_email = request.POST['email']
    #     if enered_email == '' :
    #         return render(request ,'contact_us_module/contact-us-page.html', {
    #             'empty_email':True
    #         })
    #     print(request.POST)
    #     print(request.POST['name'])
    #     print(request.POST['email'])
    #     print(request.POST['subject'])
    #     print(request.POST['message'])
    #     return redirect('home_page')
    if request.method == 'POST':
        contact_us_obj = new_model_contact_us(request.POST)
        # contact_us_obj = contact_us(request.POST)  # tamami chizayii ke hast dakhel object contact_us qarar migire
        if contact_us_obj.is_valid():
            # contact_us_models_obj = contact_us_models(
            #     title=contact_us_obj.cleaned_data.get('title'),
            #     email=contact_us_obj.cleaned_data.get('email'),
            #     full_name=contact_us_obj.cleaned_data.get('full_name'),
            #     message=contact_us_obj.cleaned_data.get('message'),
            # )
            # contact_us_models_obj.save()
            print(contact_us_obj)
            contact_us_obj.save()  # chon model ro be form vasl kardi niazi be estefade av code haye bala nist
            return redirect('home_page')
    else:
        contact_us_obj = new_model_contact_us()
        # contact_us_obj = contact_us()
    # gozashtane in else elzamie engar !
    return render(request, 'contact_us_module/contact-us-page.html', {
        'contact_us_obj': contact_us_obj
    })


def store(file):
    with open('temp/image.jpg', 'wb+') as dest:
        for chunk in file.chunks():
            dest.write(chunk)


class profile_file(CreateView):
    template_name = 'contact_us_module/profile_module.html'
    success_url = '/contact-us/profile'
    fields = ['image']
    model = user_profile_data_base

    # profile_file(view)
    # def get(self, request):
    #     form = profile_form()
    #     return render(request, 'contact_us_module/profile_module.html', {
    #         'form': form
    #     })
    #
    # def post(self, request):
    #     valid_pic = profile_form(request.POST, request.FILES)
    #     if valid_pic.is_valid():
    #         # store(request.FILES['profile_image'])
    #         profile = user_profile_data_base(image=request.FILES['user_image'])
    #         profile.save()
    #         return redirect('profile-url')
    #     # print(request.FILES)
    #     # store(request.FILES['profile_image'])
    #     # return redirect('profile-url')
    #     return render(request, 'contact_us_module/profile_module.html', {
    #         'form': valid_pic
    #     })


class profile_list(ListView):
    model = user_profile_data_base
    template_name = 'contact_us_module/profile_list_images.html'
    context_object_name = 'profile_pic'
