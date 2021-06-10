from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView
from .models import BlogModel

from django.urls import reverse_lazy

class BlogUpdate(UpdateView):
    template_name = 'update.html'
    model = BlogModel
    fields = ('title','content','category')
    success_url = reverse_lazy('list')

class BlogDelete(DeleteView):
    template_name = 'delete.html'
    model = BlogModel
    success_url = reverse_lazy('list')

class BlogCreate(CreateView):
    template_name = 'create.html'
    model = BlogModel
    fields = ('title','content','category')
    success_url = reverse_lazy('list')

class BlogList(ListView):
    template_name = 'list.html'
    model = BlogModel

class BlogDetail(DetailView):
    template_name = 'detail.html'
    model = BlogModel
