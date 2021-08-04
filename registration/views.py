from django.shortcuts import render
from . import forms


def regform(request):
    form = forms.SignUp()
    if request.method == 'POST':
        form = forms.SignUp(request.POST)
        html = 'Biz yana ushbu shaklni oldik '
        if form.is_valid():
            html = html + " Shakl haqiqiydir"
    else:
        html = 'Xush kelibsiz'
    return render(request, 'signup.html', {'html': html, 'form': form})