from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /polls/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /polls/5/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
    # ex: /polls/room
    path('room/', views.room, name='room'),
    # ex: /polls/youtube
    path('youtube/', views.youtube, name='youtube'),

    path('home/', views.home, name='home'),

    url(r'^signup/$', views.SignUpView.as_view(), name='signup'),

    url(r'^ajax/validate_username/$', views.validate_username, name='validate_username'),
]