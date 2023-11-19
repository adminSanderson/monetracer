
from django.shortcuts import render


def index(request):
    data = {
        'title': 'Главная страница',
        'values': []
        }

    return render(request,'main/index.html', data)


def about(request):
    return render(request, 'main/about.html',)


def analytics(request):
    return render(request, 'main/analytics.html')




# def tracer(request):
#     return render(request, "tracer.html")
#
# def navigation(request):
#     return render(request, "navigation.html")