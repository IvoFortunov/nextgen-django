from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
import os
from .models import Program, ProgramImage
from .forms import EditProgramForm, ProgramImageForm
from users.models import Profile

# Create your views here.

def programs(request):   
    programs = Program.objects.all
    context = {'programs':programs}
    return render(request, 'programs/programs.html', context)


def programDetail(request, pk):
    program = Program.objects.get(id=pk)
    images = ProgramImage.objects.filter(program__id = program.id ) 
    context={'program':program, 'images':images}
    return render(request, 'programs/program-detail.html', context)

@login_required(login_url='login')
@user_passes_test(lambda u: u.is_staff)
def programsAdmin(request):   
    programs = Program.objects.all
    context = {'programs' : programs}
    return render(request, 'programs/programs-admin.html', context)

@login_required(login_url='login')
@user_passes_test(lambda u: u.is_staff)
def createProgram(request):
    p_form = EditProgramForm()
    i_form = ProgramImageForm()
    
    if request.method == 'POST':
        files = request.FILES.getlist('images')
        p_form = EditProgramForm(request.POST, request.FILES)
        if p_form.is_valid():
            program = p_form.save(commit=False)
            if not program.image:
                program.image = 'programs/default.jpg'
              
            program.save()
            for file in files:
                ProgramImage.objects.create(program=program, images=file)
            return redirect('programs-admin')
      

    context={'p_form':p_form, 'i_form':i_form, 'isNew': True}
    return render(request, 'programs/programs_form.html',context)

@login_required(login_url='login')
@user_passes_test(lambda u: u.is_staff)
def editProgram(request, pk):
    program = Program.objects.get(id=pk)
    old_image = program.image.path   
    p_form = EditProgramForm(instance=program)
    i_form = ProgramImageForm()

    if request.method == 'POST':
        files = request.FILES.getlist('images')
        p_form = EditProgramForm(request.POST, request.FILES, instance=program)        
        if p_form.is_valid():
            program = p_form.save(commit=False)

            if not program.image:
                program.image = 'programs/default.jpg'
            new_image = program.image.path
            if 'user-default' not in old_image and old_image!=new_image:
                if os.path.exists(old_image):
                    os.remove(old_image) 

            program.save()
            for file in files:
                ProgramImage.objects.create(program=program, images=file)
            return redirect('programs-admin')
      

    context={'p_form':p_form, 'i_form':i_form, 'isNew':  False}
    return render(request, 'programs/programs_form.html',context)

@login_required(login_url='login')
@user_passes_test(lambda u: u.is_staff)
def deleteProgram(request, pk):
    print(request)
    program = Program.objects.get(id=pk)
    if request.method == 'POST':
        images = ProgramImage.objects.filter(program__id = program.id )    
        for image in images:
            if os.path.exists(image.images.path):
                os.remove(image.images.path)
        if os.path.exists(program.image.path):
            os.remove(program.image.path)
        program.delete()
        messages.success(request, 'Програмата е изтрита успешно!')
        return redirect('programs-admin')

    context = {'object': program}
    return render(request, 'delete_template.html', context)
