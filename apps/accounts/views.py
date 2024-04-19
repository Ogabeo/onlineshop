
from datetime import datetime
from django.shortcuts import render, redirect
from django.views import View
from apps.accounts.forms import RegisterUserForm, LoginForm, UpdateUserForm, PasswordResetForm, CheckVerifyCodeForm, PasswordResetConfirmForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import User, UserResetPasswordCode
from apps.base.utilits import send_mail_code
class UserRegisterView(View):
    form_class = RegisterUserForm
    def get(self, request):
        form = self.form_class()
        context={
            "form":form
        }
        return render(request, 'accounts/register.html', context)
    def post(self, request):
        user_form = self.form_class(data=request.POST)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, "tizimdan muvaffaqiyatli ro'yxatdan o'tdingiz...")
            return redirect('index')

        messages.error(request, "Tizimdan ro'yxatdan o'ta olmadingiz...")
        context ={
            "form":"form",
        }
        return render(request, 'accounts/register.html', context)
    
class LoginView(View):
    form_class = LoginForm
    def get(self, request):
        form = self.form_class()
        context={
            'form':form
        }
        return render(request, "accounts/login.html", context)
    def post(self, request):
        user_form=self.form_class(data=request.POST)
        if user_form.is_valid():
            user=authenticate(request, username = user_form.cleaned_data['email'], password = user_form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                messages.success(request, "siz tizimga muvaffaqiyatli kirdingiz...")
                return redirect("index")
            messages.error(request, "Login yoki parol noto'g'ri!!!")
            return render(request, "accounts/login.html", {'form': user_form})
        

        messages.error(request, user_form.errors)
        return render(request, "accounts/login.html", {'form': user_form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('index')
    

class UpdateUserView(View):
    form_class = UpdateUserForm
    def get(self, request):
        form = self.form_class(instance=request.user)
        context={
            'form':form
        }
        return render(request, "accounts/update_profile.html", context )
    def post(self, request):
        user_form=self.form_class(data=request.POST, files=request.FILES, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, "Muvaffaqiyatli yangilandi...")
            return redirect("index")
        messages.error(request, user_form.errors)
        return render(request, 'accounts/update_profile.html', {'form':user_form})

    
class PasswordResetView(View):
    form_class = PasswordResetForm
    def get(self, request):
        form = self.form_class()
        context={
            'form':form
        }
        return render(request, "accounts/password_reset_form.html", context)

    def post(self, request, *args, **kwargs):
        email_form = self.form_class(request.POST)
        if email_form.is_valid():
            verify = email_form.save()
            print(verify)
            
            send_mail_code(verify.email, verify.code)
            messages.success(request, "Emailingizga kod yuborildi...")
            return redirect("accounts:check_verify", uuid=verify.id)
        
         
        messages.error(request, 'qandaydir xatolik yuz berdi')
        return render(request, 'accounts/password_reset_form.html', {'email_form':email_form})
    
class CheckVerifyCodeView(View):
    form_class =CheckVerifyCodeForm

    def get(self, request, uuid):
        form = self.form_class()
        context={
            'form':form
        }
        return render(request, "accounts/password_reset_check_verify_code.html", context)
    def post(self, request, uuid):
        verify_form = self.form_class(request.POST)
        if not verify_form.is_valid():
            messages.error(request, verify_form.errors)
            return render(request, "accounts/password_reset_check_verify_code.html", {'form':verify_form})
        
        code = verify_form.cleaned_data.get('code')

        verify_code=UserResetPasswordCode.objects.filter(id=uuid, expiration_time__gte=datetime.now(), is_confirmation=False, code=code).first()
        if not verify_code:
            messages.error(request, "Kod xato yoki vaqti tugagan iltimos qayta urinib ko'ring...")
            return render(request, "accounts/password_reset_check_verify_code.html", {'form':verify_form})
        
        verify_code.is_confirmation = True
        verify_code.save()

        messages.success(request, "kod to'g'ri endi yangi parol kiriting:")
        return redirect("accounts:password_reset_confirm", uuid=uuid)
    
class PasswordResetConfirmView(View):
    form_class= PasswordResetConfirmForm

    def get(self, request, uuid):
        form =self.form_class()
        context={
            'form':form
        }
        return render(request, 'accounts/password_reset_confirm.html', context)

    def post(self, request, uuid):
        password_form = self.form_class(request.POST)
        if password_form.is_valid():
            email = UserResetPasswordCode.objects.get(id=uuid).email
            user = User.objects.get(email=email)
            password = password_form.cleaned_data.get('password')
            user.set_password(password)
            user.save()
            messages.success(request, "Parollaringiz o'zgartirildi...")
            return redirect("accounts:login")
        messages.error(request, password_form.errors)
        return render(request, "accounts/password_reset_confirm.html", {"form": password_form})
    
        

        



            


