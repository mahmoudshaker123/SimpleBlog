# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UserRegistrationForm
from django.contrib.auth.forms import AuthenticationForm

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('user_login')  # تحديث التوجيه إلى 'user_login' بعد التسجيل
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})

def user_login(request):  
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)  # تأكد من أن 'request' و 'user' تم تمريرهما هنا بشكل صحيح
                return redirect('post_list')  # إعادة التوجيه بعد تسجيل الدخول
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})
