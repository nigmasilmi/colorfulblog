from django.shortcuts import render
from .forms import ContactForm


def home(request):
    template_name = 'index.html'
    title = 'Colorfulblog by nigm4'
    context = {'title': title}
    return render(request, template_name, context)


def contact(request):
    template_name = 'contact.html'
    title = 'Contacta al blogger'
    form = ContactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
    context = {'title': title, 'formulario': form}
    return render(request, template_name, context)


def about(request):
    template_name = 'about.html'
    title = 'Quién escribe?'
    context = {'title': title}
    return render(request, template_name, context)
