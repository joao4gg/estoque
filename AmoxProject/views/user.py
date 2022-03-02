from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import redirect, render


def buscar(request):
    if request.user.is_authenticated:
        if request.user.has_perm('auth.view_user'):
            if request.method == 'GET':
                users = User.objects.filter()
                dados = {
                    'titulo': 'Usuarios - Buscar',
                    'rows': users
                }
                return render(request, 'user/buscar.html', dados)
        else:
            return redirect('/admin/')
    else:
        return redirect('/admin/')


def inserir(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            email = request.POST['email']
            username = request.POST['username']

            obj = User.objects.filter(email__exact=email).exists()
            username = User.objects.filter(username=username).exists()

            if obj:
                messages.warning(request, 'Email já cadastrado')
                return redirect('user_inserir')
            elif username:
                messages.warning(request, 'Username já cadastrado')
                return redirect('user_inserir')
            else:
                model = User.objects.create()
                model.username = request.POST['username']
                model.password = request.POST['password']
                model.first_name = request.POST['first_name']
                model.email = request.POST['email']
                model.last_name = request.POST['last_name'].upper()
                model.is_active = True
                model.save()

                if model is not None:
                    messages.success(request, 'Usuario Cadastrado com sucesso!')
                    return redirect('user_buscar')
                else:
                    messages.warning(request, 'Erro ao cadastrar usuario!')
                    return redirect('user_inserir')
        elif request.method == 'GET':
            dados = {
                'titulo': 'Usuario - Inserir',
                'flag': 0
            }
            return render(request, 'user/cadastro.html', dados)
    else:
        return redirect('/admin/')


def atualizar(request):
    d = {}


def editar(request):
    d = {}
