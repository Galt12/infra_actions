from django.http import HttpResponse


def index(request):
    return HttpResponse('У меня получилось!')


def second_page(request):
    return HttpResponse('А это вторая страница!docker build -t billglasses/gates:v2.11.1989 .')
