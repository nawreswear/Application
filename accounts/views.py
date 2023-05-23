from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
@login_required
def login(request):
    context={'val':"Menu Acceuil"}
    return render(request,'accounts/login.html')

# Create your views here.
