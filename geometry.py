"""Module for geometry"""
from tkinter import Canvas

class Point:
    """Class to locate a point on the canvas"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    """Class that represents a line"""
    def __init__(self, point1, point2):
        self.__point1 = point1
        self.__point2 = point2

    def draw(self, canvas:Canvas, fill_color:str)->None:
        """Function to draw the line"""
        canvas.create_line(
            self.__point1.x,
            self.__point1.y,
            self.__point2.x,
            self.__point2.y,
            fill = fill_color,
            width = 2
            )

class Cell:
    """Class that represents one block in the maze"""
    def __init__(
            self,
            window, 
            has_left_wall = False,
            has_right_wall = False,
            has_top_wall = False,
            has_bottom_wall = False,
            x1 = 0,
            x2 = 0,
            y1 = 0,
            y2 = 0
            ):
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2
        self.__win = window

    def draw(self)->None:
        """Method to draw a cell"""
        cell_wall_color = "yellow"
        if self.has_left_wall:
            left_line = Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2))
            self.__win.draw_line(left_line, cell_wall_color)

        if self.has_right_wall:
            right_line = Line(Point(self.__x2, self.__y1), Point(self.__x2, self.__y2))
            self.__win.draw_line(right_line, cell_wall_color)

        if self.has_top_wall:
            top_line = Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1))
            self.__win.draw_line(top_line, cell_wall_color)

        if self.has_bottom_wall:
            bottom_line = Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2))
            self.__win.draw_line(bottom_line, cell_wall_color)

    def draw_move(self, to_cell:"Cell", undo:bool = False)->None:
        """Draw a line between two cells"""
        mid_x_from = round((self.__x1 + self.__x2) / 2, 0)
        mid_x_to = round((to_cell.__x1 + to_cell.__x2) / 2, 0)
        mid_y_from = round((self.__y1 + self.__y2) / 2, 0)
        mid_y_to = round((to_cell.__y1 + to_cell.__y2) / 2, 0)
        line_between = Line(
            Point(mid_x_from, mid_y_from),
            Point(mid_x_to, mid_y_to)
        )

        color_match = {False: "red", True: "gray"}
        self.__win.draw_line(line_between, color_match[undo])
