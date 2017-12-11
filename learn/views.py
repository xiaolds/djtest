from django.http import HttpResponse
from django.shortcuts import render

from learn.models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ','.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


# def users(request):
#     # get all users
#     all_users = User.objects.order_by('user_register_time')
#     return HttpResponse('\n'.join([u.user_name for u in all_users]))
#
#
# def single_user(request, user_id):
#     user_detail = User.objects.get(id=user_id)
#     return HttpResponse(str(user_detail))