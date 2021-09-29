from cords import Cords
from random import randint
from display import display_obj
class Fruit:
    def __init__(self, wall) -> None:
        self.fruit_position =  None
        self.wall = wall
        
    def create(self):
        x = randint(0,self.wall.y2-1)
        y = randint(0,self.wall.x2-1)
        if self.fruit_position is not None:
            display_obj.display_char(' ',self.fruit_position)
        self.fruit_position = Cords(x,y)
    
    def display(self):
        display_obj.display_char('P',self.fruit_position)

    def is_hit(self,current_position):
        if current_position == self.fruit_position:
            self.create()
            return True
        return False