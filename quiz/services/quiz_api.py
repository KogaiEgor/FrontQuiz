import requests


def get_quiz(data, creator_id, quiz_id):
    try:
        api_url = f'http://127.0.0.1:8000/{creator_id}/getquiz/{quiz_id}/'
        response = requests.post(api_url, data=data)
        response.raise_for_status()
        test_data = response.json()
        quiz = parse_quiz(test_data)
        return quiz
    except requests.RequestException as e:
        print(f"Ошибка при обращении к API: {e}")
        return None


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

def send_results(data, creator_id, quiz_id):
    try:
        api_url = f'http://127.0.0.1:8000/{creator_id}/getquiz/{quiz_id}/getresult/'
        response = requests.post(api_url, data=data)
        response.raise_for_status()
        return True
    except requests.RequestException as e:
        print(f"Ошибка при обращении к API: {e}")
        return False

