#  функция будет считать суточную калорийность

def daily_calorie(floor, weight, growth, age, activity):
    lst = [weight, growth, age, activity]
    for i in lst:
        if i <= 0:
            return "не правильно введены данные!"
    if floor != "ж" and floor != "м":
        return "не правильно введен пол!"
    if floor == 'ж':
        result = (655.1 + (9.563 * weight) + (1.85 * growth) - (4.676 * age)) * activity
        return round(result)
    if floor == 'м':
        result = (66.5 + (13.75 * weight) + (5.003 * growth) - (6.775 * age)) * activity
        return round(result)



result2 = daily_calorie(floor="ж", weight=87, growth=175, age=32, activity=1.3)
print(result2)

#
# floor = str(input('Введите пол(М или Ж): '))
# weight = int(input('Введите свой вес: '))
# growth = int(input('Введите свой рост: '))
# age = int(input('Введите свой возраст: '))
# activity = float(input('Введите КФА: '))
# print('Суточное потребление калорий: ', daily_calorie())
