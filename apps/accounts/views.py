from django.shortcuts import render, redirect
from django.views import View
from .forms import RegisterUserForm, LoginForm, UpdateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


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
    form_class=LoginForm
    def get(self, request):
        form = self.form_class()
        context={
            "form":form
        }
        return render(request, 'accounts/login.html', context)
    
    def post(self, request):
        user_form = self.form_class(data=request.POST)
        if user_form.is_valid:
            user=authenticate(request, username=user_form.cleaned_data['username'], password=user_form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'Siz tizimga muvaffaqiyatli kirdingiz...')
                return redirect('index')
            messages.error(request, "Login yoki parol noto'g'ri...")
            return render(request, 'accounts/login.html', {'form':user_form})
        messages.error(request, user_form.errors)
        return render(request, 'accounts/login.html', {'form':user_form})


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

    
