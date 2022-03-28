from django.shortcuts import render, HttpResponse


def mainp(request):
    return render(request, 'index.html')
