from src.cords import Cords
def test_cords():
    c = Cords(1,2)
    assert c.x == 1
    assert c.y == 2