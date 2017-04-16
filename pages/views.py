from django.shortcuts import render, render_to_response
from django.contrib import auth

# Create your views here.



def index(request):
    return render(request, 'pages/index.html', {'user_name': auth.get_user(request).username})

def contact(request):
    return render_to_response('pages/contact.html',)
