from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
from django.template import loader
import subprocess
from .websearch import get
from asgiref.sync import sync_to_async
import time, asyncio


# Create your views here.
def index(request) :
    return HttpResponseRedirect(reverse("websites"))

def websites(request):
    return render(request, "websitelinks/websites.html")

def movies(request) :
    return render(request, "websitelinks/movies.html")    

def music(request) :
    return render(request, "websitelinks/music.html")    

def games(request) :
    return render(request, "websitelinks/games.html")    

def images(request) : 
    return render(request, "websitelinks/images.html")    

def animes(request) :
    return render(request, "websitelinks/animes.html")#, {'animeweb': animeweb}) 
   # return render(request, "websitelinks/animessearch.html", {'context': context})

def animessearch(request) :
    
    context = dict()
    context['context'] = get()
    
    t = loader.get_template("websitelinks/animessearch.html")
    return HttpResponse(t.render(context, request))
    
   
    

    
