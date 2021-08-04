from django.views.generic import TemplateView, DetailView
from .models import Infografika
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy


# Create your views here.
class InfografikaView(TemplateView):
    template_name = 'infografika.html'

    def get_context_data(self, **kwargs):
         context = super().get_context_data(**kwargs)
         context['infografika'] = Infografika.objects.all()
         return context

class InfografikaDetail(DetailView):
    model = Infografika
    context_object_name = 'info'
    template_name = 'infografika_detail.html'  

class InfografikaCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Infografika
    template_name = 'infografika_new.html'
    success_url = reverse_lazy('infografika')
    fields = ('title','text')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # user superuser ekanini tekshirish
    def test_func(self):
        return self.request.user.is_superuser    


class InfografikaUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Infografika
    fields = ('title', 'text')
    template_name = 'infografika_edit.html'
    success_url = reverse_lazy('infografika')

    def test_func(self):
        return self.request.user.is_superuser 

class InfografikaDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Infografika
    template_name = 'infografika_delete.html'
    success_url = reverse_lazy('infografika')

    def test_func(self):
        return  self.request.user.is_superuser  