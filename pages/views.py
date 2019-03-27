from django.shortcuts import render, redirect
from django.contrib import messages

from django.core.mail import send_mail
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST or None)
        if form.is_valid():
            form.save()
            name = form.cleaned_data['first_name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            messages.success(request, f'Uspesno ste poslali poruku')
            return redirect('/')
            
    else:
        form = ContactForm()

    return render(request, 'pages/contact.html', {'form': form })

def about_view(request):
    return render(request, 'pages/about_page.html')

def recipes_view(request):
    return render(request, 'pages/recipes.html')

