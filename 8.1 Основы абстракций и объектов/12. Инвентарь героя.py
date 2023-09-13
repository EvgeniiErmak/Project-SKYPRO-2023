class Hero:
  things = []

  def __init__(self, name):
    pass

  def collect(self, thing):
    self.thing = thing
    self.things.append(thing)

# Не удаляйте код ниже, это проверка (иначе мы укусим вас за бочок)

pythomir = Hero("Питомир")
pythomir.collect("Усы хитрости")
pythomir.collect("Рукавички пряморукости")

if len(pythomir.things) == 2:
  print("Проверка пройдена")
else:
  print("Добавление в список things работает некорректно")