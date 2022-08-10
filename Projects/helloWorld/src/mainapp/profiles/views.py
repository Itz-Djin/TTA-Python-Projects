from django.http import HttpResponse
from django.shortcuts import render
from .models import profiles

def admin_console(request):
    users =  profiles.objects.all()
    return render(request, 'profiles/profile_page.html', {'users':users})
