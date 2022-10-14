from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect

from .forms import *
from .models import *


def index(request):
    posts = vuz.objects.all()
    return render(request, 'step1/index.html', {'title': 'Все вузы:', 'posts': posts})


def vuz_show(request, vuzid):
    vuz_from_db = get_object_or_404(vuz, pk=vuzid)
    persons = vuz_from_db.person_set.all()

    return render(request, 'step1/vuz.html', {'vuzid': vuzid, 'persons': persons, 'vuz_from_db': vuz_from_db})


def addperson(request, vuzid):
    vuz_from_db = get_object_or_404(vuz, pk=vuzid)
    if request.method == 'POST':
        form = AddPersonForm(request.POST)
        print(request.POST)
        if form.is_valid():
            try:
                name = form.cleaned_data.get("name")
                wiki = form.cleaned_data.get("wiki")
                vk = form.cleaned_data.get("vk")
                vk_subs = form.cleaned_data.get("vk_subs")
                choisen_vuz1 = form.cleaned_data.get("vuzs")
                instance = Person.objects.create(name=name, wiki=wiki, vk=vk, vk_subs=vk_subs)
                instance.vuzs.set(choisen_vuz1)
                return redirect('home')
            except Exception as e:
                print(e)
                form.add_error(None, 'Ошибка добаваление персоналии')
    else:
        form = AddPersonForm({'vuzs': [f'{vuzid}']})
    return render(request, 'step1/add.html', {'title': f'Добавление персоналии', 'form': form, 'vuz': vuz_from_db})


def pageNotFound(request, exception):
    return HttpResponseNotFound("Страница не найдена(")