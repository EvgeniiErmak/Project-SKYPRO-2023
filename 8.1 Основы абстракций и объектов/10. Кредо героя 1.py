class Hero:
  def __init__(self, name, motto):
    self.name = name
    self.motto = motto


pythomir = Hero("Питомир", "Кусь за Русь")
flaskomir = Hero("Фласкомир", "Это нужно отметить")
djangomir = Hero("Джангомир", "Работает – и ладно!")

# Не удаляйте код ниже, это проверка (иначе мы укусим вас за бочок)

if not hasattr(pythomir, "name"): print("Имя не задано")
if not hasattr(pythomir, "motto"): print("Девиз не задан")
print("Условия выполнены")