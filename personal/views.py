from django.shortcuts import render

# Create your views here.


def index(request):

    if 'agree' in request.COOKIES:
        print('SET')
    else:
        print('NOT SET')
    
    response = render(request, 'personal/home.html')

    return response


def contact(request):
    return render(request, 'personal/basic.html', {'content': ['If you would like to contact me, please email me', 'jabir.hussain.aec@gmail.com']})
