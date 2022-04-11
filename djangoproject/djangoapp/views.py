from django.shortcuts import render

# Create your views here.


def home(request):
    context = {
            'form':'form'
    }
    return render(request, 'djangoapp/home.html',context)
