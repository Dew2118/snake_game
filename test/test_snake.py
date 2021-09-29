from src.snake import Snake
import src.snake as snk
from src.cords import Cords

class Fruit:
    def __init__(self,is_hit_return) -> None:
        self.order = []
        self.is_hit_return = is_hit_return

    def is_hit(self,current_position):
        self.order.append(f'is_hit({current_position})')
        return self.is_hit_return

class Display:
    def __init__(self,input = 'none') -> None:
        self.order = []
        self.input = input
    
    def display_char(self,char,cords):
        self.order.append(f'display_char({char},{cords.x},{cords.y})')

    def get_arrow(self):
        return self.input

def test_create():
    snake = Snake('fruit','wall')
    snake.create(Cords(1,1))
    assert snake.current_positions == [Cords(1,1)]

def test_run():
    display = Display()
    snk.display_obj = display
    snake = Snake('fruit','wall')
    snake.current_positions = [Cords(1,1)]
    snake.orientation = 'up'
    snake.run()
    assert snake.current_positions == [Cords(1,1),Cords(1,0)]
    snake.current_positions = [Cords(1,1)]
    snake.orientation = 'right'
    snake.run()
    assert snake.current_positions == [Cords(1,1),Cords(2,1)]
    snake.current_positions = [Cords(1,1)]
    snake.orientation = 'down'
    snake.run()
    assert snake.current_positions == [Cords(1,1),Cords(1,2)]
    snake.current_positions = [Cords(1,1)]
    snake.orientation = 'left'
    snake.run()
    assert snake.current_positions == [Cords(1,1),Cords(0,1)]

    display = Display('end')
    snk.display_obj = display
    assert snake.run() == 'a'

    display = Display('RIGHT')
    snk.display_obj = display
    snake = Snake('fruit','wall')
    snake.current_positions = [Cords(1,1)]
    snake.orientation = 'up'
    snake.run()
    assert snake.last == 'RIGHT'
    assert snake.current_positions == [Cords(1,1),Cords(2,1)]
    snake.current_positions = [Cords(1,1)]
    snake.orientation = 'right'
    snake.run()
    assert snake.current_positions == [Cords(1,1),Cords(1,2)]
    snake.current_positions = [Cords(1,1)]
    snake.orientation = 'down'
    snake.run()
    assert snake.current_positions == [Cords(1,1),Cords(0,1)]
    snake.current_positions = [Cords(1,1)]
    snake.orientation = 'left'
    snake.run()
    assert snake.current_positions == [Cords(1,1),Cords(1,0)]

    display = Display('LEFT')
    snk.display_obj = display
    snake = Snake('fruit','wall')
    snake.current_positions = [Cords(1,1)]
    snake.orientation = 'up'
    snake.run()
    assert snake.last == 'LEFT'
    assert snake.current_positions == [Cords(1,1),Cords(0,1)]
    snake.current_positions = [Cords(1,1)]
    snake.orientation = 'right'
    snake.run()
    assert snake.current_positions == [Cords(1,1),Cords(1,0)]
    snake.current_positions = [Cords(1,1)]
    snake.orientation = 'down'
    snake.run()
    assert snake.current_positions == [Cords(1,1),Cords(2,1)]
    snake.current_positions = [Cords(1,1)]
    snake.orientation = 'left'
    snake.run()
    assert snake.current_positions == [Cords(1,1),Cords(1,2)]

def test_check_is_hit_fruit():
    #test True
    fruit = Fruit(True)
    snake = Snake(fruit,'wall')
    l = snake.lenght
    snake.current_positions = [Cords(1,1),Cords(2,2)]
    snake.is_hit_fruit()
    assert snake.lenght == l+1
    #test False
    fruit = Fruit(False)
    snake = Snake(fruit,'wall')
    snake.current_positions = [Cords(1,1),Cords(2,2)]
    l = snake.lenght
    snake.is_hit_fruit()
    assert snake.lenght == l

def test_display_snake():
    #when more than lenght
    display = Display()
    snk.display_obj = display
    snake = Snake('fruit','wall')
    snake.current_positions = [Cords(1,1),Cords(2,2),Cords(3,3),Cords(4,4)]
    snake.display_snake()
    assert display.order == ['display_char( ,1,1)','display_char(A,4,4)']
    #when less than lenght
    display = Display()
    snk.display_obj = display
    snake = Snake('fruit','wall')
    snake.current_positions = [Cords(1,1),Cords(4,4)]
    snake.display_snake()
    assert display.order == ['display_char(A,4,4)']

def test_check_is_in():
    snake = Snake('fruit','wall')
    snake.current_positions = [Cords(1,1),Cords(2,2),Cords(3,3),Cords(4,4)]
    assert snake.check_is_in() is False
    snake.current_positions = [Cords(1,1),Cords(4,4),Cords(3,3),Cords(4,4)]
    assert snake.check_is_in() is True