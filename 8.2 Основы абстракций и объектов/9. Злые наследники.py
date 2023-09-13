class Enemy():

  def __init__(self, name, health):
    self.is_alive = True;
    self.name = name
    self.health = health


class Dragon(Enemy):

  def bite(self):
    print("я кусаюсь")

  def burn(self):
    print("я дышу огнем")


dragon = Dragon("Инхеритий Проворный", 300)

# Не удаляйте код ниже, это проверка!

dragon.bite()
dragon.burn()