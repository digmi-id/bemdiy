from django.shortcuts import render

from .models import ProfilOrganisasi, SosialMedia
from akun.models import Devisi

def home(request):
    template_name = 'sites/home.html'
    devisi = Devisi.objects.all()
    context = {'devisis': devisi}
    return render(request, template_name, context)


def about(request):
    template_name = 'sites/about.html'
    profile = ProfilOrganisasi.objects.latest('updated_at')
    context = {'profile': profile}
    return render(request, template_name, context)

def contact(request):
    template_name = 'sites/contact.html'
    profile = ProfilOrganisasi.objects.latest('updated_at')
    context = {'profile': profile}
    return render(request, template_name, context)