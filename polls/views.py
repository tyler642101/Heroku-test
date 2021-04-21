from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader
from django import template
from .models import Question
from .models import Song
import requests
from json import dumps


# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
    
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def room(request):
    return render(request, 'polls/room.html')

def room(request):
    vote_list = Song.objects.values_list('title')
    vote_list = dumps(list(vote_list))
    URL = "https://www.googleapis.com/youtube/v3/search"
    key = "AIzaSyBtQEH431JmblFH_MAJpLC9AoyGCCOYC54"
    param1 = "snippet"
    param2= "never gonna give you up"
    param3 = "1"
    param4 = "relavance"
    param5 = "video"
    param6 = "true"
    PARAMS = {'key':key, 'part':param1, 'q':param2, 'maxResults':param3, 'type':param5, 'videoEmbeddable':param6, 'videoSyndicated':'true'}
    
    #'order':param4,
    #r = requests.get(url=URL, params=PARAMS)
    #data = r.json()
    
    #for record in data['items']:
      # youtubeKey = record['id']['videoId']
    #return HttpResponse(youtubeKey)

    # d = Song(title = "test", key = "test key")
    # d.save()
    
    return render(request, 'polls/room.html', {'youtubeKey': 'dQw4w9WgXcQ', 'vote_list':vote_list})

def youtube(request,  submit):
    URL = "https://www.googleapis.com/youtube/v3/search"
    key = "AIzaSyBtQEH431JmblFH_MAJpLC9AoyGCCOYC54"
    param1 = "snippet"
    param2= request.POST['recommend']
    param3 = "1"
    param4 = "relavance"
    param5 = "video"
    param6 = "true"
    PARAMS = {'key':key, 'part':param1, 'q':param2, 'maxResults':param3, 'type':param5, 'videoEmbeddable':param6, 'videoSyndicated':'true'}
    #'order':param4,
    #r = requests.get(url=URL, params=PARAMS)
    #data = r.json()
    
    #for record in data['items']:
    #   youtubeKey = record['id']['videoId']
    #return HttpResponse(youtubeKey)
    return render(request, 'polls/room.html', {'youtubeKey': 'dQw4w9WgXcQ'})

# def search(ytSearch):
#     URL = "https://www.googleapis.com/youtube/v3/search"
#     key = "AIzaSyBtQEH431JmblFH_MAJpLC9AoyGCCOYC54"
#     param1 = "snippet"
#     param2 = ytSearch
#     param3 = "1"
#     param4 = "relavance"
#     param5 = "video"
#     param6 = "true"
#     PARAMS = {'key':key, 'part':param1, 'q':param2, 'maxResults':param3, 'type':param5, 'videoEmbeddable':param6, 'videoSyndicated':'true'}
#     #'order':param4,
#     r = requests.get(url=URL, params=PARAMS)
#     data = r.json()
    
#     for record in data['items']:
#        youtubeKey = record['id']['videoId']
#     #return HttpResponse(youtubeKey)
#     return youtubeKey