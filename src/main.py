from snake import Snake
from cords import Cords
from fruit import Fruit
from datetime import timedelta, datetime
from wall import Wall

wall = Wall()
fruit = Fruit(wall)
snake = Snake(fruit, wall)
snake.create(Cords(0,0))
a = None
n = datetime.now()
wall.show_wall()
fruit.create()
while a == None:
    if datetime.now() - n > timedelta(seconds=6):
        fruit.create()
        n = datetime.now()
    a = snake.run()
    fruit.display()