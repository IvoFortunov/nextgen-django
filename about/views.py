from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render
from .models import About
from .forms import EditAboutForm

def about(request):   
    about = About.objects.first()
    context = {'about':about}
    return render(request, 'about/about.html', context)

@login_required(login_url='login')
@user_passes_test(lambda u: u.is_staff)
def editAbout(request):
    about = About.objects.first()
    form = EditAboutForm(instance=about)

    if request.method == 'POST':
        form = EditAboutForm(request.POST, instance=about)
        if form.is_valid():
            form.save()
            return redirect('about')
      

    context={'form':form}
    return render(request, 'about/about_form.html',context)
