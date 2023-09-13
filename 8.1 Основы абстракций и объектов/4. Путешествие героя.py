class Hero:

  def go_right(self):
    print("Я иду направо")

  def go_left(self):
    print("Я иду налево")

  def observe(self):
    print("Я осматриваюсь")

hero = Hero()

hero.go_left()
hero.observe()
hero.go_right()
hero.go_right()
hero.go_right()
hero.observe()
hero.go_right()