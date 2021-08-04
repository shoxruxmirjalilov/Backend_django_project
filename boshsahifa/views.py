from django.shortcuts import render
from .models import Bosh_sahifa
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
# Create your views here.



class Index(ListView):
    model = Bosh_sahifa
    template_name = 'index.html'
    queryset=Bosh_sahifa.objects.all()
    context_object_name = 'btext'

class IndexDetail(DetailView):
    model = Bosh_sahifa
    context_object_name = 'b'
    template_name = 'bosh_sahifa_detail.html'    

class IndexCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Bosh_sahifa
    template_name = 'bosh_sahifa_new.html'
    success_url = reverse_lazy('index')
    fields = ('title','text')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # user superuser ekanini tekshirish
    def test_func(self):
        return self.request.user.is_superuser    

class IndexUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Bosh_sahifa
    fields = ('title', 'text')
    template_name = 'bosh_sahifa_edit.html'
    success_url = reverse_lazy('index')

    def test_func(self):
        return self.request.user.is_superuser 

class IndexDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Bosh_sahifa
    template_name = 'bosh_sahifa_delete.html'
    success_url = reverse_lazy('index')

    def test_func(self):
        return  self.request.user.is_superuser        
