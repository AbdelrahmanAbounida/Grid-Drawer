import sys
import os
from qpaint_event import Grid
from PySide2 import *
import csv
########################################################################
# IMPORT GUI FILE
from PySide2 import QtGui
from PySide2.QtCore import *
from ui_app_nosidebar import *
from PySide2.QtGui import QPainter, QPixmap, QPen, QPaintDevice
# from PySide2 import QtGui

from PySide2 import QtWidgets
from PySide2.QtCore import QSize


########################################################################


class MainApp(QMainWindow):
    def __init__(self):
        self.y_spacing = 20
        self.x_spacing = 20
        self.num_of_y_lines = 40
        self.num_of_x_lines = 40
        self.x_spaces_list = []
        self.y_spaces_list = []

        self.animation = None
        self.label = None
        self.grid_height = None
        self.grid_width = None
        self.app = QApplication(sys.argv)
        super(MainApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.setGeometry(650, 450, 900, 900)
        ################### Create Table ######################
        self.create_table()
        ################### Remove window tittle bar ######################
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowMaximizeButtonHint)
        self.setIcon()

        ################### Set main background to transparent ###################
        self.setAttribute(Qt.WA_TranslucentBackground)

        ################### Shadow effect style ###################
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(50)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 92, 157, 550))

        ################### Appy shadow to central widget ###################
        self.ui.centralwidget.setGraphicsEffect(self.shadow)

        #################### Set window Icon ###################
        # This icon and title will not appear on our app main window because we removed the title bar
        self.setWindowIcon(QIcon(u"icons/analysis.png"))

        ################### Set window tittle ###################
        self.setWindowTitle("ANOM")

        ################### Minimize window ###################
        self.ui.minimize.clicked.connect(lambda: self.showMinimized())

        ################### Close window ###################
        self.ui.out.clicked.connect(lambda: self.close())
        self.ui.exit_button.clicked.connect(lambda: self.close())

        ################### Restore/Maximize window ###################
        self.ui.expand.clicked.connect(lambda: self.restore_or_maximize_window())

        # Function to Move window on mouse drag event on the tittle bar
        def moveWindow(e):
            # Detect if the window is  normal size
            # ###############################################
            if self.isMaximized() == False:  # Not maximized
                # Move window only when window is normal size
                # ###############################################
                # if left mouse button is clicked (Only accept left mouse button clicks)
                if e.buttons() == Qt.LeftButton:
                    # Move window
                    self.move(self.pos() + e.globalPosition().toPoint() - self.clickPosition)
                    self.clickPosition = e.globalPosition().toPoint()
                    e.accept()

        # Add click event/Mouse move event/drag event to the top header to move the window
        self.ui.ToolBar.mouseMoveEvent = moveWindow

        # Left Menu toggle button
        self.ui.open_close_side_bar.clicked.connect(lambda: self.slideLeftMenu())

        # Left Choices buttons
        # Home Button
        self.ui.home_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.home_page))
        # Create Grid
        self.ui.create_grid_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.create_grid))
        # Edit Grid
        self.ui.edit_grid_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.edit_grid))
        # Show Grid
        self.ui.show_grid_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.show_grid))

        self.ui.show_grid_button.clicked.connect(self.show_grid)

        # create grid ok
        self.ui.pushButton.clicked.connect(self.create_grid_ok)

        # create grid cancel
        self.ui.pushButton_4.clicked.connect(self.create_grid_cancel)

        # edit space ok
        self.ui.pushButton_2.clicked.connect(self.edit_grid_ok)
        self.createWindow()

    ###############################################################
    # TAble creation
    ###############################################################
    def create_table(self):
        self.ui.x_table.setColumnCount(2)
        self.ui.y_table.setColumnCount(2)
        self.ui.x_table.setHorizontalHeaderLabels(("Grid ID", "Ordinate"))
        self.ui.y_table.setHorizontalHeaderLabels(("Grid ID", "Ordinate"))
        self.ui.x_table.setColumnWidth(0, 127)
        self.ui.x_table.setColumnWidth(1, 127)
        self.ui.y_table.setColumnWidth(0, 127)
        self.ui.y_table.setColumnWidth(1, 127)

        self.ui.x_table.setRowCount(self.num_of_x_lines)
        self.ui.y_table.setRowCount(self.num_of_y_lines)

        # print(self.ui.x_table.item(0, 1).text())

    ###############################################################
    # Edit Table Ok
    ###############################################################
    def edit_grid_ok(self):
        self.update_grid()

    ###############################################################
    # Create Grid Ok
    ###############################################################

    def create_grid_ok(self):
        num_of_x_lines = self.ui.lineEdit.text()
        num_of_y_lines = self.ui.lineEdit_2.text()

        x_spacing = self.ui.lineEdit_3.text()
        y_spacing = self.ui.lineEdit_4.text()

        if not num_of_x_lines.isnumeric() or not num_of_y_lines.isnumeric() or not x_spacing.isnumeric() or not y_spacing.isnumeric():
            print("Please Enter numeric values")

        else:
            self.num_of_x_lines = int(num_of_x_lines)
            self.num_of_y_lines = int(num_of_y_lines)
            self.x_spacing = int(x_spacing)
            self.y_spacing = int(y_spacing)

        self.ui.x_table.setRowCount(self.num_of_x_lines)
        self.ui.y_table.setRowCount(self.num_of_y_lines)
        self.initiate_table()

    ###############################################################
    # initiate Table
    ###############################################################

    def initiate_table(self):

        # self.ui.x_table.setItem(0, 1, QTableWidgetItem('5'))
        x_counter = 0
        for i in range(0, self.num_of_x_lines * self.x_spacing, self.x_spacing):
            self.ui.x_table.setItem(x_counter, 0, QTableWidgetItem(str(x_counter)))
            self.ui.x_table.setItem(x_counter, 1, QTableWidgetItem(str(i)))
            x_counter = x_counter + 1

        y_counter = 0
        for j in range(0, self.num_of_y_lines * self.y_spacing, self.y_spacing):
            self.ui.y_table.setItem(y_counter, 0, QTableWidgetItem(str(y_counter)))
            self.ui.y_table.setItem(y_counter, 1, QTableWidgetItem(str(j)))
            y_counter = y_counter + 1

    def update_table(self):
        pass

    ###############################################################
    # Create Grid cancel
    ###############################################################

    def create_grid_cancel(self):
        self.ui.lineEdit.setText('')
        self.ui.lineEdit_2.setText('')
        self.ui.lineEdit_3.setText('')
        self.ui.lineEdit_4.setText('')

    ###############################################################
    # update grid
    ###############################################################

    def update_grid(self):
        x_spaces = []
        y_spaces = []
        for i in range(self.ui.x_table.rowCount()):
            x_spaces.append(self.ui.x_table.item(i, 1).text())

        for j in range(self.ui.y_table.rowCount()):
            y_spaces.append(self.ui.y_table.item(j, 1).text())
        self.x_spaces_list = x_spaces
        self.y_spaces_list = y_spaces
    ###############################################################
    # Grid creation
    ###############################################################

    def show_grid(self):
        if len(self.x_spaces_list) == 0 or len(self.y_spaces_list) == 0:
            self.update_grid()
        # scene = QGraphicsScene(self)
        self.ui.label_3 = Grid(self.num_of_x_lines, self.num_of_y_lines, self.x_spacing, self.y_spacing,
                               self.x_spaces_list,self.y_spaces_list)

    def edit_grid(self, width=800, height=800, num_of_x_lines=28, num_of_y_lines=28, x_spacing=25, y_spacing=25):
        pass
        '''self.grid_width = width
        self.grid_height = height
        self.num_of_x_lines = num_of_x_lines
        self.num_of_y_lines = num_of_y_lines
        self.x_spacing = x_spacing
        self.y_spacing = y_spacing

        canvas = QPixmap(5000, 5000)
        canvas.fill("#384d54")
        self.ui.label_3.setPixmap(canvas)

        # self.label.setPixmap(canvas)
        painter = QtGui.QPainter()
        painter.begin(self.ui.label_3)
        print(painter)

        # create the pen
        pen = QtGui.QPen()
        print(pen)
        pen.setWidth(2)
        pen.setColor(QtGui.QColor("green"))
        # add the pen to the painter
        painter.setPen(pen)
        painter.drawEllipse(100, 100, 100, 100)
        # self.ui.grid_layout.addWidget(painter)
        for i in range(0, self.num_of_x_lines * self.x_spacing, self.x_spacing):
            if self.num_of_x_lines * self.x_spacing > self.grid_width:
                print("The required number of grids cannot be drawn with that x_spacing ")
                break
            painter.drawLine(i, 0, i, self.grid_height)

        for i in range(0, self.num_of_y_lines * self.y_spacing, self.y_spacing):
            if self.num_of_y_lines * self.y_spacing > self.grid_height:
                print("The required number of grids cannot be drawn with that x_spacing ")
                break
            painter.drawLine(0, i, self.grid_width, i)

        painter.end()'''

        '''# create the pen
        pen = QPen()
        pen.setWidth(2)
        pen.setColor(QColor("black"))
        # add the pen to the painter
        painter.setPen(pen)
        # use the pen to draw the grid
        for i in range(0, self.num_of_x_lines * self.x_spacing, self.x_spacing):
            if self.num_of_x_lines * self.x_spacing > self.grid_width:
                print("The required number of grids cannot be drawn with that x_spacing ")
                break

            painter.drawLine(i, 0, i, self.grid_height)

        for i in range(0, self.num_of_y_lines * self.y_spacing, self.y_spacing):
            if self.num_of_y_lines * self.y_spacing > self.grid_height:
                print("The required number of grids cannot be drawn with that x_spacing ")
                break
            painter.drawLine(0, i, self.grid_width, i)

        painter.end()'''

    ###############################################################
    # Update restore button icon on msximizing or minimizing window
    ###############################################################
    def restore_or_maximize_window(self):
        # If window is maxmized
        if self.isMaximized():
            self.showNormal()
            # Change Icon
            self.ui.expand.setIcon(QIcon(u"icons/assets/expand-arrows-free-icon-font.svg"))
        else:
            self.showMaximized()
            # Change Icon
            self.ui.expand.setIcon(QIcon(u"icons/minimize.png"))

    ########################################################################
    # Slide left menu function
    ########################################################################
    def slideLeftMenu(self):
        # Get current left menu width
        width = self.ui.left_body.width()

        # If minimized
        if width == 0:
            # Expand menu
            newWidth = 220
            self.ui.open_close_side_bar.setIcon(QIcon(u"icons/left-arrow.png"))
            self.ui.sidebar_icon.setMaximumWidth(190)
            self.ui.open_close_side_bar.setMaximumWidth(100)
            self.ui.logo_name.setMaximumWidth(100)
            self.ui.Logo.setMaximumWidth(50)

        # If maximized
        else:
            # Restore menu
            newWidth = 0
            self.ui.logo_name.setMaximumWidth(0)
            self.ui.Logo.setMaximumWidth(0)
            self.ui.open_close_side_bar.setIcon(QIcon(u"icons/align-justify-free-icon-font.png"))
            self.ui.sidebar_icon.setMaximumWidth(60)

        # Animate the transition
        self.animation = QPropertyAnimation(self.ui.left_body, b"maximumWidth")  # Animate minimumWidht
        self.animation.setDuration(200)
        self.animation.setStartValue(width)  # Start value is the current menu width
        self.animation.setEndValue(newWidth)  # end value is the new menu width
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()

    ########################################################################
    # show window
    ########################################################################
    def createWindow(self):
        self.show()
        sys.exit(self.app.exec())

    ########################################################################
    # set the application icon
    ########################################################################
    def setIcon(self):
        icon = QIcon('increasing.png')
        icon.addFile('../assets/increasing.png')
        self.setWindowIcon(icon)

    #######################################################################
    # Add mouse events to the window
    #######################################################################
    def mousePressEvent(self, event):
        # Get the current position of the mouse
        self.clickPosition = event.globalPosition().toPoint()
        # We will use this value to move the window


'''class Grid(QWidget):
    def __init__(self):
        super().__init__()

    def paintEvent(self, event):
        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawText(event, qp)
        qp.end()

def main():
        app = QApplication(sys.argv)
        demo = Grid()
        demo.show()
        sys.exit(app.exec())'''

if __name__ == '__main__':
    app = MainApp()
    # app.geometry().center()
