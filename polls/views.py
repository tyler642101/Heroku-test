from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Question
import requests
from django.urls import reverse
from polls.models import Choice
from django.views import generic
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.http import JsonResponse

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def room(request):
    return render(request, 'polls/room.html')

def youtube(request):
    URL = "https://www.googleapis.com/youtube/v3/search"
    key = "AIzaSyBtQEH431JmblFH_MAJpLC9AoyGCCOYC54"
    param1 = "snippet"
    param2 = "drake laugh now cry later music video"
    param3 = "1"
    # param4 = "relavance"
    param5 = "video"
    param6 = "true"
    PARAMS = {'key':key, 'part':param1, 'q':param2, 'maxResults':param3, 'type':param5, 'videoEmbeddable':param6, 'videoSyndicated':'true'}
    # 'order':param4,
    # r = requests.get(url=URL, params=PARAMS)
    # data = r.json()
    
    # for record in data['items']:
    #     youtubeKey = record['id']['videoId']
    # return HttpResponse(youtubeKey)
    return render(request, 'polls/room.html', {'youtubeKey': youtubeKey})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def home(request):
    print(request.POST["your_name"])
    # youtubeKey = 'cPJUBQd-PNM'
    youtubeKey = request.POST["your_name"]
    return render(request, "polls/home.html", {'youtubeKey': youtubeKey})

class SignUpView(CreateView):
    template_name = 'polls/signup.html'
    form_class = UserCreationForm

def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    if data['is_taken']:
        data['error_message'] = 'A user with this username already exists.'
    return JsonResponse(data)