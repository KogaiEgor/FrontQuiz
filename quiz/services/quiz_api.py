import requests


def get_quiz(data, creator_id, quiz_id):
    api_url = f'http://127.0.0.1:8000/{creator_id}/getquiz/{quiz_id}/'
    response = requests.post(api_url, data=data)
    if response.status_code == 200:
        # Получаем данные теста из ответа API
        test_data = response.json()
        quiz = parse_quiz(test_data)
        #print(quiz)
        # Отображаем тест на странице
        return quiz


def parse_quiz(json_data):
    parsed_quiz = []

    for question in json_data['quiz']:
        answers = [answer['content'] for answer in json_data['answers'] if answer['question'] == question['id']]
        correct_answer = next((i for i, answer in enumerate(answers) if any(
            a['is_correct'] for a in json_data['answers'] if
            a['question'] == question['id'] and a['content'] == answer)), None)
        parsed_quiz.append({
            'question': question['content'],
            'answers': answers,
            'correctAnswer': correct_answer
        })

    return parsed_quiz
