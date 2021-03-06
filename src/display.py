from curses import wrapper
import curses
import sys
class Display:
    def __init__(self,stdscr) -> None:
        self.stdscr = stdscr
        self.stdscr.nodelay(1)
        curses.cbreak()
        curses.noecho()
        curses.curs_set(0)

    def display_char(self, char, cords):
        try:
            self.stdscr.addstr(cords.y, cords.x, char)
            self.stdscr.refresh()
        except Exception:
            return

    def get_arrow(self):
        self.stdscr.keypad(True)
        char = self.stdscr.getch()
        if char == -1:
            return 'none'
        if char == 113: 
            return 'end'
        elif char == curses.KEY_RIGHT: 
            return 'RIGHT'
        elif char == curses.KEY_LEFT: 
            return 'LEFT'
if 'pytest' not in sys.modules:
    display_obj = wrapper(Display)