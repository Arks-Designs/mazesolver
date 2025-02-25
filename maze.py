"""Module to hold the actual maze class"""
from random import getrandbits
from time import sleep
from geometry import Cell

class Maze:
    """Maze class"""
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win,
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells = None

    def _create_cells(self)->None:
        """Creates the cells of the matrix"""
        self._cells = [[
            Cell(
                self.win,
                x1 = i * self.cell_size_x + self.x1,
                x2 = i * self.cell_size_x + self.cell_size_x + self.x1,
                y1 = j * self.cell_size_y + self.y1,
                y2 = j * self.cell_size_y + self.cell_size_y + self.y1,
                has_bottom_wall = bool(getrandbits(1)),
                has_top_wall = bool(getrandbits(1)),
                has_left_wall = bool(getrandbits(1)),
                has_right_wall = bool(getrandbits(1))
            ) for j in range(self.num_rows)
        ] for i in range(self.num_cols)]

    def _draw_cells(self)->None:
        """Draws the cells of the matrix"""
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._cells[i][j].draw()
                self._animate()

    def _animate(self)->None:
        """Sleep to make the drawing of cells slower"""
        self.win.redraw()
        sleep(0.05)
