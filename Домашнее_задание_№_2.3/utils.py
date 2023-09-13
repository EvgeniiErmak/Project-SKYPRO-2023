import json

"""
Дополнительные функции для работы программы
"""

from question import Question

def load_questions(filename):
    with open(filename, "r", encoding="utf-8") as file:
        data = json.load(file)

    questions = []
    for item in data:
        text = item['q']
        complexity = int(item['d'])
        correct_answer = item['a']
        question = Question(text, complexity, correct_answer)
        questions.append(question)

    return questions


def build_statistics(questions):
    score = 0
    count = 0

    for question in questions:
        if question.is_correct():
            score = score + question.score
            count = count + 1

    return f'Вот и всё! \n' \
           f'Отвечено {count} вопроса из 10 \n' \
           f'Набрано баллов: {score}'