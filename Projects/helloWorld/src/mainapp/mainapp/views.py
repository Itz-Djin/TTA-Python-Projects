from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    users = ["Johnny Appleseed", "Long John Silver", "Bojack Horseman", "The Human", "Ranolph Cunningham"]
    context = {
        'users': users,
    }
    return render(request, "home.html", context)