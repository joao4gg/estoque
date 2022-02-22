import json

from django.http import HttpResponse
from django.shortcuts import render, redirect


def index(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            dados = {
                'user': request.user
            }
            return render(request, 'index.html', dados)
        else:
            return redirect('/admin/')
