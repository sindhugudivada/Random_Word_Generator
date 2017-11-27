from django.shortcuts import render,HttpResponse,redirect
from time import gmtime,strftime
from django.utils.crypto import get_random_string
from models import *



# Create your views here.

def show_random(request):
    print "my husband is too caring"
    if 'number' not in request.session:
        request.session['number'] = 0
    if request.method == "POST":
        request.session['number'] += 1
    word = get_random_string(length=14)
    context = {
        'number': request.session['number'],
        'word': word
    }
    return render(request,'random_word/index.html', context)


def reset(request):
    request.session['number'] = 0
    return redirect('/random_word/')