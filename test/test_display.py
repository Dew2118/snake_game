from src.display import Display
from src.cords import Cords
from src import display as ds
#mock
class Stdscr:
    def __init__(self, getch_input = None) -> None:
        self.order = []
        self.getch_input = getch_input
    
    def nodelay(self, num):
        self.order.append(f'nodelay({num})')

    def addstr(self, y, x, str):
        self.order.append(f'addstr({y},{x},{str})')

    def refresh(self):
        self.order.append('refresh')

    def keypad(self, c):
        self.order.append(f'keypad({c})')
    
    def getch(self):
        self.order.append('getch')
        return self.getch_input

class Curses_mock:
    KEY_RIGHT = 9
    KEY_LEFT = 11
    def __init__(self) -> None:
        self.order = []
    
    def cbreak(self):
        self.order.append('cbreak')
    
    def noecho(self):
        self.order.append('noecho')
    def curs_set(self, num):
        self.order.append(f'curs_set({num})')

def test_Display():
    curses = Curses_mock()
    stdscr = Stdscr()
    ds.curses = curses
    Display(stdscr)
    assert curses.order == ['cbreak','noecho','curs_set(0)']
    assert stdscr.order == ['nodelay(1)']

def test_display_char():
    curses = Curses_mock()
    stdscr = Stdscr()
    ds.curses = curses
    Display(stdscr).display_char('a',Cords(2,1))
    assert stdscr.order == ['nodelay(1)','addstr(1,2,a)','refresh']

def test_get_arrow():
    c = Curses_mock()
    ds.curses =  c
    stdscr = Stdscr(-1)
    assert Display(stdscr).get_arrow() == 'none'
    assert stdscr.order == ['nodelay(1)','keypad(True)','getch']
    stdscr = Stdscr(113)
    assert Display(stdscr).get_arrow() == 'end'
    assert stdscr.order == ['nodelay(1)','keypad(True)','getch']
    stdscr = Stdscr(9)
    assert Display(stdscr).get_arrow() == 'RIGHT'
    assert stdscr.order == ['nodelay(1)','keypad(True)','getch']
    stdscr = Stdscr(11)
    assert Display(stdscr).get_arrow() == 'LEFT'
    assert stdscr.order == ['nodelay(1)','keypad(True)','getch']
