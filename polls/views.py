from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader
from .models import Question
import requests

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

def youtube(request):
    URL = "https://www.googleapis.com/youtube/v3/search"
    key = "AIzaSyBtQEH431JmblFH_MAJpLC9AoyGCCOYC54"
    param1 = "snippet"
    param2 = "end of golden wind orchestral version"
    param3 = "1"
    # param4 = "relavance"
    param5 = "video"
    param6 = "true"
    PARAMS = {'key':key, 'part':param1, 'q':param2, 'maxResults':param3, 'type':param5, 'videoEmbeddable':param6}
    # 'order':param4,
    r = requests.get(url=URL, params=PARAMS)
    data = r.json()
    
    for record in data['items']:
        youtubeKey = record['id']['videoId']
    # return HttpResponse(youtubeKey)
    return render(request, 'polls/room.html', {'youtubeKey': youtubeKey})