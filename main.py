from window import Window
from maze import Maze
from geometry import Point, Line, Cell

def main():
    win = Window(1500,900)

    #Test maze
    m = Maze(10, 10, 15, 24, 50, 50, win)
    m._create_cells()
    m._draw_cells()

    win.wait_for_close()

if __name__ == "__main__":
    main()
