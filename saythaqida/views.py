from django.views.generic import TemplateView, DetailView
from .models import SaytHaqida
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy


# Create your views here.
class SaytHaqidaView(TemplateView):
    template_name = 'sayt-haqida.html'

    def get_context_data(self, **kwargs):
         context = super().get_context_data(**kwargs)
         context['haqida'] = SaytHaqida.objects.all()
         return context

class SaytHaqidaDetail(DetailView):
    model = SaytHaqida
    context_object_name = 's'
    template_name = 'sayt_haqida_detail.html'  

class SaytHaqidaCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = SaytHaqida
    template_name = 'sayt-haqida_new.html'
    success_url = reverse_lazy('haqida')
    fields = ('title','text')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # user superuser ekanini tekshirish
    def test_func(self):
        return self.request.user.is_superuser    


class HaqidaUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = SaytHaqida
    fields = ('title', 'text')
    template_name = 'haqida_edit.html'
    success_url = reverse_lazy('haqida')

    def test_func(self):
        return self.request.user.is_superuser 

class HaqidaDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = SaytHaqida
    template_name = 'haqida_delete.html'
    success_url = reverse_lazy('haqida')

    def test_func(self):
        return  self.request.user.is_superuser  