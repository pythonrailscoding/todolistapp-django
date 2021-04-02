from django.shortcuts import render
from .models import Task
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy

class UserList(ListView):
    model = Task
    template_name = 'yapp\index.html'

class UserCreateView(CreateView):
    model = Task
    fields = '__all__'
    template_name = 'yapp/create.html'
    success_url = reverse_lazy('index')

class UserUpdateView(UpdateView):
    model = Task
    fields = '__all__'
    template_name = 'yapp/update.html'
    success_url = reverse_lazy('index')

class UserDetailView(DetailView):
    model = Task
    template_name = 'yapp/detail.html'

class UserDeleteView(DeleteView):
    model = Task
    template_name = 'yapp/delete.html'
    success_url = reverse_lazy('index')
