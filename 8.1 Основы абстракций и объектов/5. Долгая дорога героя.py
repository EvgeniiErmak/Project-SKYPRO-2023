class Hero:

  def go_right(self, name):
    self.name = name
    print(f"Я иду", self.name, "метров направо")

  def go_left(self, name):
    self.name = name
    print(f"Я иду", self.name, "метров налево")

  def observe(self):
    print("Я осматриваюсь")


hero = Hero()

hero.go_right(50)
hero.go_left(30)
hero.observe()