import maqolalar
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import   TemplateView, DetailView
from .models import Maqola, Maqolalar
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
# Create your views here.



class MaqolaView(TemplateView):
    template_name = 'maqolalar.html'


    def get_context_data(self, **kwargs):
         context = super().get_context_data(**kwargs)
         context['maqolalar'] = Maqolalar.objects.all()
         context['maqola'] = Maqola.objects.all()
         return context




class MaqolaDetail(DetailView):
    model = Maqola
    context_object_name = 'ii'
    template_name = 'maqola.html'

class MaqolalarDetail(DetailView):
    model = Maqolalar
    context_object_name = 'i'
    template_name = 'maqolaa.html'    

class MaqolaCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Maqola
    template_name = 'maqola_new.html'
    success_url = reverse_lazy('maqola')
    fields = ('title','summary','text')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # user superuser ekanini tekshirish
    def test_func(self):
        return self.request.user.is_superuser 

class MaqolaUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Maqola
    fields = ('title','summary','text')
    template_name = 'maqola_edit.html'
    success_url = reverse_lazy('maqola')

    def test_func(self):
        return self.request.user.is_superuser 

class MaqolaDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Maqola
    template_name = 'maqola_delete.html'
    success_url = reverse_lazy('maqola')

    def test_func(self):
        return  self.request.user.is_superuser            

class MaqolalarCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Maqolalar
    template_name = 'maqola-img_new.html'
    success_url = reverse_lazy('maqola')
    fields = ('photo','title','summary','text')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # user superuser ekanini tekshirish
    def test_func(self):
        return self.request.user.is_superuser   

class MaqolalarUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Maqolalar
    fields = ('photo','title','summary','text')
    template_name = 'maqolaa_edit.html'
    success_url = reverse_lazy('maqola')

    def test_func(self):
        return self.request.user.is_superuser 

class MaqolalarDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Maqolalar
    template_name = 'maqolaa_delete.html'
    success_url = reverse_lazy('maqola')

    def test_func(self):
        return  self.request.user.is_superuser                 