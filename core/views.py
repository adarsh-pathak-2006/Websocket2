from django.shortcuts import render
from core.forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.views import View


class RegisterView(View):
    def get(self, request):
        form=RegisterForm()
        return render(request, 'register.html', { 'form':form })
