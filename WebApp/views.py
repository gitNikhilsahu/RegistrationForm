from django.shortcuts import render
from django.http import HttpResponseRedirect
from WebApp import forms

def RegistrationView(request):
    form = forms.RegistrationForm()
    if request.method == 'POST':
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks')
    else:
        form = forms.RegistrationForm()
    return render(request, 'WebApp/Registration.html', {'form': form})

def ThankView(request):
    return render(request, 'WebApp/Thanks.html')
