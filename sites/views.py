from django.shortcuts import render
from django.utils import timezone

from .models import ProfilOrganisasi, SosialMedia, Galeri, Klien
from akun.models import Devisi
from blog.models import Artikel, Video

def home(request):
    template_name = 'sites/home.html'
    devisis = Devisi.objects.all()
    galleries = Galeri.objects.all()
    video = Video.objects.latest('created_at')
    articles = Artikel.objects.filter(
        tanggal_terbit__lte=timezone.now()).order_by('-tanggal_terbit')[:4]
    clients = Klien.objects.all()
    context = {
        'devisis': devisis,
        'galleries': galleries,
        'video': video,
        'articles': articles,
        'clients': clients,
    }
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