class Character():
  def move(self):
    pass

class Hero(Character):

  def __init__(self, name):
    self.name = name

  def move(self, direction, distance):

    if direction == "north":
      print(self.name, "движется", distance, "метров", "на север")
    elif direction == "south":
      print(self.name, "движется", distance, "метров", "на юг")
    elif direction == "west":
      print(self.name, "движется", distance, "метров", "на запад")
    elif direction == "east":
      print(self.name, "движется", distance, "метров", "на восток")
    else:
      print(self.name, "движется непонятно куда")


class Enemy(Character):

  def __init__(self, name):
    self.name = name

  def move(self, direction, distance):

    directions_list = {"north":"на север", "south": "на юг", "west": "на запад", "east": "на восток"}
    if direction not in directions_list.keys():
      print(self.name, "движется непонятно куда")
    else:
      print(self.name, "движется", distance, "метров", directions_list[direction])


pythomir = Hero("Питомир")
bugoonya = Enemy("Багуня")

pythomir.move("north", 50)
pythomir.move("west", 10)
pythomir.move("climb", 0)

bugoonya.move("north", 50)
bugoonya.move("west", 10)
pythomir.move("climb", 0)

# Не удаляйте код ниже, это проверка!

if not 'Character' in dir():
 print("Общий класс родитель Character не создан")

if not hasattr(Character, "move"):
 print("У общего класса отсутствует метод move")