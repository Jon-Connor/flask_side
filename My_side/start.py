from flask import Flask
from flask import render_template
from flask import request

from daily_calorie import daily_calorie
from parcing_table import ParsingTableCalories

#  создание веб-сайта
app = Flask(__name__)


#  основная логика веб-сайта

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        pass


@app.route('/breakfast', methods=['POST', 'GET'])
def breakfast():
    if request.method == 'GET':
        return render_template('breakfast.html')
    if request.method == 'POST':
        pass


@app.route('/lanch', methods=['POST', 'GET'])
def lanch():
    if request.method == 'GET':
        return render_template('lanch.html')
    if request.method == 'POST':
        pass


@app.route('/dinner', methods=['POST', 'GET'])
def dinner():
    if request.method == 'GET':
        return render_template('dinner.html')
    if request.method == 'POST':
        pass


@app.route('/table_calories', methods=['POST', 'GET'])
def table_calories():
    if request.method == 'GET':
        obj = ParsingTableCalories()
        table_title = obj.get_title_table()
        table_meet = obj.get_table_meet()
        table_chicken = obj.get_table_chicken()
        table_fish = obj.get_table_fish()
        table_agg = obj.get_table_agg()
        table_milk = obj.get_table_milk()
        table_cereals = obj.get_table_cereals()
        table_bread = obj.get_table_bread()
        table_vegetables = obj.get_table_vegetables()
        table_fruit = obj.get_table_fruit()
        table_greens = obj.get_table_greens()
        table_berries = obj.get_table_berries()
        return render_template('table_calories.html', TITLE=table_title, MEET=table_meet, CHICKEN=table_chicken,
                               FISH=table_fish, AGG=table_agg, MILK=table_milk, CEREALS=table_cereals,
                               BREAD=table_bread,
                               VEGETABLES=table_vegetables, FRUIT=table_fruit, GREENS=table_greens,
                               BERRIES=table_berries)

    if request.method == 'POST':
        return render_template('table_calories.html')


@app.route('/calories', methods=['POST', 'GET'])
def calories():
    if request.method == 'GET':
        return render_template('calories.html')

    if request.method == 'POST':
        try:
            floor = request.form["value"]
            weight = request.form['weight']
            growth = request.form['growth']
            age = request.form['age']
            activity = request.form['activity']
            result = daily_calorie(floor=str(floor), weight=int(weight), growth=int(growth), age=int(age),
                                   activity=float(activity))
            return render_template('calories.html', RESULT=result)
        except ValueError:
            error = "Заполните форму!"
            return render_template('calories.html', ERROR=error)


# запуск сайта
if __name__ == '__main__':
    app.run()
