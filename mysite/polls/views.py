from django.http import HttpResponse,HttpResponseRedirect
from .models import Choice, Question
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")


# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     # output = ', '.join([q.question_text for q in latest_question_list])
#     # return HttpResponse(output)				#displays the latest 5 poll questions in the system, separated by commas,
#     											# according to publication date without using html

#     context = {
#         'latest_question_list': latest_question_list,
#     }

#     # template = loader.get_template('polls/index.html')    
#     # return HttpResponse(template.render(context, request)) #That code loads the template called polls/index.html and passes it a context.
#     													     #The context is a dictionary mapping template variable names to Python objects.

#     return render(request, 'polls/index.html', context)  #The render() function takes the request object as its first argument,
    													 # a template name as its second argument and a dictionary as its optional third argument.
    													 # It returns an HttpResponse object of the given template rendered with the given context.


# def detail(request, q):
#     # return HttpResponse("You're looking at question %s." % q)
#     try:
#         question = Question.objects.get(pk=q)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, 'polls/detail.html', {'question': question})

    #A shortcut: get_object_or_404()
    #The get_object_or_404() function takes a Django model as its first argument and an arbitrary number of keyword arguments, 
    #which it passes to the get() function of the model’s manager.

# def detail(request, q):
#     question = get_object_or_404(Question, pk=q)
#     return render(request, 'polls/detail.html', {'question': question})


# def results(request, question_id):
#     # response = "You're looking at the results of question %s."
#     # return HttpResponse(response % question_id)
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    # return HttpResponse("You're voting on question %s." % question_id)

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



#_____________________________________________________________________________
#using Django’s generic views

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    # def get_queryset(self):
    #     """Return the last five published questions."""
    #     return Question.objects.order_by('-pub_date')[:5]

    # We need to amend the get_queryset() method and change it so
    #  that it also checks the date by comparing it with timezone.now(). 
    def get_queryset(self):
	    """
	    Return the last five published questions (not including those set to be
	    published in the future).
	    """
	    return Question.objects.filter(
	        pub_date__lte=timezone.now()
	    ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
	#The DetailView generic view expects the primary key value captured from the URL to be called "pk",
	#so we’ve changed question_id to pk for the generic views.
    model = Question #Each generic view needs to know what model it will be acting upon.
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'