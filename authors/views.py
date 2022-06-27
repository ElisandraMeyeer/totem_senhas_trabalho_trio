from authors.forms import  RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import redirect, render
from django.urls import reverse

# Create your views here.

def register_view(request):
    register_form_data = request.session.get('register_form_data',None)
    form = RegisterForm(register_form_data)
    
    return render(request, 'authors/pages/register_view.html',{
        'form':form,
    })

def register_create(request):
    
    if not  request.POST:
        raise Http404()
    POST = request.POST
    
    request.session['register_form_data']=POST
    form = RegisterForm(request.POST)

    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(user.password)
        user.save()
        messages.success(request, 'Seu usuário foi registrado com sucesso!')
        print("Passei aqui")
        del(request.session['register_form_data'])

    return redirect('authors:register')