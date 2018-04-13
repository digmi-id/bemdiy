# from django.shortcuts import get_object_or_404, render
# from django.http import HttpResponseRedirect, HttpResponse
# from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Artikel, Kategori, Tag, Video

class IndexView(generic.ListView):
    template_name = 'blog/list.html'
    context_object_name = 'latest_artikel_list'

    def get_queryset(self):
        return Artikel.objects.filter(
            tanggal_terbit__lte=timezone.now()).order_by('-tanggal_terbit')[:5]

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        context['video'] = Video.objects.latest('created_at')
        context['categories'] = Kategori.objects.all()
        return context


class DetailView(generic.DetailView):
    model = Artikel
    template_name = 'blog/detail.html'

    def get_queryset(self):
        return Artikel.objects.filter(tanggal_terbit__lte=timezone.now())