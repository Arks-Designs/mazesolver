"""Module to create a window for use"""
from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        # Create the main window
        self.__root =  Tk()
        self.__root.title("Maze Solver")
        
        # Create canvas widget
        self.__canvas = Canvas(master=self.__root, height=height, width=width)
        self.__canvas.pack()

        # Set whether window is running
        self.running = False

        # Set protocol to delete stopped window
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self)->None:
        """Method to redraw graphics on the window"""
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self)->None:
        """Waits for the app to close"""
        self.running = True
        while self.running:
            self.redraw()

    def close(self)->None:
        """Sets running flag to false"""
        self.running = False