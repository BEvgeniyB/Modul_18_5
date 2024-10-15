

from django.shortcuts import render

# Create your views here.

def main(request):
    title = 'Главная страница сайта'
    context = {'Title':title,}
    return render(request,"main_task3.html",context=context)

def shop(request):
    title = 'Магазин'
    context = {'list':['SSD 256gb','SSD 512gb','SSD 1024gb'],'Title':title}
    return render(request,"shop_task3.html",context=context)

def shopping_cart(request):
    title = 'Корзина'
    context = {'title':title,}
    return render(request,"shopping_cart_task3.html",context=context)