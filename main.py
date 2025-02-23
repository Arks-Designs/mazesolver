from window import Window
from geometry import Point, Line

def main():
    win = Window(800,600)

    # Test lines
    point_1 = Point(0, 0)
    point_2 = Point(700, 500)
    line_1 = Line(point_1, point_2)
    win.draw_line(line_1, "red")

    point_1 = Point(500, 2)
    point_2 = Point(150, 450)
    line_1 = Line(point_1, point_2)
    win.draw_line(line_1, "blue")


    win.wait_for_close()

if __name__ == "__main__":
    main()
