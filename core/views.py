from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Olá, Mundo! Esta é a página principal da app core.</h1>")