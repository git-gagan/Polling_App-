import django
from django.http.response import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, resolve_url
from django.urls import reverse
from django import http
# Create your views here.
# My first view here from the Polling App documentation

from django.http import HttpResponse
from .models import Question, Choice

def index(request):
    # return HttpResponse("Hello, This is the very first view!")
    # Modify the index view to display latest 5 questions or all of them
    # Using Django free Database API
    latest_question_list = Question.objects.order_by("-pub_date")
    context = {'latest_question_list' : latest_question_list}
    return render(request, './index.html', context)

# Creating More views

def detail(request, question_id):
    try:
        question = Question.objects.get(pk = question_id)   
    except:
        raise Http404("Question Does not exist!")
    return render(request, "./detail.html", {"question" : question})
    # or use
    # question = get_object_or_404(Question, pk=question_id) for loose coupling

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, './results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    try:
        choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
         return render(request, './detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        choice.votes += 1
        choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('Polls:results', args=(question.id,)))
        # using reverse, we need not to hardcode the url we want to go to!

