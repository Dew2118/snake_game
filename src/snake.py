from cords import Cords
from display import display_obj
from time import sleep

class Snake:
    def __init__(self, fruit,wall) -> None:
        self.current_positions = []
        self.lenght = 3
        self.last = 'RIGHT'
        self.fruit = fruit
        self.wall = wall
        self.orientation = 'right'

    def create(self, starting_cords):
        self.current_positions.append(starting_cords)

    def run(self):
        arrow = display_obj.get_arrow()
        if arrow == 'none':
            if self.orientation == 'up':
                self.current_positions.append(Cords(self.current_positions[-1].x, self.current_positions[-1].y-1))
            elif self.orientation == 'right':
                self.current_positions.append(Cords(self.current_positions[-1].x+1, self.current_positions[-1].y))
            elif self.orientation == 'down':
                self.current_positions.append(Cords(self.current_positions[-1].x, self.current_positions[-1].y+1))
            elif self.orientation == 'left':
                self.current_positions.append(Cords(self.current_positions[-1].x-1, self.current_positions[-1].y))
        if arrow == 'end':
            return 'a'
        if arrow == 'RIGHT':
            self.last = 'RIGHT'
            if self.orientation == 'up':
                self.current_positions.append(Cords(self.current_positions[-1].x+1, self.current_positions[-1].y))
                self.orientation = 'right'
            elif self.orientation == 'right':
                self.current_positions.append(Cords(self.current_positions[-1].x, self.current_positions[-1].y+1))
                self.orientation = 'down'
            elif self.orientation == 'down':
                self.current_positions.append(Cords(self.current_positions[-1].x-1, self.current_positions[-1].y))
                self.orientation = 'left'
            elif self.orientation == 'left':
                self.current_positions.append(Cords(self.current_positions[-1].x, self.current_positions[-1].y-1))
                self.orientation = 'up'
        elif arrow == 'LEFT':
            self.last = 'LEFT'
            if self.orientation == 'up':
                self.current_positions.append(Cords(self.current_positions[-1].x-1, self.current_positions[-1].y))
                self.orientation = 'left'
            elif self.orientation == 'left':
                self.current_positions.append(Cords(self.current_positions[-1].x, self.current_positions[-1].y+1))
                self.orientation = 'down'
            elif self.orientation == 'down':
                self.current_positions.append(Cords(self.current_positions[-1].x+1, self.current_positions[-1].y))
                self.orientation = 'right'
            elif self.orientation == 'right':
                self.current_positions.append(Cords(self.current_positions[-1].x, self.current_positions[-1].y-1))
                self.orientation = 'up'

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