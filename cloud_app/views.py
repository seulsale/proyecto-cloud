from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import TODO
from django.views.generic import ListView, CreateView, UpdateView, DeleteView


def index(request):
    return render(request, 'index.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('user_index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(request.POST.get('next', 'user_index'))
            else:
                messages.warning(request, 'Verifica tu correo y contraseña')
                return redirect('login')
        elif request.method == 'GET':
            return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('index')


class TODOList(ListView):
    model = TODO
    template_name = 'user/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TODOList, self).get_context_data(**kwargs)
        context['todos'] = TODO.objects.filter(owner_id=self.request.user.id).order_by('-id')
        return context


class TODOCreate(CreateView):
    model = TODO
    fields = ['text', 'owner']
    success_url = reverse_lazy('user_index')


class TODOUpdate(UpdateView):
    model = TODO
    fields = ['completed']
    success_url = reverse_lazy('user_index')


class TODODelete(DeleteView):
    model = TODO
    success_url = reverse_lazy('user_index')
