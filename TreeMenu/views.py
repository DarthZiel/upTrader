from django.shortcuts import render


# Create your views here.


def index(request, slug=None):
    context = {'slug': slug}
    return render(request, 'TreeMenu/index.html', context=context)


def menu(request):
    return render(request, 'TreeMenu/index.html')
