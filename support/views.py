
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

def contact_success_view(request):
    return render(request, 'support/contact_success.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Send email
            send_mail(
                f'Contact Form Submission from {name}',
                message,
                email,
                [settings.CONTACT_EMAIL],
                fail_silently=False,
            )

            return redirect('contact_success')
    else:
        form = ContactForm()

    # Ensure template exists in support/templates/support/
    return render(request, 'support/contact.html', {'form': form})
