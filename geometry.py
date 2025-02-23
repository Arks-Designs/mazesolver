"""Module for geometry"""
from tkinter import Canvas

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
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