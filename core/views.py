from django.contrib.auth import login
from django.shortcuts import render, redirect

from core.forms import SingUpForm


def frontpage(request):
    return render(request, 'core/frontpage.html')


def signup(request):
    form = SingUpForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('frontpage')
    return render(request, 'core/signup.html', {'form': form})
