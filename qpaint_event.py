from PySide6 import QtWidgets
from PySide6.QtGui import QPainter, QPen, QColor, QIcon
from PySide6.QtWidgets import QWidget
import sys


class Grid(QWidget):
    def __init__(self,num_of_x_lines,num_of_y_lines,x_spacing,y_spacing, x_spaces_list, y_spaces_list):
        super().__init__()
        self.setWindowTitle("Grid")
        self.setWindowIcon(QIcon("grid_logo.png"))
        self.num_of_x_lines = num_of_x_lines
        self.x_spacing = x_spacing
        self.num_of_y_lines = num_of_y_lines
        self.y_spacing = y_spacing
        self.x_spaces_list = x_spaces_list
        self.y_spaces_list = y_spaces_list

        self.width = 800
        self.height = 800
        self.show()

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        pen = QPen()
        pen.setWidth(2)
        pen.setColor("black")
        painter.setPen(pen)
        painter.fillRect(event.rect(),"white")

        for i in self.x_spaces_list:
            painter.drawLine(int(i), 0, int(i), self.height)
        for i in self.y_spaces_list:
            painter.drawLine(0, int(i), self.width, int(i))

        painter.end()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Grid()
    window.show()
    app.exec_()
