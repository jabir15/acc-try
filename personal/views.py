from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm

# Create your views here.


def index(request):
    response = render(request, 'personal/home.html')
    return response


def about(request):
    return render(request, 'personal/about.html')


def contact(request):

    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)

        if form.is_valid():
            contact_name = request.POST.get('contact_name','')
            from_email = request.POST.get('contact_email','')
            subject = request.POST.get('content_subject','')
            message = request.POST.get('content','')
            # contact_name = form.cleaned_data['contact_name']
            # from_email = form.cleaned_data['contact_email']
            # subject = form.cleaned_data['content_subject']
            # message = form.cleaned_data['content']
            try:
                send_mail(
                    subject,
                    message,
                    from_email,
                    ['admin@example.com']
                )
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('index')

    return render(request, 'personal/contact.html', {'form': form,})
