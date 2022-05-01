import sys
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import Qt
from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QMainWindow


class Grid(QMainWindow):
    def __init__(self,width=700,height=700,num_of_x_lines=28,num_of_y_lines=28,x_spacing=25,y_spacing=25):
        super().__init__()
        # initiate the required variables
        self.width = width
        self.height = height
        self.num_of_x_lines = num_of_x_lines
        self.num_of_y_lines = num_of_y_lines
        self.x_spacing = x_spacing
        self.y_spacing = y_spacing

        # create the place on which the grid will be shown
        self.label = QtWidgets.QLabel()
        canvas = QPixmap(5000, 5000)
        canvas.fill("#384d54")
        self.label.setPixmap(canvas)
        self.setCentralWidget(self.label)

        # draw the grid


    def draw_grid(self):
        # create a painter
        painter = QtGui.QPainter()
        painter.begin(self.label.pixmap())
        print(painter)

        # create the pen
        pen = QtGui.QPen()
        print(pen)
        pen.setWidth(2)
        pen.setColor(QtGui.QColor("white"))
        # add the pen to the painter
        painter.setPen(pen)
        painter.drawEllipse(0, 0, 100, 100)
        # self.ui.grid_layout.addWidget(painter)
        for i in range(0, self.num_of_x_lines * self.x_spacing, self.x_spacing):
            if self.num_of_x_lines * self.x_spacing > self.width:
                print("The required number of grids cannot be drawn with that x_spacing ")
                break
            painter.drawLine(i, 0, i, self.height)

        for i in range(0, self.num_of_y_lines * self.y_spacing, self.y_spacing):
            if self.num_of_y_lines * self.y_spacing > self.height:
                print("The required number of grids cannot be drawn with that x_spacing ")
                break
            painter.drawLine(0, i, self.width, i)

        painter.end()


app = QtWidgets.QApplication(sys.argv)
window = Grid()
window.show()
window.draw_grid()
app.exec_()
