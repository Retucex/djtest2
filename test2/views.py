from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.views import generic

from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = 'test2/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'test2/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'test2/results.html'


def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'test2/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))


def new_question(request):
    date = str(timezone.datetime.date(timezone.now()))
    return render(request, 'test2/new.html', {'date': date})


def create_question(request):
    print(request.POST)
    choices = [v for k, v in request.POST.items() if 'choice' in k]

    datetime_str = request.POST['date'] + ' ' + request.POST['time']
    valid_datetime = timezone.datetime.strptime(datetime_str, '%Y-%m-%d %H:%M')

    q = Question.objects.create(
        question_text=request.POST['question_text'],
        valid_until=valid_datetime,
        pub_date=timezone.now()
    )

    for choice in choices:
        Choice.objects.create(
            question=q,
            choice_text=choice,
            votes=0
        )

    return HttpResponseRedirect(reverse('polls:index'))