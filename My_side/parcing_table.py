import requests
from bs4 import BeautifulSoup


# url = "https://rsport.ria.ru/20220514/kaloriynost-1788483172.html"
#
# html = requests.get(url=url).text
#

# with open("soup.html", "w") as file:
#     file.write(html)

# Парсинг таблиц калорийности продуктов
class ParsingTableCalories:

    def __init__(self):
        self.table_title = []
        self.table_meet = [[], [], [], [], []]
        self.table_chicken = [[], [], [], [], []]
        self.table_fish = [[], [], [], [], []]
        self.table_agg = [[], [], [], [], []]
        self.table_milk = [[], [], [], [], []]
        self.table_cereals = [[], [], [], [], []]
        self.table_bread = [[], [], [], [], []]
        self.table_vegetables = [[], [], [], [], []]
        self.table_fruit = [[], [], [], [], []]
        self.table_greens = [[], [], [], [], []]
        self.table_berries = [[], [], [], [], []]
        with open("soup.html") as file:
            html = file.read()
        self.soup = BeautifulSoup(html, "html.parser")

    def get_title_table(self):
        table_title = self.soup.find_all("div", class_="article__table-wr")[0].find_all("strong")
        for i in table_title:
            title = i.text
            self.table_title.append(title)
        return self.table_title

    def get_table_meet(self):
        table_meet = self.soup.find_all("div", class_="article__table-wr")[0]
        tr = table_meet.find_all("tr")[1:]
        for i in tr:
            product = i.find_all("p")
            title = product[0].text
            self.table_meet[0].append(title)
            protein = product[1].text
            self.table_meet[1].append(protein)
            fat = product[2].text
            self.table_meet[2].append(fat)
            carbohydrates = product[3].text
            self.table_meet[3].append(carbohydrates)
            calories = product[4].text
            self.table_meet[4].append(calories)
        return self.table_meet

    def get_table_chicken(self):
        table_meet = self.soup.find_all("div", class_="article__table-wr")[1]
        tr = table_meet.find_all("tr")[1:]
        for i in tr:
            product = i.find_all("p")
            title = product[0].text
            self.table_chicken[0].append(title)
            protein = product[1].text
            self.table_chicken[1].append(protein)
            fat = product[2].text
            self.table_chicken[2].append(fat)
            carbohydrates = product[3].text
            self.table_chicken[3].append(carbohydrates)
            calories = product[4].text
            self.table_chicken[4].append(calories)
        return self.table_chicken

    def get_table_fish(self):
        table_meet = self.soup.find_all("div", class_="article__table-wr")[3]
        tr = table_meet.find_all("tr")[1:]
        for i in tr:
            product = i.find_all("p")
            title = product[0].text
            self.table_fish[0].append(title)
            protein = product[1].text
            self.table_fish[1].append(protein)
            fat = product[2].text
            self.table_fish[2].append(fat)
            carbohydrates = product[3].text
            self.table_fish[3].append(carbohydrates)
            calories = product[4].text
            self.table_fish[4].append(calories)
        return self.table_fish

    def get_table_agg(self):
        table_meet = self.soup.find_all("div", class_="article__table-wr")[7]
        tr = table_meet.find_all("tr")[1:]
        for i in tr:
            product = i.find_all("p")
            title = product[0].text
            self.table_agg[0].append(title)
            protein = product[1].text
            self.table_agg[1].append(protein)
            fat = product[2].text
            self.table_agg[2].append(fat)
            carbohydrates = product[3].text
            self.table_agg[3].append(carbohydrates)
            calories = product[4].text
            self.table_agg[4].append(calories)
        return self.table_agg

    def get_table_milk(self):
        table_meet = self.soup.find_all("div", class_="article__table-wr")[9]
        tr = table_meet.find_all("tr")[1:]
        for i in tr:
            product = i.find_all("p")
            title = product[0].text
            self.table_milk[0].append(title)
            protein = product[1].text
            self.table_milk[1].append(protein)
            fat = product[2].text
            self.table_milk[2].append(fat)
            carbohydrates = product[3].text
            self.table_milk[3].append(carbohydrates)
            calories = product[4].text
            self.table_milk[4].append(calories)
        return self.table_milk

    def get_table_cereals(self):
        table_meet = self.soup.find_all("div", class_="article__table-wr")[10]
        tr = table_meet.find_all("tr")[1:]
        for i in tr:
            product = i.find_all("p")
            title = product[0].text
            self.table_cereals[0].append(title)
            protein = product[1].text
            self.table_cereals[1].append(protein)
            fat = product[2].text
            self.table_cereals[2].append(fat)
            carbohydrates = product[3].text
            self.table_cereals[3].append(carbohydrates)
            calories = product[4].text
            self.table_cereals[4].append(calories)
        return self.table_cereals

    def get_table_bread(self):
        table_meet = self.soup.find_all("div", class_="article__table-wr")[11]
        tr = table_meet.find_all("tr")[1:]
        for i in tr:
            product = i.find_all("p")
            title = product[0].text
            self.table_bread[0].append(title)
            protein = product[1].text
            self.table_bread[1].append(protein)
            fat = product[2].text
            self.table_bread[2].append(fat)
            carbohydrates = product[3].textbread
            self.table_bread[3].append(carbohydrates)
            calories = product[4].text
            self.table_bread[4].append(calories)
        return self.table_bread

    def get_table_vegetables(self):
        table_meet = self.soup.find_all("div", class_="article__table-wr")[12]
        tr = table_meet.find_all("tr")[1:]
        for i in tr:
            product = i.find_all("p")
            title = product[0].text
            self.table_vegetables[0].append(title)
            protein = product[1].text
            self.table_vegetables[1].append(protein)
            fat = product[2].text
            self.table_vegetables[2].append(fat)
            carbohydrates = product[3].text
            self.table_vegetables[3].append(carbohydrates)
            calories = product[4].text
            self.table_vegetables[4].append(calories)
        return self.table_vegetables

    def get_table_fruit(self):
        table_meet = self.soup.find_all("div", class_="article__table-wr")[13]
        tr = table_meet.find_all("tr")[1:]
        for i in tr:
            product = i.find_all("p")
            title = product[0].text
            self.table_fruit[0].append(title)
            protein = product[1].text
            self.table_fruit[1].append(protein)
            fat = product[2].text
            self.table_fruit[2].append(fat)
            carbohydrates = product[3].text
            self.table_fruit[3].append(carbohydrates)
            calories = product[4].text
            self.table_fruit[4].append(calories)
        return self.table_fruit

    def get_table_greens(self):
        table_meet = self.soup.find_all("div", class_="article__table-wr")[14]
        tr = table_meet.find_all("tr")[1:]
        for i in tr:
            product = i.find_all("p")
            title = product[0].text
            self.table_greens[0].append(title)
            protein = product[1].text
            self.table_greens[1].append(protein)
            fat = product[2].text
            self.table_greens[2].append(fat)
            carbohydrates = product[3].text
            self.table_greens[3].append(carbohydrates)
            calories = product[4].text
            self.table_greens[4].append(calories)
        return self.table_greens

    def get_table_berries(self):
        table_meet = self.soup.find_all("div", class_="article__table-wr")[15]
        tr = table_meet.find_all("tr")[1:]
        for i in tr:
            product = i.find_all("p")
            title = product[0].text
            self.table_berries[0].append(title)
            protein = product[1].text
            self.table_berries[1].append(protein)
            fat = product[2].text
            self.table_berries[2].append(fat)
            carbohydrates = product[3].text
            self.table_berries[3].append(carbohydrates)
            calories = product[4].text
            self.table_berries[4].append(calories)
        return self.table_berries


