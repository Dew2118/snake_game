from main import Main
import time
from datetime import datetime, timedelta
#mock
class Wall:
    def __init__(self) -> None:
        self.order = []

    def show_wall(self):
        self.order.append('show_wall')
class Fruit:
    def __init__(self,wall=None) -> None:
        self.order = []

    def create(self):
        self.order.append('create')

    def display(self):
        self.order.append('display')

class Snake:
    def __init__(self,fruit=None,wall=None) -> None:
        self.order = []
        self.n=datetime.now()

    def create(self,cords):
        self.order.append(f'create({cords.x},{cords.y})')

    def run(self):
        # print(datetime.now()-self.n)
        if datetime.now()-self.n >= timedelta(seconds=6.0001):
            self.order.append('run')
            return 'a'

def test_setup():
    wall = Wall()
    fruit = Fruit()
    snake = Snake()
    main = Main()
    main.wall = wall
    main.fruit = fruit
    main.snake = snake
    main.setup()
    assert wall.order == ['show_wall']
    assert fruit.order == ['create']
    assert snake.order == ['create(0,0)']

def test_run():
    wall = Wall()
    fruit = Fruit()
    main = Main()
    main.wall = wall
    main.fruit = fruit
    snake = Snake()
    main.snake = snake
    main.run()
    # assert 1==1
    assert 'create' in fruit.order
    assert snake.order == ['run']
    