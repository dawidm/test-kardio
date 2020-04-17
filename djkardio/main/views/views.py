from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.views.generic import CreateView

from ..models import User


def index(request):
    return HttpResponse("Hello, world. You're at the test index.")


@login_required
def patients(request):
    if request.user.is_doctor:
        users = User.objects.filter(is_patient=True)
        template = loader.get_template('users.html')
        context = {
            'users': users,
        }
        #return render(request, 'users.html', context)
        return HttpResponse(template.render(context, request))
    raise PermissionDenied()


@login_required()
def home(request):
    if request.user.is_authenticated:
        if request.user.is_patient:
            return redirect('home_patient')
        else:
            return redirect('home_doctor')
    #return redirect('accounts/login')


#question = get_object_or_404(Question, pk=question_id)


#<li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li>


# # Always return an HttpResponseRedirect after successfully dealing
# # with POST data. This prevents data from being posted twice if a
# # user hits the Back button.
# return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


    # lte - less than or equal
    # return Question.objects.filter(
    #     pub_date__lte=timezone.now()
    # ).order_by('-pub_date')[:5]


# from django.contrib.auth.decorators import login_required
#
# @login_required
# def my_view(request):
#     ...