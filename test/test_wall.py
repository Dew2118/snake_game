from src.wall import Wall
import src.wall as wl
from src.cords import Cords
#mock
class Display:
    def __init__(self) -> None:
        self.order = []
    
    def display_char(self,char,cords):
        self.order.append(f'display_char({char},{cords.x},{cords.y})')

def test_show_wall():
    wall = Wall()
    display = Display()
    wl.display_obj = display
    wall.show_wall()
    assert display.order == [f'display_char(#,40,{a})' for a in range(0,20)]+[f'display_char(#,{a},20)' for a in range(0,40)]

def test_in_wall():
    wall = Wall()
    assert wall.check_in_wall(Cords(0,19)) is False
    assert wall.check_in_wall(Cords(0,20)) is True
    assert wall.check_in_wall(Cords(0,-1)) is True
    assert wall.check_in_wall(Cords(39,0)) is False
    assert wall.check_in_wall(Cords(40,0)) is True
    assert wall.check_in_wall(Cords(-1,0)) is True