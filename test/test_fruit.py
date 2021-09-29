from src.fruit import Fruit
import src.fruit as frt
from src.cords import Cords
from src.wall import Wall
#mock
class Random:
    def __init__(self) -> None:
        self.order = []
    
    def randint(self,min, max):
        self.order.append(f'randint({min},{max})')
        return 1

class Wall_mock:
    def __init__(self) -> None:
        self.x2 = Wall().x2
        self.y2 = Wall().y2

class Display:
    def __init__(self) -> None:
        self.order = []
    
    def display_char(self,char,cords):
        self.order.append(f'display_char({char},{cords.x},{cords.y})')

def test_create():
    fruit = Fruit(Wall_mock())
    random = Random()
    display = Display()
    frt.randint = random.randint
    frt.display_obj = display
    #fruit_position is None
    fruit.create()
    assert random.order == ['randint(0,39)','randint(0,19)']
    assert fruit.fruit_position == Cords(1,1)
    #fruit_position is not None
    fruit.create()
    assert display.order == [f'display_char( ,1,1)']

def test_display():
    fruit = Fruit(Wall_mock())
    random = Random()
    display = Display()
    frt.display_obj = display
    fruit.fruit_position = Cords(1,1)
    fruit.display()
    assert display.order == [f'display_char(P,1,1)']

def test_is_hit():
    fruit = Fruit(Wall_mock())
    random = Random()
    display = Display()
    frt.randint = random.randint
    frt.display_obj = display    
    assert fruit.is_hit(Cords(5,2)) is False
    fruit.fruit_position = Cords(1,1)
    assert fruit.is_hit(Cords(1,1)) is True
    #the code will call Fruit.create()
    assert random.order == ['randint(0,39)','randint(0,19)']
    assert display.order == [f'display_char( ,1,1)']



    