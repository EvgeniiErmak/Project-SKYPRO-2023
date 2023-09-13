class Hero:

  def go_right(self):
    print("Я иду направо")

  def go_left(self):
    print("Я иду налево")

  def observe(self):
    print("Я осматриваюсь")


pythomir = Hero()
flaskomir = Hero()
djangomir = Hero()

heroes = []

heroes.append(pythomir)
heroes.append(flaskomir)
heroes.append(djangomir)

# Не удаляйте код ниже, это проверка (иначе мы укусим вас за бочок)
assert len(heroes) == 3, "в списке не три героя"
assert isinstance(pythomir, Hero) , "pythomir – не экземпляр Hero"
assert isinstance(flaskomir, Hero) , "flaskomir – не экземпляр Hero"
assert isinstance(djangomir, Hero) , "djangomir – не экземпляр Hero"
print("Условия выполнены")