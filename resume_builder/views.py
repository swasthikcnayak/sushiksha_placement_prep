from django.shortcuts import render, redirect, get_object_or_404

from resume_builder.forms import ContactModelForm, AboutModelForm, SkillModelForm, EducationModelForm, \
    InternshipFormExperienceForm, TrainingCertificationForm, ProjectForm, ExtraModelForm, LanguageModelForm, \
    PIModelForm, AchievementModelForm, DeclarationModelForm, OtherModelForm
from resume_builder.models import Contact, About, Skill, Education, InternshipExperience, TrainingCertification, \
    Project, Extra, Language, PersonalInterest, Achievement, Declaration, Other

count = 13
def contact(request):
    try:
        contact = Contact.objects.get(user=request.user)
    except Contact.DoesNotExist:
        contact = None
    if request.method == 'GET':
        form = ContactModelForm(instance=contact)
        context = {
            'heading': "Update the Contact Information",
            'form': form,
            'next':'resume-about',
            'width': 100/13,
        }
        return render(request, 'resume-builder/one_entry.html', context=context)
    elif request.method == 'POST':
        form = ContactModelForm(request.POST, instance=contact)
        if form.is_valid():
            row = form.save(commit=False)
            row.user = request.user
            form.save()
        return redirect('resume-contact')


def about(request):
    try:
        about = About.objects.get(user=request.user)
    except About.DoesNotExist:
        about = None
    if request.method == 'GET':
        form = AboutModelForm(instance=about)
        context = {
            'heading': "Update the Profile Information",
            'form': form,
            'prev':'resume-contact',
            'next':'resume-skills',
            'width': 200 / 13,
        }
        return render(request, 'resume-builder/one_entry.html', context=context)
    elif request.method == 'POST':
        form = AboutModelForm(request.POST, instance=about)
        if form.is_valid():
            row = form.save(commit=False)
            row.user = request.user
            form.save()
        return redirect('resume-about')


def skills(request):
    skill = Skill.objects.filter(user=request.user)
    if request.method == 'GET':
        form = SkillModelForm()
        context = {
            'heading': "Add new Skills Information",
            'form': form,
            'skills': skill,
            'prev': 'resume-about',
            'next':'resume-education',
            'width': 300 / 13,
        }
        return render(request, 'resume-builder/one_entry.html', context=context)
    elif request.method == 'POST':
        form = SkillModelForm(request.POST)
        if form.is_valid():
            row = form.save(commit=False)
            row.user = request.user
            form.save()
        return redirect('resume-skills')


def skills_edit(request, id):
    skill = Skill.objects.get(user=request.user, id=id)
    if request.method == 'GET':
        form = SkillModelForm(instance=skill)
        context = {
            'heading': "Update the Skills Information",
            'form': form,
        }
        return render(request, 'resume-builder/one_entry.html', context=context)
    elif request.method == 'POST':
        form = SkillModelForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
        return redirect('resume-skills')


def skills_delete(request, id):
    skill = Skill.objects.get(id=id, user=request.user).delete()
    return redirect('resume-skills')


def education(request):
    ed = Education.objects.filter(user=request.user)
    if request.method == 'GET':
        print(ed)
        form = EducationModelForm()
        context = {
            'heading': "Add new Education Information",
            'form': form,
            'education': ed,
            'prev': 'resume-skills',
            'next':'resume-internship',
            'width': 400 / 13,
        }
        return render(request, 'resume-builder/one_entry.html', context=context)
    elif request.method == 'POST':
        form = EducationModelForm(request.POST)
        if form.is_valid():
            row = form.save(commit=False)
            row.user = request.user
            form.save()
        return redirect('resume-education')


def education_edit(request, id):
    educaiton = Education.objects.get(user=request.user, id=id)
    if request.method == 'GET':
        form = EducationModelForm(instance=educaiton)
        context = {
            'heading': "Update the Education Information",
            'form': form,
        }
        return render(request, 'resume-builder/one_entry.html', context=context)
    elif request.method == 'POST':
        form = EducationModelForm(request.POST, instance=educaiton)
        if form.is_valid():
            form.save()
        return redirect('resume-education')


def education_delete(request, id):
    educaiton = Education.objects.get(id=id, user=request.user).delete()
    return redirect('resume-education')


def internship(request):
    ie = InternshipExperience.objects.filter(user=request.user)
    if request.method == 'GET':
        form = InternshipFormExperienceForm()
        context = {
            'heading': "Add new Internship Information",
            'form': form,
            'internship': ie,
            'prev': 'resume-education',
            'next':'resume-training',
            'width': 500 / 13,
        }
        return render(request, 'resume-builder/one_entry.html', context=context)
    elif request.method == 'POST':
        form = InternshipFormExperienceForm(request.POST)
        if form.is_valid():
            row = form.save(commit=False)
            row.user = request.user
            form.save()
        print(form.errors)
        return redirect('resume-internship')


def internship_edit(request, id):
    internship = InternshipExperience.objects.get(user=request.user, id=id)
    if request.method == 'GET':
        form = InternshipFormExperienceForm(instance=internship)
        context = {
            'heading': "Update the Education Information",
            'form': form,
        }
        return render(request, 'resume-builder/one_entry.html', context=context)
    elif request.method == 'POST':
        form = InternshipFormExperienceForm(request.POST, instance=internship)
        if form.is_valid():
            form.save()
        return redirect('resume-internship')


def internship_delete(request, id):
    intern = InternshipExperience.objects.get(id=id, user=request.user).delete()
    return redirect('resume-internship')


def training(request):
    train = TrainingCertification.objects.filter(user=request.user)
    if request.method == 'GET':
        form = TrainingCertificationForm()
        context = {
            'heading': "Add new Training Information",
            'form': form,
            'training': train,
            'prev': 'resume-internship',
            'next':'resume-project',
            'width': 600 / 13,
        }
        return render(request, 'resume-builder/one_entry.html', context=context)
    elif request.method == 'POST':
        form = TrainingCertificationForm(request.POST)
        if form.is_valid():
            row = form.save(commit=False)
            row.user = request.user
            form.save()
        print(form.errors)
        return redirect('resume-training')


def training_edit(request, id):
    train = TrainingCertification.objects.get(user=request.user, id=id)
    if request.method == 'GET':
        form = TrainingCertificationForm(instance=train)
        context = {
            'heading': "Update the Training Information",
            'form': form,
        }
        return render(request, 'resume-builder/one_entry.html', context=context)
    elif request.method == 'POST':
        form = TrainingCertificationForm(request.POST, instance=train)
        if form.is_valid():
            form.save()
        return redirect('resume-training')


def training_delete(request, id):
    intern = TrainingCertification.objects.get(id=id, user=request.user).delete()
    return redirect('resume-training')


def project(request):
    proj = Project.objects.filter(user=request.user)
    if request.method == 'GET':
        form = ProjectForm()
        context = {
            'heading': "Add new Project Information",
            'form': form,
            'projects': proj,
            'prev': 'resume-training',
            'next':'resume-extra',
            'width': 700 / 13,
        }
        return render(request, 'resume-builder/one_entry.html', context=context)
    elif request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            row = form.save(commit=False)
            row.user = request.user
            form.save()
        print(form.errors)
        return redirect('resume-project')


def project_edit(request, id):
    proj = Project.objects.get(user=request.user, id=id)
    if request.method == 'GET':
        form = ProjectForm(instance=proj)
        context = {
            'heading': "Update the Project Information",
            'form': form,
        }
        return render(request, 'resume-builder/one_entry.html', context=context)
    elif request.method == 'POST':
        form = ProjectForm(request.POST, instance=proj)
        if form.is_valid():
            form.save()
        return redirect('resume-project')


def project_delete(request, id):
    proj = Project.objects.get(id=id, user=request.user).delete()
    return redirect('resume-project')


def extra(request):
    try:
        ex = Extra.objects.get(user=request.user)
    except Extra.DoesNotExist:
        ex = None
    if request.method == 'GET':
        form = ExtraModelForm(instance=ex)
        context = {
            'heading': "Update the Extra Curricular Information",
            'form': form,
            'prev': 'resume-project',
            'next':'resume-language',
            'width': 800 / 13,
        }
        return render(request, 'resume-builder/one_entry.html', context=context)
    elif request.method == 'POST':
        form = ExtraModelForm(request.POST, instance=ex)
        if form.is_valid():
            row = form.save(commit=False)
            row.user = request.user
            form.save()
        return redirect('resume-extra')


def language(request):
    lang = Language.objects.filter(user=request.user)
    if request.method == 'GET':
        form = LanguageModelForm()
        context = {
            'heading': "Add new Language Information",
            'form': form,
            'lang': lang,
            'prev': 'resume-extra',
            'next':'resume-pi',
            'width': 900 / 13,
        }
        return render(request, 'resume-builder/one_entry.html', context=context)
    elif request.method == 'POST':
        form = LanguageModelForm(request.POST)
        if form.is_valid():
            row = form.save(commit=False)
            row.user = request.user
            form.save()
        return redirect('resume-language')


def language_edit(request, id):
    lang = Language.objects.get(user=request.user, id=id)
    if request.method == 'GET':
        form = LanguageModelForm(instance=lang)
        context = {
            'heading': "Update the Language Information",
            'form': form,
        }
        return render(request, 'resume-builder/one_entry.html', context=context)
    elif request.method == 'POST':
        form = LanguageModelForm(request.POST, instance=lang)
        if form.is_valid():
            form.save()
        return redirect('resume-language')


def language_delete(request, id):
    lang = Language.objects.get(id=id, user=request.user).delete()
    return redirect('resume-language')


def pi(request):
    try:
        pi = PersonalInterest.objects.get(user=request.user)
    except PersonalInterest.DoesNotExist:
        pi = None
    if request.method == 'GET':
        form = PIModelForm(instance=pi)
        context = {
            'heading': "Update the Personal Interest Information",
            'form': form,
            'prev': 'resume-language',
            'next':'resume-achievement',
            'width': 1000 / 13,
        }
        return render(request, 'resume-builder/one_entry.html', context=context)
    elif request.method == 'POST':
        form = PIModelForm(request.POST, instance=pi)
        if form.is_valid():
            row = form.save(commit=False)
            row.user = request.user
            form.save()
        return redirect('resume-pi')


def achievement(request):
    try:
        ach = Achievement.objects.get(user=request.user)
    except Achievement.DoesNotExist:
        ach = None
    if request.method == 'GET':
        form = AchievementModelForm(instance=ach)
        context = {
            'heading': "Update the Achievements Information",
            'form': form,
            'prev': 'resume-pi',
            'next':'resume-declaration',
            'width': 1100 / 13,
        }
        return render(request, 'resume-builder/one_entry.html', context=context)
    elif request.method == 'POST':
        form = AchievementModelForm(request.POST, instance=ach)
        if form.is_valid():
            row = form.save(commit=False)
            row.user = request.user
            form.save()
        return redirect('resume-achievement')


def declaration(request):
    try:
        dec = Declaration.objects.get(user=request.user)
    except Declaration.DoesNotExist:
        dec = None
    if request.method == 'GET':
        form = DeclarationModelForm(instance=dec)
        context = {
            'heading': "Update the Declaration Information",
            'form': form,
            'prev': 'resume-achievement',
            'next':'resume-other',
            'width': 1200 / 13,
        }
        return render(request, 'resume-builder/one_entry.html', context=context)
    elif request.method == 'POST':
        form = DeclarationModelForm(request.POST, instance=dec)
        if form.is_valid():
            row = form.save(commit=False)
            row.user = request.user
            form.save()
        return redirect('resume-declaration')


def other(request):
    oth = Other.objects.filter(user=request.user)
    if request.method == 'GET':
        form = OtherModelForm()
        context = {
            'heading': "Add any other specific Information",
            'form': form,
            'other': oth,
            'prev': 'resume-declaration',
            'width': 1300 / 13,
        }
        return render(request, 'resume-builder/one_entry.html', context=context)
    elif request.method == 'POST':
        form = OtherModelForm(request.POST)
        if form.is_valid():
            row = form.save(commit=False)
            row.user = request.user
            form.save()
        return redirect('resume-other')


def other_edit(request, id):
    oth = Other.objects.get(user=request.user, id=id)
    if request.method == 'GET':
        form = OtherModelForm(instance=oth)
        context = {
            'heading': "Update the Information",
            'form': form,
        }
        return render(request, 'resume-builder/one_entry.html', context=context)
    elif request.method == 'POST':
        form = OtherModelForm(request.POST, instance=oth)
        if form.is_valid():
            form.save()
        return redirect('resume-other')


def other_delete(request, id):
    oth = Other.objects.get(id=id, user=request.user).delete()
    return redirect('resume-other')
