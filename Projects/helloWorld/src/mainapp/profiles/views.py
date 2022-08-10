from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import profiles
from .forms import ProfileForm

def admin_console(request):
    users =  profiles.objects.all()
    return render(request, 'profiles/profile_page.html', {'users':users})

def details(request, pk):
    pk = int(pk)
    item = get_object_or_404(profiles, pk=pk)
    form = ProfileForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.save()
            return redirect('admin_console')
        else:
            print(form.errors)
    else:
        return render(request, 'profiles/present_profiles.html', {'form': form})