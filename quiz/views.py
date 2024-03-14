from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext
from django.middleware.csrf import get_token
import requests
from .services.quiz_api import get_quiz
import json

# Create your views here.
def home_page(request):
    return render(request, 'temp.html')


def quiz_page(request, creator_id, quiz):
    if request.method == 'POST':

        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        dob = request.POST.get('dob')

        data = {'fullname': name, 'email': email, 'phone': phone, "birth": dob}
        test_data = get_quiz(data, creator_id, quiz)

        return render(request, 'quiz.html', {'test_data': test_data, 'creator_id': creator_id, 'quiz': quiz})

    return render(request, 'candidate_form.html')


def quiz_results(request, creator_id, quiz):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_answers = data.get('answers')
        print('Ответы пользователя:', user_answers)
        context = {'csrf_token': get_token(request)}

        return render(request, 'test_finished.html', context)

    return render(request, 'candidate_form.html')