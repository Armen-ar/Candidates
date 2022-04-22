from flask import Flask

from utilit import get_candidates, format_candidates, get_candidate_id, get_candidate_skill

app = Flask(__name__)



@app.route('/')
def page_index():
    """Выводит на главную страницу список кандидатов"""
    candidates_list = get_candidates('candidates.json')

    return format_candidates(candidates_list)


@app.route('/candidates/<int:candidate_id>')
def page_candidates(candidate_id):
    """Выводит на страницу информацию на конкретного кандидата"""
    candidates_list = get_candidates('candidates.json')
    candidate = get_candidate_id(candidates_list, candidate_id)
    result = f"<img src={candidate['picture']}>"

    return result + format_candidates([candidate])
"""
Возвращает переменную и возврат функции get_candidate_id через функцию format_candidates
"""


@app.route('/skills/<skill>')
def page_skills(skill):
    candidates_list = get_candidates('candidates.json')

    return format_candidates(get_candidate_skill(candidates_list, skill))
"""
Возвращает возврат функции get_candidate_skill по аргументам внутри функции format_candidates
"""


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
