from django.conf.urls import url
from django.contrib import admin

from polls import views

urlpatterns = [
    # /polls/ 
    url(r'^$', views.IndexView.as_view(), name='index'),

    # /polls/5/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    # /polls/5/results/
    # pk means primary key. This captured value is used by DetailView to retrieve
    # the appropriate model object
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),

    # /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
