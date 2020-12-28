from flask import Flask, render_template, request
from random import sample
import json
from data import goals
from days import days

app = Flask(__name__)


@app.route('/')
def render_main():
    with open("data.json", "r", encoding='utf-8') as f:
        teachers_list = json.load(f)
    return render_template('index.html', teachers=sample(teachers_list, 6), goals = goals)


@app.route('/all/')
def render_all():
    with open("data.json", "r", encoding='utf-8') as f:
        teachers_list = json.load(f)
    return render_template('all.html', teachers=teachers_list, number_of_teachers=len(teachers_list))


@app.route('/goals/<goal>/')
def render_goal(goal):
    with open("data.json", "r", encoding='utf-8') as f:
        teachers_list = json.load(f)
    teachers_by_goal = []
    for teacher in teachers_list:
        if goal in teacher["goals"]:
            teachers_by_goal.append(teacher)
    return render_template('goal.html', goal=goals[goal], teachers_by_goal=teachers_by_goal)


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
    return render_template('request.html')


@app.route('/request_done/', methods=['POST'])
def render_request_done():
    goal = request.form.get("goal")
    time = request.form.get("time")
    client_name = request.form.get("clientName")
    client_phone = request.form.get("clientPhone")
    temp_dict = {"goal": goal, "client_time": time, "client_name": client_name, "client_phone": client_phone}
    with open("request.json", "a") as r:
        json.dump(temp_dict, r)
    return render_template('request_done.html', goal=goal, client_name=client_name, time=time, client_phone=client_phone, goals=goals)


@app.route('/booking/<id>/<day>/<time>/')
def render_booking(id, day, time):
    with open("data.json", "r", encoding='utf-8') as f:
        teachers_list = json.load(f)
    return render_template('booking.html', teacher=teachers_list[int(id)], day=day, time=time)


@app.route('/booking_done/', methods=['POST'])
def render_booking_done():
    client_weekday = request.form.get("clientWeekday")
    client_time = request.form.get("clientTime")
    client_teacher = request.form.get("clientTeacher")
    client_name = request.form.get("clientName")
    client_phone = request.form.get("clientPhone")
    temp_dict = {"client_weekday": client_weekday, "client_time": client_time, "client_teacher": client_teacher, "client_name": client_name, "client_phone": client_phone}
    with open("booking.json", "a") as b:
        json.dump(temp_dict, b)
    return render_template('booking_done.html', time=client_time, day=client_weekday, teacher=client_teacher, client_name=client_name, client_phone=client_phone)


if __name__ == '__main__':
    app.run(debug=True)
