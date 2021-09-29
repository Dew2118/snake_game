import sys
if 'pytest' not in sys.modules:
    from src.display import display_obj
from src.cords import Cords

class Wall:
    def __init__(self) -> None:
        self.x2 = 40
        self.y2 = 20
    
    def show_wall(self):
        for a in range(20):
            display_obj.display_char('#',Cords(self.x2,a))
        for a in range(40):
            display_obj.display_char('#',Cords(a,self.y2))            
    
    def check_in_wall(self, cords):
        if cords.x == self.x2 or cords.x < 0 or cords.y == self.y2 or cords.y < 0:
            return True
        return False