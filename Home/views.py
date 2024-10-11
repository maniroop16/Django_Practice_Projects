from django.shortcuts import render, redirect
from django.http import HttpResponse
from Cooking.seed import *
from Home.utils import *

# Create your views here.

'''def home(request):
    return HttpResponse("<h1>This is the first launch</h1>")'''
def home(request):
    samp_tabel = [
        {"name" : "Sai", "age":24},
        {"name" : "mani", "age":23},
        {"name" : "roop", "age":17},
        {"name" : "krishna", "age":30},
        {"name" : "Jeevith", "age":1}
                  ]
    
    text = "Home Django"

    

    return render(request, "home/index.html", context = {"data": samp_tabel, "text": text})


def about(request): 
    return render(request, "home/about.html",context = { "text": "About"})

def contact(request):
    return render(request, "home/contact.html",context = { "text": "Contacts"})


def testingmail(request):
    send_email()
    return redirect("/")
