from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from polls.models import Question, Choice

class IndexView(generic.ListView):
	"""List view - display a list of objects on a page."""
	template_name = 'polls/index.html'
	context_object_name = 'latest_question_list'

	def get_queryset(self):
		"""Return the last 5 published poll subject."""
		return Question.objects.all().order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
	"""Detail view - display a detail page of a type of object"""
	model = Question # The model attribute depicts the model
	                 # which the request will be acting upon.
	template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
	model = Question
	template_name = 'polls/results.html'

def vote(request, question_id):
	p = get_object_or_404(Question, pk=question_id)
	try :
		selected_choice = p.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice"
		})	
	else:
		selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
