from display import display_obj
from cords import Cords
class Wall:
    def __init__(self) -> None:
        self.x2 = 20
        self.y2 = 40
    
    def show_wall(self):
        for a in range(0,40):
            display_obj.display_char('#',Cords(a,self.x2))
        for a in range(20):
            display_obj.display_char('#',Cords(self.y2,a))            
    
    def check_in_wall(self, cords):
        if cords.x == self.y2 or cords.y == self.x2:
            return True
        return False