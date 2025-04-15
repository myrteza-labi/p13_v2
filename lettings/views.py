from django.shortcuts import render, get_object_or_404
from .models import Letting
from django.http import HttpResponse

def test_error(request):
    raise Exception("Test d'erreur 500")

def lettings_index(request):
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)

def letting(request, letting_id):
    letting = get_object_or_404(Letting, id=letting_id)
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'lettings/letting.html', context)

def test_sentry(request):
    raise Exception("Test de Sentry")

