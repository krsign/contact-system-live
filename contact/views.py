from django.shortcuts import render,redirect
from django.http import HttpResponse
from contact.models import *
from contact.forms import ContactForm, ContactUsForm
# Create your views here.

def index(request):
    contacts =Contact.objects.all()
    return render(request, 'contact/home.html', context = {'contacts':contacts})

def about(request):
    return render(request, 'contact/about.html')

def add_contact_form(request):
    if request.method == 'GET':
        form = ContactForm()
        return render(request, 'contact/new-contact.html', context={'form':form})

    else:
        form = ContactForm(request.POST, request.FILES)

        if form.is_valid():

            obj = Contact.objects.create(**form.cleaned_data)
            return render(request, 'contact/thankyou.html')

        else:
            return render(request, 'contact/new-contact.html', context={'form':form})


def update_contact_form(request, id):

    contact = Contact.objects.get(id=id)
    if request.method == 'GET':
        form = ContactForm(instance=contact)
        return render(request, 'contact/contact.html', context={'form':form})
    else:
        form = ContactForm(request.POST, request.FILES, instance=contact)
        if form.is_valid():
            form.save()
            return render(request, 'contact/thankyou.html')
        else:
            return render(request, 'contact/contact.html', context={'form':form})

def delete_contact_form(request, id):
    contact = Contact.objects.get(id=id)
    if request.method == 'POST':
        contact.delete()
        return redirect('home')

    return render(request, 'contact/delete.html' , context={'contact':contact})


def contact_us_form(request):
    if request.method == 'GET':

        form = ContactUsForm()
        return render(request, 'contact/contact-us.html', context={'form':form})

    else:
        form = ContactUsForm(request.POST)
        if form.is_valid():
            return render(request, 'contact/thankyou.html')
        else:
            return render(request, 'contact/contact-us.html', context={'form':form})