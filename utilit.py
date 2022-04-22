import json


def get_candidates(path):
    """Функция принимает аргумент, ссылку на json-файл,
     открывает его и возвращает его в виде списока словарей"""
    with open(path, 'r', encoding='utf-8') as candidates:

        return json.loads(candidates.read())


def format_candidates(candidates_list):
    """Функция распаковывает словари и выводит
     Форматированную строку (информацию о кандидате)"""
    inf_candidate = ""
    for i in range(len(candidates_list)):
        name = candidates_list[i]['name']
        position = candidates_list[i]['position']
        skills = candidates_list[i]['skills']
        inf_candidate += f'<h1>Имя кандидата - {name}\nПозиция кандидата:' \
                         f' {position}\nНавыки кандидата: {skills}\n\n<h1>'

    return f"<pre>{inf_candidate}<pre>"


def get_candidate_id(candidates_list, candidate_id):
    """Функция принимает аргумент список словарей и номер
     Кандидата и возвращает информацию о кандидате"""
    for candidate in candidates_list:
        if candidate['id'] == candidate_id:

            return candidate


def get_candidate_skill(candidates_list, candidate_skill):
    """Функция принимает аргумент список словарей и навыки кандидата и
     Возвращает информацию тех кандидатов, которые обладают этими навыками"""
    result = []
    for candidate in candidates_list:
        candidate_skills = candidate['skills'].lower().split(', ')
        """Переменная хранит значение по ключу, разделённое через запятую в нижнем регистре"""
        if candidate_skill in candidate_skills:
            result.append(candidate)

    return result


candidates_list = get_candidates('candidates.json')
print(get_candidate_skill(candidates_list, 'python'))
