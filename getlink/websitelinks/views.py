from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
from django.template import loader
import subprocess
from .websearch import get
from .games import game
from .movies import movie
from .musics import music
from .images import image
from asgiref.sync import sync_to_async
import time, asyncio
from .models import users

# Create your views here.
def index(request) :
    return HttpResponseRedirect(reverse("websites"))

def websites(request):
    return render(request, "websitelinks/websites.html")

def movies(request) :
    return render(request, "websitelinks/movies.html")    

def musics(request) :
    return render(request, "websitelinks/musics.html")    

def games(request) :
    return render(request, "websitelinks/games.html")    

def images(request) : 
    return render(request, "websitelinks/images.html")    

def animes(request) :
    
    user = users.objects.all()
    context = dict()
    context['context'] = user
   # print('SOO', context)
   
    return render(request, "websitelinks/animes.html", context)
      #, {'animeweb': animeweb}) 
   # return render(request, "websitelinks/animessearch.html", {'context': context})

def animessearch(request) :
    
    context = dict()
    context['context'] = get()
    
    t = loader.get_template("websitelinks/animessearch.html")
    return HttpResponse(t.render(context, request))

def gamessearch(request) :
    
    context = dict()
    context['context'] = game()
    
    t = loader.get_template("websitelinks/gamessearch.html")
    return HttpResponse(t.render(context, request))

def moviessearch(request) :
    
    context = dict()
    context['context'] = movie()
    
    t = loader.get_template("websitelinks/moviessearch.html")
    return HttpResponse(t.render(context, request))

def musicssearch(request) :
    
    context = dict()
    context['context'] = music()
    
    t = loader.get_template("websitelinks/musicssearch.html")
    return HttpResponse(t.render(context, request))

def imagessearch(request) :
    
    context = dict()
    context['context'] = image()
    
    t = loader.get_template("websitelinks/imagessearch.html")
    return HttpResponse(t.render(context, request))

        
def book(request):
    if request.method == "POST":
        input = request.POST.get('user')
        if input != "" :
            print('lallal')
            user = users.objects.create(urls = (request.POST["user"]))
        print('herehere', input)
   # return render(request, "websitelinks/animes.html")
    return HttpResponseRedirect(reverse("animes") ) 

def check(request):
    if request.method == "POST":
        mylink = users.objects.all()
        id = mylink[0]
        member = request.POST.getlist('mylink')
        context = dict()
        context['context'] = mylink
        pil  = request.POST.get('user')
        #member.delete()
        linkid = users.objects.get(id = pil)
        linkid.delete()


        print(member)
        print('pills',pil)
    return HttpResponseRedirect(reverse("animes"))


    
