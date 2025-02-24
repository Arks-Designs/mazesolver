from window import Window
from geometry import Point, Line, Cell

def main():
    win = Window(800,600)

    # Test lines
    c = Cell(
        win,
        True,
        True,
        True,
        True,
        10,
        50,
        10,
        50
    )

    c2 = Cell(
        win,
        True,
        True,
        True,
        True,
        50,
        90,
        10,
        50
    )

    c3 = Cell(
        win,
        True,
        True,
        True,
        True,
        10,
        50,
        50,
        90
    )

    c4 = Cell(
        win,
        True,
        True,
        True,
        True,
        50,
        90,
        50,
        90
    )

    c5 = Cell(
        win,
        False,
        False,
        False,
        False,
        764,
        767,
        580,
        584
    )

    c.draw()
    c2.draw()
    c3.draw()
    c4.draw()
    c5.draw()
    c.draw_move(c2, True)
    c.draw_move(c3, False)
    c.draw_move(c4)
    c.draw_move(c5)

    win.wait_for_close()

if __name__ == "__main__":
    main()
