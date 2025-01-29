from django.http import Http404, HttpRequest
from django.shortcuts import render, redirect

from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.crypto import get_random_string
from django.views import View

from account_module.forms import Register_form, Login_form, Forget_form, Reset_form
from account_module.models import User

from django.contrib.auth import login, logout

from account_module.utils.email_service import send_email


# Create your views here.


class Register(View):
    def get(self, request: HttpRequest):
        register_form = Register_form()
        context = {
            'register_form': register_form
        }
        return render(request, 'account_module/register_page.html', context)

    def post(self, request):
        register_form = Register_form(request.POST)
        if register_form.is_valid():
            # print(request.POST)
            print(register_form.cleaned_data)
            # todo : register user
            user_email = register_form.cleaned_data.get('email')
            user_password = register_form.cleaned_data.get('password')
            filtered_user: bool = User.objects.filter(
                email__iexact=user_email).exists()  # yek bool bar migardone fitered_user : bool type in on data ro moshakhas mikonim
            if filtered_user:
                register_form.add_error('email', 'ایمیل کاریری تکراری میباشد')
            else:
                # new_user = User(email=user_email, password=user_password, email_active_code=get_random_string(72))  age bekhaym password ro injori save konim toye database hash nmishe baraye hash kardan passwprd az set password estefade mikonim
                new_user = User(email=user_email, email_active_code=get_random_string(72), username=user_email,
                                is_active=False)
                new_user.set_password(user_password)
                new_user.save()
                # todo : send email activator link
                send_email('فعالساری حساب کاربری', new_user.email, {'user': new_user},
                           'emails/activated_page.html')
                return redirect('login-page')

        context = {
            'register_form': register_form
        }
        return render(request, 'account_module/register_page.html', context)


class Login(View):
    def get(self, request):
        login_form = Login_form
        context = {
            'login_form': login_form
        }
        return render(request, 'account_module/login_page.html', context)

    def post(self, request):
        # information login ma tavasote session ha save mishe to qesmat cookie ha age on info ha nabashan karbar logout mishe va dobare bayad login kone

        login_form = Login_form(request.POST)
        if login_form.is_valid():
            user_email = login_form.cleaned_data.get('email')
            user_password = login_form.cleaned_data.get('password')
            user: User = User.objects.filter(email__iexact=user_email).first()  # in moshakhas kardan type miad kari ke mikone intlisence ro behtar mikone
            if user is not None:
                if user.is_active:
                    is_pass_correct = user.check_password(user_password)  # password vared shode ro hash mikone va ba oni ke toye database ykie check mikone ta bbine equalan ya naa meqdare return shode boolean hastesh
                    if is_pass_correct:
                        login(request, user)  # in darvaqe hamon session ro ok mikone
                        return redirect('home_page')
                    else:
                        login_form.add_error('password', 'نام کاربی یا رمز عبور اشتباه است')
                if not user.is_active:
                    login_form.add_error('email', 'شما ثبت نام نکرده اید')
            else:
                login_form.add_error('email', 'کاربری با مشخصات زیر پیدا نشد')
        context = {
            'login_form': login_form
        }
        return render(request, 'account_module/login_page.html', context)
    # baraye inke ba in hesab django admin dastresi dashte bashi bayad is staff va is super user in account login shode true beshand


class AcitivatedAccount(View):

    def get(self, request, email_active_code):
        user: User = User.objects.filter(email_active_code__iexact=email_active_code).first()
        if user is not None:
            if user.is_active is False:
                user.is_active = True
                user.email_active_code = get_random_string(
                    72)  # in kar baraye amniate site ke user az active code bazam estefade nakone
                user.save()
                # todo : show success message to user
                return redirect('login-page')
            else:
                # todo : show your account was activated
                pass
        else:
            raise Http404


class ForgetPassword(View):

    def get(self, request: HttpRequest):
        forget_form = Forget_form()
        context = {
            'forget_form': forget_form
        }
        return render(request, 'account_module/forget_page.html', context)

    def post(self, request: HttpRequest):
        forget_form = Forget_form(request.POST)
        if forget_form.is_valid():
            user_email = forget_form.cleaned_data.get('email')
            user: User = User.objects.filter(email__iexact=user_email).first()
            if user is not None:
                # send reset password email to user
                send_email('بازیابی رمز عبور', user.email, {'user': user},
                           'emails/passwordrecovery_page.html')

            else:
                forget_form.add_error('email', 'شما حسابی در این سایت ندارید')
        context = {
            'forget_form': forget_form
        }
        return render(request, 'account_module/forget_page.html', context)


class ResetPassword(View):

    def get(self, request: HttpRequest, email_active_code):
        user: User = User.objects.filter(email_active_code__iexact=email_active_code).first()
        reset_form = Reset_form()
        # if user is None:
        #     reset_form.add_error('email', 'شما حسابی در این سایت ندارید')

        context = {
            'reset_form': reset_form,
            'user': user
        }
        return render(request, 'account_module/reset_page.html', context)

    def post(self, request: HttpRequest, email_active_code):
        # vaqti template dari va in eac ro to function post mikhaysh bayad be on temolate ham befrestish
        user: User = User.objects.filter(email_active_code__iexact=email_active_code).first()
        reset_form = Reset_form(request.POST)
        if reset_form.is_valid():
            user_password = reset_form.cleaned_data.get('password')
            if user is not None:
                user.set_password(user_password)
                user.email_active_code = get_random_string(72)
                user.is_active = True
                user.save()
                return redirect(reverse('login-page'))

        context = {
            'reset_form': reset_form,
        }
        return render(request, 'account_module/reset_page.html', context)


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('login-page'))
