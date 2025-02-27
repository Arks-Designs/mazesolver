"""Module to hold the actual maze class"""
from random import getrandbits, seed, choice
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
        win = None,
        rand_seed = None
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells = None
        if rand_seed:
            seed(rand_seed)

    def _create_cells(self)->None:
        """Creates the cells of the matrix"""
        self._cells = [[
            Cell(
                self.win,
                x1 = i * self.cell_size_x + self.x1,
                x2 = i * self.cell_size_x + self.cell_size_x + self.x1,
                y1 = j * self.cell_size_y + self.y1,
                y2 = j * self.cell_size_y + self.cell_size_y + self.y1,
                has_bottom_wall = True, #bool(getrandbits(1)),
                has_top_wall = True, #bool(getrandbits(1)),
                has_left_wall = True, #bool(getrandbits(1)),
                has_right_wall = True, #bool(getrandbits(1))
            ) for j in range(self.num_rows)
        ] for i in range(self.num_cols)]

        # Create border around the maze
        # Note this is no longer needed because of the switch to starting with 
        # a maze full of walls
        #self._fill_edges()

        # Remove top of top left cell (starting point)
        self._cells[0][0].has_top_wall = False

        # Remove bottom of bottom right cell (end point)
        self._cells[-1][-1].has_bottom_wall = False

        # Create path through the maze
        self._break_walls_r(0,0)

    def _draw_cells(self)->None:
        """Draws the cells of the matrix"""
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._cells[i][j].draw()
                self._animate()

    def _animate(self)->None:
        """Sleep to make the drawing of cells slower"""
        self.win.redraw()
        #sleep(0.05)

    def _break_walls_r(self, i, j):
        """Creates a path through the maze"""
        # Note i cooresponds to columns
        # j cooresponds to row
        # m._cells[i][j]
        # So m._cells[2][4] cooresponds to 2nd col, 4th row
        self._cells[i][j].visited = True

        while True:
            ij_list = []
            # Test top adjacent cell
            new_j = j - 1
            if new_j >= 0 and not self._cells[i][new_j].visited:
                ij_list.append((i, new_j))

            # Test bottom adjacent cell
            new_j = j + 1
            if new_j < self.num_rows and not self._cells[i][new_j].visited:
                ij_list.append((i, new_j))

            # Test left adjacent cell
            new_i = i - 1
            if new_i >= 0 and not self._cells[new_i][j].visited:
                ij_list.append((new_i, j))

            # Test right adjacent cell
            new_i = i + 1
            if new_i < self.num_cols and not self._cells[new_i][j].visited:
                ij_list.append((new_i, j))

            if len(ij_list) == 0:
                return

            direction = choice(ij_list)
            new_i, new_j = direction
            # Up
            if new_j < j:
                self._cells[i][j].has_top_wall = False
                self._cells[new_i][new_j].has_bottom_wall = False

            # Down
            elif new_j > j:
                self._cells[i][j].has_bottom_wall = False
                self._cells[new_i][new_j].has_top_wall = False

            # Left
            elif new_i < i:
                self._cells[i][j].has_left_wall = False
                self._cells[new_i][new_j].has_right_wall = False

            # Right
            elif new_i > i:
                self._cells[i][j].has_right_wall = False
                self._cells[new_i][new_j].has_left_wall = False

            self._break_walls_r(new_i, new_j)

    def _fill_edges(self):
        # Create borders around the maze
        for i in range(self.num_cols):
            self._cells[i][0].has_top_wall = True
            self._cells[i][-1].has_bottom_wall = True

        for j in range(self.num_rows):
            self._cells[0][j].has_left_wall = True
            self._cells[-1][j].has_right_wall = True
