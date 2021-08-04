from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationsForm
# Create your views here.

class SignUp(CreateView):
    form_class = CustomUserCreationsForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'