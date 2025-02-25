from window import Window
from maze import Maze
from geometry import Point, Line, Cell

def main():
    win = Window(800,600)

    #Test maze
    m = Maze(200, 200, 5, 7, 50, 50, win)
    m._create_cells()
    m._draw_cells()

    win.wait_for_close()

if __name__ == "__main__":
    main()
