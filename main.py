from src.snake import Snake
from src.cords import Cords
from src.fruit import Fruit
from src.wall import Wall
from datetime import timedelta, datetime

class Main:
    def __init__(self) -> None:
        self.wall = Wall()
        self.fruit = Fruit(self.wall)
        self.snake = Snake(self.fruit, self.wall)

    def setup(self):
        self.snake.create(Cords(0,0))
        self.wall.show_wall()
        self.fruit.create()

    def run(self):
        a = None
        n = datetime.now()
        while a == None:
            if datetime.now() - n > timedelta(seconds=6):
                self.fruit.create()
                n = datetime.now()
            a = self.snake.run()
            self.fruit.display()

if __name__ == '__main__':
    main = Main()
    main.setup()
    main.run()