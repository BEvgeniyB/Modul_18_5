from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from django.core.exceptions import ValidationError

from .forms import UserRegister

users = ["Petro", "Sergey", "Diana", "Teodor"]


# Create your views here.
def sign_up_by_html(request: WSGIRequest):
    if request.method == "POST":
        global users
        info = {'username': request.POST.get('username'), 'password': request.POST.get('password'),
                'repeat_password': request.POST.get('repeat_password'), 'age': request.POST.get('age')}

        if info['password'] == info['repeat_password']  and not users.count(info['username']) and int( info['age']) > 18:
            info["generated"] = f"Приветствуем, {info['username']}!"

        elif users.count(info['username']):
            info["error"] = "Пользователь уже существует"
            info['username'] = ''
        elif info['password'] != info['repeat_password'] :
            info["error"] = "Пароли не совпадают"
            info['password'] = ''
            info['repeat_password'] = ''

        else:
            info["error"] = "Вы должны быть старше 18"
            info['age'] = ''

        return render(request, template_name="registration_page.html", context=info)

    else:
        return render(request,'registration_page.html')



def sign_up_by_django(request: WSGIRequest):
    global users
    info = {}
    if request.method == "POST":
        form = UserRegister(request.POST)
        info['form'] = form
        if form.is_valid():
            info['username'] = form.cleaned_data["username"]
            info['password'] = form.cleaned_data["password"]
            info['repeat_password'] = form.cleaned_data["repeat_password"]
            info['age'] = form.cleaned_data["age"]

            if info['password'] == info['repeat_password'] and not users.count(info['username']):
                info["generated"] = f"Приветствуем, {info['username']}!"
            elif users.count(info['username']):
                info["error"] = "Пользователь уже существует"
            elif info['password'] != info['repeat_password']:
                info["error"] = "Пароли не совпадают"
            else:
                info["error"] = "Вы должны быть старше 18"
        return render(request, template_name="registration_page.html", context=info)

    else:
        form = UserRegister()
        return render(request, template_name="registration_page.html",context={'form':form})
