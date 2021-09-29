from cords import Cords
from display import display_obj
from time import sleep

class Snake:
    def __init__(self, fruit,wall) -> None:
        self.current_positions = []
        self.lenght = 1
        self.last = 'RIGHT'
        self.fruit = fruit
        self.wall = wall

    def create(self, starting_cords):
        self.current_positions.append(starting_cords)

    def run(self):
        opposite = {'RIGHT':'LEFT','LEFT':'RIGHT', 'UP':'DOWN','DOWN':'UP'}
        arrow = display_obj.get_arrow()
        if arrow == 'none' or arrow == opposite[self.last]:
            arrow = self.last
        if arrow == 'end':
            return 'a'
        if arrow == 'RIGHT':
            self.last = 'RIGHT'
            self.current_positions.append(Cords(self.current_positions[-1].x+1, self.current_positions[-1].y))
        elif arrow == 'LEFT':
            self.last = 'LEFT'
            self.current_positions.append(Cords(self.current_positions[-1].x-1, self.current_positions[-1].y))
        elif arrow == 'UP':
            self.last = 'UP'
            self.current_positions.append(Cords(self.current_positions[-1].x, self.current_positions[-1].y-1))
        elif arrow == 'DOWN':
            self.last = 'DOWN'
            self.current_positions.append(Cords(self.current_positions[-1].x, self.current_positions[-1].y+1))
        if self.wall.check_in_wall(self.current_positions[-1]):
            return 'a' 
        if self.fruit.is_hit(self.current_positions[-1]):
            self.lenght += 1
        if self.lenght < len(self.current_positions):
            display_obj.display_char(' ', self.current_positions.pop(0))
        display_obj.display_char('A', self.current_positions[-1])
        if self.check_is_in():
            return 'a'
        sleep(0.2)

    def check_is_in(self):
        if self.current_positions[-1] in self.current_positions[:-1]:
            return True
        return False