from django.shortcuts import render, HttpResponseRedirect, render, redirect

from django.http import HttpResponse
from django.urls import reverse
from django.views.generic import TemplateView

from Portfolio_App.models import herohome, about, service, experience, banner, portfolio, discount, plan, client, \
    skillname
from django.conf import settings
from Portfolio_App.forms import ContactForm
from django.contrib import messages
from django.core.mail import send_mail, EmailMessage

# Create your views here.

app_name = 'Portfolio_App'


def index(request):
    header = herohome.objects.all()
    skills = about.objects.all()
    skilltitle = skillname.objects.all()
    services = service.objects.all()
    context = {'header': header, 'skills': skills,
               'skilltitle': skilltitle, 'services': services}
    return render(request, 'Portfolio_App/index.html', context)

class Contact(TemplateView):
    template_name = './Portfolio_App/index.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        message = "From: " + email + "n/"  " " + message

        mail = EmailMessage(subject, message, to= [settings.EMAIL_HOST_USER])
        mail.content_subtype = 'html'
        mail.send()
        return render(request, './Portfolio_App/index.html')



#==========Send mail

# class Contact(TemplateView):
#     template_name = './Portfolio_App/index.html'
#
#     def get(self, request):
#         return render(request, self.template_name)
#
#     def post(self, request):
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         subject = request.POST.get('subject')
#         message = request.POST.get('message')
#
#         mail = EmailMessage(subject, message, settings.EMAIL_HOST_USER, [email])
#         mail.content_subtype = 'html'
#         mail.send()
#         return render(request, './Portfolio_App/index.html')
