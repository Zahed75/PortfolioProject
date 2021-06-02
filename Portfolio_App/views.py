from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
from Portfolio_App.models import herohome, about, service, experience, banner, portfolio, discount, plan, client, skillname

# Create your views here.


def index(request):


    header = herohome.objects.all()
    skills = about.objects.all()
    skilltitle = skillname.objects.all()
    services = service.objects.all()
    context = {'header': header, 'skills': skills,
               'skilltitle': skilltitle, 'services': services}
    return render(request, 'Portfolio_App/index.html', context)




