from django.shortcuts import render

# Create your views here.


def index(request):
    response = render(request, 'personal/home.html')
    return response


def about(request):
    return render(request, 'personal/about.html')


def contact(request):
    return render(request, 'personal/basic.html', {'content': ['If you would like to contact me, please email me at', 'jabir.hussain.aec@gmail.com']})
