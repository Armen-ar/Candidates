import json

from flask import Flask

app = Flask(__name__)

with open('candidates.json', 'r', encoding='utf-8') as file:  # открывает файл для чтения
    candidates = json.loads(file.read())  # переменная хранит файл в виде словаря


@app.route('/')  # '/' это означает первая(стартовая) страница
def page_index():
    """Выводит на главную страницу список кандидатов"""
    inf_candidate = ""  # пустая строка информация о кандидате
    for i in range(len(candidates)):  # проходя по всем ключам
        name = candidates[i]['name']  # переменная хранит значение по ключу 'name'
        position = candidates[i]['position']  # переменная хранит значение по ключу 'position'
        skills = candidates[i]['skills']  # переменная хранит значение по ключу 'skills'
        inf_candidate += f'{name} - \n{position}\n{skills}\n\n'  # запись переменных в строку

    return f"<h1><pre>{inf_candidate}<pre><h1>"  # возвращает информацию о всех кандидатах


@app.route('/candidates/<name>')  # <....> это скобки аргумента, т.е. конкретно
def page_candidates(name: str):
    inf_candidate = ""
    for i in range(len(candidates)):  # проходя по всем ключам
        if name.lower() == candidates[i]['name'].lower():
            name = candidates[i]['name']  # переменная хранит значение по ключу 'name'
            position = candidates[i]['position']  # переменная хранит значение по ключу 'position'
            skills = candidates[i]['skills']  # переменная хранит значение по ключу 'skills'
            picture = candidates[i]['picture']
            inf_candidate += f'<img src={picture}>\n{name} - \n{position}\n{skills}\n\n'

    return f"<pre>{inf_candidate}<pre>"


@app.route('/skills/<skill>')
def page_skills(skill: str):
    inf_candidate = ""
    for i in range(len(candidates)):  # проходя по всем ключам
        if skill.lower() in candidates[i]['skills'].lower():
            name = candidates[i]['name']  # переменная хранит значение по ключу 'name'
            position = candidates[i]['position']  # переменная хранит значение по ключу 'position'
            skills = candidates[i]['skills']  # переменная хранит значение по ключу 'skills'
            inf_candidate += f'{name} - \n{position}\n{skills}\n\n'  # запись переменных в строку

    return f"<pre>{inf_candidate}<pre>"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
