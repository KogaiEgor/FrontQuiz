from django.shortcuts import render
import requests
from .services.quiz_api import get_quiz

# Create your views here.
def home_page(request):
    return render(request, 'temp.html')


def quiz_page(request, creator_id, quiz):
    if request.method == 'POST':
        # Получение данных из формы
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        dob = request.POST.get('dob')
        # Отправка данных на ваше API и получение теста
        data = {'fullname': name, 'email': email, 'phone': phone, "birth": dob}
        print(data)
        test_data = get_quiz(data, creator_id, quiz)
        # test_data = [
        #     {
        #         "question": "Что такое JavaScript?",
        #         "answers": ["Язык программирования", "Марка кофе", "Среда разработки"],
        #         "correctAnswer": 0
        #     },
        #     {
        #         "question": "Что такое HTML?",
        #         "answers": ["Язык разметки", "Язык программирования", "База данных"],
        #         "correctAnswer": 0
        #     }]
        return render(request, 'quiz.html', {'test_data': test_data})

    return render(request, 'candidate_form.html')