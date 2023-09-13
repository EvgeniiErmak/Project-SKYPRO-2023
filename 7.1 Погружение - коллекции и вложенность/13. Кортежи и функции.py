fish = [

{"specie": "Белуга", "water": "fresh"},
{"specie": "Карась", "water": "fresh"},
{"specie": "Красноперка", "water": "fresh"},

{"specie": "Морской окунь", "water": "sea"},
{"specie": "Тунец", "water": "sea"},
{"specie": "Скумбрия", "water": "sea"},

]

def get_fish(fish_name):
    for item in fish:
        if item["specie"] == fish_name:
            return (item["specie"], item["water"])


fish_name = input().title()
fish, water = get_fish(fish_name)
print(fish, water)