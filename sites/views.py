from django.shortcuts import render

def home(request):
    template_name = 'sites/home.html'
    return render(request, template_name, context=None)

def about(request):
    template_name = 'sites/about.html'
    return render(request, template_name, context=None)

def contact(request):
    template_name = 'sites/contact.html'
    return render(request, template_name, context=None)