from flask import Flask, render_template, request
import json
from data import goals
from days import days

app = Flask(__name__)


@app.route('/')
def render_main():
    return "главная"


@app.route('/all/')
def render_all():
    return "здесь будут преподаватели"


@app.route('/goals/<goal>/')
def render_goal(goal):
    return "здесь будет цель "+goal


@app.route('/profiles/<id>/')
def render_teacher(id):
    with open("data.json", "r", encoding='utf-8') as f:
        teachers_list = json.load(f)
    teacher = teachers_list[0]
    for temp in teachers_list:
        if temp["id"] == int(id):
            teacher = temp
    return render_template('profile.html', teacher=teacher, goals=goals, days=days)


@app.route('/request/')
def render_request():
    return "здесь будет цель заявка на подбор"


@app.route('/request_done/')
def render_request_done():
    return "заявка на подбор отправлена"


@app.route('/booking/<id>/<day>/<time>/')
def render_booking(id):
    return "здесь будет форма бронирования "+id


@app.route('/booking_done/')
def render_booking_done():
    return "заявка отправлена"


if __name__ == '__main__':
    app.run(debug=True)
