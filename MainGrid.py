import sys
import os

import PySide6

########################################################################
# IMPORT GUI FILE
from qpaint_event import Grid
from ui_app_nosidebar import *
########################################################################
from PySide6.QtWidgets import QMainWindow
from PySide6 import *
from PySide6.QtCore import *

class MainApp(QMainWindow):
    def __init__(self):
        self.y_spacing = None
        self.animation = None
        self.x_spacing = None
        self.num_of_y_lines = None
        self.num_of_x_lines = None
        self.label = None
        self.grid_height = None
        self.grid_width = None
        self.app = QApplication(sys.argv)
        super(MainApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.setGeometry(650, 450, 900, 900)


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

        self.ui.show_grid_button.clicked.connect(self.edit_grid)
        self.createWindow()



    ###############################################################
    # Grid creation
    ###############################################################

    def create_grid(self, width=800, height=800, num_of_x_lines=28, num_of_y_lines=28, x_spacing=25, y_spacing=25):
        pass
        '''
        # create the place on which the grid will be shown
        self.label = QtWidgets.QLabel()
        canvas = QtGui.QPixmap(width, height)
        canvas.fill(Qt.white)
        self.label.setPixmap(canvas)
        # self.setCentralWidget(self.label)'''

    def edit_grid(self):
        pass


    def show_grid(self, width=800, height=800, num_of_x_lines=28, num_of_y_lines=28, x_spacing=25, y_spacing=25):
        pass
        '''self.grid_width = width
        self.grid_height = height
        self.num_of_x_lines = num_of_x_lines
        self.num_of_y_lines = num_of_y_lines
        self.x_spacing = x_spacing
        self.y_spacing = y_spacing

        # create the place on which the grid will be shown
        # self.label = QLabel()
        # self.ui.label_3.addWidget(self.label)
        print(self.ui.show_grid)
        print(type(self.ui.show_grid))

        # self.label.setPixmap(canvas)

        canvas = qpx6(5000,5000)
        canvas.fill("#384d54")
        print(self.ui.label_3.size())
        print(self.ui.show_grid.size())
        #self.ui.label_3.setMinimumSize(700,700)
        self.ui.label_3.setPixmap(canvas)
        painter = pqnt5(canvas)'''

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
