

from django.shortcuts import render

# Create your views here.

def main(request):
    title = 'Главная страница сайта'
    context = {'Title':title,}
    return render(request,"main_task3.html",context=context)

def shop(request):
    title = 'Магазин'
    context = {'list':['Atomic Heart', 'Cyberpunk 2077','PayDay 2'],'Title':title}
    return render(request,"shop_task3.html",context=context)

def shopping_cart(request):
    title = 'Корзина'
    context = {'title':title,}
    return render(request,"shopping_cart_task3.html",context=context)