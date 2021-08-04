from django.shortcuts import render

from django.views.generic import   TemplateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Video


# Create your views here.
class VideoView(TemplateView):
    template_name = 'videolar.html'

    def get_context_data(self, **kwargs):
         context = super().get_context_data(**kwargs)
         context['video'] = Video.objects.all()
         return context

class VideoDetail(DetailView):
    model = Video
    context_object_name = 'v'
    template_name = 'video-detail.html'


class VideoCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Video
    template_name = 'video_new.html'
    success_url = reverse_lazy('video')
    fields = ('video','title','qisqacha','text')



    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # user superuser ekanini tekshirish
    def test_func(self):
        return self.request.user.is_superuser   

class VideoUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Video
    fields = ('video','title','qisqacha','text')
    template_name = 'video_edit.html'
    success_url = reverse_lazy('video')

    def test_func(self):
        return self.request.user.is_superuser 

class VideoDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Video
    template_name = 'video_delete.html'
    success_url = reverse_lazy('video')

    def test_func(self):
        return  self.request.user.is_superuser           




