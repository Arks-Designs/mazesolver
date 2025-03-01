"""Module to house tests for the maze"""
import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m1._create_cells()
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_start_and_end_cells(self):
        num_cols = 2
        num_rows = 2
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        for _ in range(100):
            m1._create_cells()
            self.assertFalse(m1._cells[0][0].has_top_wall)
            self.assertFalse(m1._cells[-1][-1].has_bottom_wall)

    def test_outer_walls(self):
        num_cols = 3
        num_rows = 4
        m1 = Maze(0,0, num_rows, num_cols, 10, 10)
        m1._create_cells()
        for i in range(num_cols):
            if i != 0:
                self.assertTrue(m1._cells[i][0].has_top_wall)
            if i != num_cols - 1:
                self.assertTrue(m1._cells[i][-1].has_bottom_wall)
        for j in range(num_rows):
            self.assertTrue(m1._cells[0][j].has_left_wall)
            self.assertTrue(m1._cells[-1][j])

if __name__ == "__main__":
    unittest.main()
