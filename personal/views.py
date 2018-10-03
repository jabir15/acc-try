from django.contrib import messages
from django.core.mail import BadHeaderError, EmailMessage
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import College
# Create your views here.


# class CollegeListView(ListView):
#     model = College
#     def colleges(self):
#         return College.objects.all().order_by('name')

def actrules(request):
    response = render(request, 'personal/actrules.html')
    return response

def updates(request):
    response = render(request, 'personal/updates.html')
    return response

def colleges(request):
    
    college_list_A = College.objects.filter(name__startswith='A').order_by('name')
    college_list_B = College.objects.filter(name__startswith='B').order_by('name')
    college_list_C = College.objects.filter(name__startswith='C').order_by('name')
    college_list_D = College.objects.filter(name__startswith='D').order_by('name')
    college_list_E = College.objects.filter(name__startswith='E').order_by('name')
    college_list_F = College.objects.filter(name__startswith='F').order_by('name')
    college_list_G = College.objects.filter(name__startswith='G').order_by('name')
    college_list_H = College.objects.filter(name__startswith='H').order_by('name')
    college_list_I = College.objects.filter(name__startswith='I').order_by('name')
    college_list_J = College.objects.filter(name__startswith='J').order_by('name')
    college_list_K = College.objects.filter(name__startswith='K').order_by('name')
    college_list_L = College.objects.filter(name__startswith='L').order_by('name')
    college_list_M = College.objects.filter(name__startswith='M').order_by('name')
    college_list_N = College.objects.filter(name__startswith='N').order_by('name')
    college_list_O = College.objects.filter(name__startswith='O').order_by('name')
    college_list_P = College.objects.filter(name__startswith='P').order_by('name')
    college_list_Q = College.objects.filter(name__startswith='Q').order_by('name')
    college_list_R = College.objects.filter(name__startswith='R').order_by('name')
    college_list_S = College.objects.filter(name__startswith='S').order_by('name')
    college_list_T = College.objects.filter(name__startswith='T').order_by('name')
    college_list_U = College.objects.filter(name__startswith='U').order_by('name')
    college_list_V = College.objects.filter(name__startswith='V').order_by('name')
    college_list_W = College.objects.filter(name__startswith='W').order_by('name')
    college_list_X = College.objects.filter(name__startswith='X').order_by('name')
    college_list_Y = College.objects.filter(name__startswith='Y').order_by('name')
    college_list_Z = College.objects.filter(name__startswith='Z').order_by('name')
    list_of_colleges = { 'colleges_A':college_list_A, 'colleges_B': college_list_B,
                        'colleges_C':college_list_C,
                        'colleges_D':college_list_D,
                        'colleges_E':college_list_E,
                        'colleges_F':college_list_F,
                        'colleges_G':college_list_G,
                        'colleges_H':college_list_H,
                        'colleges_I':college_list_I,
                        'colleges_J':college_list_J,
                        'colleges_K':college_list_K,
                        'colleges_L':college_list_L,
                        'colleges_M':college_list_M,
                        'colleges_N':college_list_N,
                        'colleges_O':college_list_O,
                        'colleges_P':college_list_P,
                        'colleges_Q':college_list_Q,
                        'colleges_R':college_list_R,
                        'colleges_S':college_list_S,
                        'colleges_T':college_list_T,
                        'colleges_U':college_list_U,
                        'colleges_V':college_list_V,
                        'colleges_W':college_list_W,
                        'colleges_X':college_list_X,
                        'colleges_Y':college_list_Y,
                        'colleges_Z':college_list_Z,
    }
    
    return render(request, 'personal/college_list.html', list_of_colleges)

def search_colleges(request):
    if request.method=="POST":
        query = request.POST.get('query','').strip().lower()
    
    if (query.find(':')>=0):
        tag = query.split(':')[0].strip()
        q = query.split(':')[1].strip()
        if tag.startswith('d'):
            college_filter = College.objects.filter(college_district__startswith=q).order_by('college_district')
        elif tag.startswith('a'):
            college_filter = College.objects.filter(full_address__icontains=q).order_by('full_address')
        else:
            college_filter = College.objects.filter(name__icontains=q)

    else:
        college_filter = College.objects.filter(name__icontains=query)

    return render(request, 'personal/includes/college_search.html', {'colleges_filter':college_filter})


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
            message = """Message from """ + contact_name + """. """ + form.cleaned_data['content']
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
