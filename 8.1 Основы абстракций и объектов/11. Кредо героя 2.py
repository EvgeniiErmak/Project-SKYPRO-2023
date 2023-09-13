class Hero:

  def __init__(self, name, motto):
    self.name = name
    self.motto = motto

  def say(self):
    print(self.name, "говорит:", self.motto)

# Не удаляйте код ниже, это проверка (иначе мы укусим вас за бочок)

pythomir = Hero("Питомир", "Кусь за Русь!")
pythomir.say()
djangomir = Hero("Джангомир", "Работает - и ладно!")
djangomir.say()