from django.shortcuts import render, redirect
from matonat.settings import EMAIL_HOST_USER
from . import forms 
from django.core.mail import send_mail
from django.utils import timezone
from aloqa.forms import MyCommentForm
from django.contrib import messages


# Create your views here.

def aloqa(request):
    form = forms.Email()    
        
    context = {
        'form' : form,    
        }
    if request.method == 'POST':
        form = forms.Email(request.POST)
        subject = 'Sizning fikringiz  muvaffaqiyatli yuborildi!'
        message = request.POST.get('message')
        email = request.POST.get('email')
        send_mail(subject,
            message, EMAIL_HOST_USER, [email], fail_silently = False)  
        form = MyCommentForm(request.POST)     
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.save()
            messages.success(request, 'Sizning fikringiz  muvaffaqiyatli yuborildi!')
            return redirect('aloqa')
    else:
        form = MyCommentForm()    
    return render(request, 'aloqa.html', context)

 

