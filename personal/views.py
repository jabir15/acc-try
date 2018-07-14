from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError, EmailMessage
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
            # contact_name = request.POST.get('contact_name','')
            # from_email = request.POST.get('contact_email','')
            # subject = request.POST.get('content_subject','')
            # message = request.POST.get('content','')
            contact_name = form.cleaned_data['contact_name']
            subject = form.cleaned_data['content_subject']
            message = """Message from """ + contact_name + """. email-ID is: """ + sender + form.cleaned_data['content']
            sender = form.cleaned_data['contact_email']
            cc_myself = form.cleaned_data['cc_myself']

            recipients = ['assamcollegecode.pythonanywhere@gmail.com']
            if cc_myself:
                recipients.append(sender)
            email = EmailMessage(subject, message, sender,recipients,reply_to=[sender,])
            try:
                email.send()
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            messages.success(
                request, "Thank you! We will get back with you soon.")
            return redirect('contact')

    return render(request, 'personal/contact.html', {'form': form, })
