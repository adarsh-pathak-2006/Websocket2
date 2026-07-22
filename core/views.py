from django.shortcuts import render, redirect
from core.forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.views import View
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin


class RegisterView(View):
    def get(self, request):
        form=RegisterForm()
        return render(request, 'register.html', { 'form':form })
    
    def post(self, request):
        form_data=RegisterForm(request.POST)
        if form_data.is_valid():
            username=form_data.cleaned_data['username']
            pass1=form_data.cleaned_data['password']
            pass2=form_data.cleaned_data['rep_password']
            if pass1==pass2:
                if User.objects.filter(username=username).exists():
                    return render(request, 'register.html', {'form':form_data, 'user_err':'username already exists..try another'})
                else:
                    user=User.objects.create(username=username, password=pass1)
                    login(user)
                    return redirect('login')
            else:
                return render(request, 'register.html', {'form':form_data, 'pass_err':'password mismatch in both fields'})
        else:
            return render(request, 'login.html', { 'invalid':'invalid inputs' }) 

class LoginView(View):
    def get(self, request):
        form=LoginForm()
        return render(request, 'login.html', { 'form':form })
    
    def post(self, request):
        form_data=LoginForm(request.POST)
        if form_data.is_valid():
            username=form_data.cleaned_data['username']
            password=form_data.cleaned_data['password']
            user=authenticate(username=username, password=password)
            if user is None:
                return render(request, 'login.html', {'user_err':'user does not exist..try registration first'})
            else:
                login(user)
                return redirect('home')
        else:
            return render(request, 'login.html', { 'invalid':'invalid inputs' })    
    
class HomeView(LoginRequiredMixin,View):
    def get(self, request):
        return render(request, 'home.html')