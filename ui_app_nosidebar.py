# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'app_nosidebarKikZuu.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

import new_icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(807, 615)
        MainWindow.setMinimumSize(QSize(800, 400))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setPointSize(8)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"*{\n"
"border:none;\n"
"padding:2px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QSize(500, 500))
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.ToolBar = QFrame(self.centralwidget)
        self.ToolBar.setObjectName(u"ToolBar")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.ToolBar.sizePolicy().hasHeightForWidth())
        self.ToolBar.setSizePolicy(sizePolicy1)
        self.ToolBar.setAutoFillBackground(False)
        self.ToolBar.setStyleSheet(u"background-color: #0db7ed;")
        self.ToolBar.setFrameShape(QFrame.StyledPanel)
        self.ToolBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.ToolBar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.Logo = QFrame(self.ToolBar)
        self.Logo.setObjectName(u"Logo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.Logo.sizePolicy().hasHeightForWidth())
        self.Logo.setSizePolicy(sizePolicy2)
        self.Logo.setMaximumSize(QSize(50, 70))
        self.Logo.setSizeIncrement(QSize(0, 0))
        self.Logo.setFrameShape(QFrame.StyledPanel)
        self.Logo.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.Logo)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(8, 6, 0, -1)
        self.logo_img = QLabel(self.Logo)
        self.logo_img.setObjectName(u"logo_img")
        self.logo_img.setMinimumSize(QSize(0, 0))
        self.logo_img.setMaximumSize(QSize(100, 70))
        font1 = QFont()
        font1.setPointSize(30)
        font1.setBold(True)
        self.logo_img.setFont(font1)
        self.logo_img.setStyleSheet(u"color:white;\n"
"\n"
"")
        self.logo_img.setPixmap(QPixmap(u"icons/grid.png"))
        self.logo_img.setScaledContents(True)
        self.logo_img.setWordWrap(False)
        self.logo_img.setMargin(0)
        self.logo_img.setIndent(-1)

        self.verticalLayout_2.addWidget(self.logo_img, 0, Qt.AlignLeft|Qt.AlignVCenter)


        self.horizontalLayout.addWidget(self.Logo)

        self.Icons = QFrame(self.ToolBar)
        self.Icons.setObjectName(u"Icons")
        sizePolicy1.setHeightForWidth(self.Icons.sizePolicy().hasHeightForWidth())
        self.Icons.setSizePolicy(sizePolicy1)
        self.Icons.setFrameShape(QFrame.StyledPanel)
        self.Icons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Icons)
        self.horizontalLayout_2.setSpacing(40)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.sidebar_icon = QFrame(self.Icons)
        self.sidebar_icon.setObjectName(u"sidebar_icon")
        self.sidebar_icon.setMaximumSize(QSize(190, 50))
        self.sidebar_icon.setCursor(QCursor(Qt.ArrowCursor))
        self.sidebar_icon.setStyleSheet(u"")
        self.sidebar_icon.setFrameShape(QFrame.StyledPanel)
        self.sidebar_icon.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.sidebar_icon)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.logo_name = QLabel(self.sidebar_icon)
        self.logo_name.setObjectName(u"logo_name")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.logo_name.sizePolicy().hasHeightForWidth())
        self.logo_name.setSizePolicy(sizePolicy3)
        self.logo_name.setMinimumSize(QSize(0, 0))
        self.logo_name.setMaximumSize(QSize(90, 16777215))
        font2 = QFont()
        font2.setPointSize(20)
        font2.setBold(True)
        self.logo_name.setFont(font2)
        self.logo_name.setStyleSheet(u"color:white;\n"
"")

        self.horizontalLayout_4.addWidget(self.logo_name)

        self.open_close_side_bar = QPushButton(self.sidebar_icon)
        self.open_close_side_bar.setObjectName(u"open_close_side_bar")
        self.open_close_side_bar.setMaximumSize(QSize(100, 16777215))
        self.open_close_side_bar.setCursor(QCursor(Qt.PointingHandCursor))
        self.open_close_side_bar.setStyleSheet(u"margin-left:35px")
        icon = QIcon()
        icon.addFile(u"icons/assets/left-arrow.png", QSize(), QIcon.Normal, QIcon.Off)
        self.open_close_side_bar.setIcon(icon)
        self.open_close_side_bar.setIconSize(QSize(30, 30))

        self.horizontalLayout_4.addWidget(self.open_close_side_bar)


        self.horizontalLayout_2.addWidget(self.sidebar_icon)

        self.control_icons = QFrame(self.Icons)
        self.control_icons.setObjectName(u"control_icons")
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.control_icons.sizePolicy().hasHeightForWidth())
        self.control_icons.setSizePolicy(sizePolicy4)
        self.control_icons.setMaximumSize(QSize(150, 50))
        self.control_icons.setFrameShape(QFrame.StyledPanel)
        self.control_icons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.control_icons)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 6, 0, 0)
        self.minimize = QPushButton(self.control_icons)
        self.minimize.setObjectName(u"minimize")
        self.minimize.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u"icons/assets/minus-free-icon-font.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize.setIcon(icon1)
        self.minimize.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.minimize, 0, Qt.AlignRight|Qt.AlignTop)

        self.expand = QPushButton(self.control_icons)
        self.expand.setObjectName(u"expand")
        self.expand.setCursor(QCursor(Qt.PointingHandCursor))
        self.expand.setStyleSheet(u"margin-right:15px;\n"
"margin-left:15px;")
        icon2 = QIcon()
        icon2.addFile(u"icons/assets/expand-arrows-free-icon-font.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.expand.setIcon(icon2)
        self.expand.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.expand, 0, Qt.AlignRight|Qt.AlignVCenter)

        self.out = QPushButton(self.control_icons)
        self.out.setObjectName(u"out")
        self.out.setCursor(QCursor(Qt.PointingHandCursor))
        self.out.setStyleSheet(u"margin-right: 5px")
        icon3 = QIcon()
        icon3.addFile(u"icons/assets/cross-free-icon-font.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.out.setIcon(icon3)
        self.out.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.out, 0, Qt.AlignRight|Qt.AlignTop)


        self.horizontalLayout_2.addWidget(self.control_icons, 0, Qt.AlignRight|Qt.AlignTop)


        self.horizontalLayout.addWidget(self.Icons)


        self.verticalLayout.addWidget(self.ToolBar)

        self.Body = QFrame(self.centralwidget)
        self.Body.setObjectName(u"Body")
        self.Body.setMinimumSize(QSize(500, 0))
        self.Body.setStyleSheet(u"background-color:#F0F1F3;\n"
"padding:0px;")
        self.Body.setFrameShape(QFrame.StyledPanel)
        self.Body.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.Body)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setSizeConstraint(QLayout.SetNoConstraint)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.Body)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 0))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.left_body = QFrame(self.frame)
        self.left_body.setObjectName(u"left_body")
        sizePolicy4.setHeightForWidth(self.left_body.sizePolicy().hasHeightForWidth())
        self.left_body.setSizePolicy(sizePolicy4)
        self.left_body.setMinimumSize(QSize(0, 0))
        self.left_body.setMaximumSize(QSize(220, 16777215))
        self.left_body.setStyleSheet(u"background-color:#384d54;")
        self.left_body.setFrameShape(QFrame.StyledPanel)
        self.left_body.setFrameShadow(QFrame.Raised)
        self.vboxLayout = QVBoxLayout(self.left_body)
        self.vboxLayout.setSpacing(0)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.vboxLayout.setContentsMargins(0, 0, 0, 0)
        self.choices = QFrame(self.left_body)
        self.choices.setObjectName(u"choices")
        self.choices.setMinimumSize(QSize(210, 0))
        self.choices.setMaximumSize(QSize(0, 16777215))
        self.choices.setFrameShape(QFrame.StyledPanel)
        self.choices.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.choices)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 22, 0, 0)
        self.home_button = QPushButton(self.choices)
        self.home_button.setObjectName(u"home_button")
        self.home_button.setMinimumSize(QSize(220, 70))
        self.home_button.setMaximumSize(QSize(220, 70))
        font3 = QFont()
        font3.setPointSize(16)
        font3.setBold(False)
        self.home_button.setFont(font3)
        self.home_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.home_button.setStyleSheet(u"QPushButton{\n"
"color:white;\n"
"padding-right:80px;\n"
"}\n"
"QPushButton::hover{\n"
"font-weight:bold;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u"icons/assets/home-free-icon-font.png", QSize(), QIcon.Normal, QIcon.Off)
        self.home_button.setIcon(icon4)
        self.home_button.setIconSize(QSize(30, 30))

        self.verticalLayout_4.addWidget(self.home_button, 0, Qt.AlignLeft|Qt.AlignTop)

        self.create_grid_button = QPushButton(self.choices)
        self.create_grid_button.setObjectName(u"create_grid_button")
        self.create_grid_button.setMinimumSize(QSize(220, 70))
        self.create_grid_button.setMaximumSize(QSize(220, 70))
        font4 = QFont()
        font4.setPointSize(16)
        self.create_grid_button.setFont(font4)
        self.create_grid_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.create_grid_button.setStyleSheet(u"QPushButton{\n"
"color:white;\n"
"\n"
"padding-right:35px;\n"
"}\n"
"QPushButton::hover{\n"
"font-weight:bold;\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u"icons/grid.png", QSize(), QIcon.Normal, QIcon.Off)
        self.create_grid_button.setIcon(icon5)
        self.create_grid_button.setIconSize(QSize(30, 30))

        self.verticalLayout_4.addWidget(self.create_grid_button, 0, Qt.AlignLeft|Qt.AlignTop)

        self.edit_grid_button = QPushButton(self.choices)
        self.edit_grid_button.setObjectName(u"edit_grid_button")
        self.edit_grid_button.setMinimumSize(QSize(170, 70))
        self.edit_grid_button.setMaximumSize(QSize(230, 70))
        self.edit_grid_button.setFont(font4)
        self.edit_grid_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.edit_grid_button.setStyleSheet(u"QPushButton{\n"
"color:white;\n"
"padding-right:50px;\n"
"}\n"
"QPushButton::hover{\n"
"font-weight:bold;\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u"icons/edit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.edit_grid_button.setIcon(icon6)
        self.edit_grid_button.setIconSize(QSize(30, 30))

        self.verticalLayout_4.addWidget(self.edit_grid_button)

        self.show_grid_button = QPushButton(self.choices)
        self.show_grid_button.setObjectName(u"show_grid_button")
        self.show_grid_button.setMinimumSize(QSize(0, 70))
        self.show_grid_button.setFont(font4)
        self.show_grid_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.show_grid_button.setStyleSheet(u"QPushButton{\n"
"color:white;\n"
"padding-right:1px;\n"
"padding-left:15px\n"
"}\n"
"QPushButton::hover{\n"
"font-weight:bold;\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u"icons/assets/time-fast-free-icon-font.png", QSize(), QIcon.Normal, QIcon.Off)
        self.show_grid_button.setIcon(icon7)
        self.show_grid_button.setIconSize(QSize(30, 30))

        self.verticalLayout_4.addWidget(self.show_grid_button, 0, Qt.AlignLeft)


        self.vboxLayout.addWidget(self.choices, 0, Qt.AlignTop)

        self.out_2 = QFrame(self.left_body)
        self.out_2.setObjectName(u"out_2")
        self.out_2.setMinimumSize(QSize(0, 70))
        self.out_2.setMaximumSize(QSize(16777215, 70))
        self.out_2.setFrameShape(QFrame.StyledPanel)
        self.out_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.out_2)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.exit_button = QPushButton(self.out_2)
        self.exit_button.setObjectName(u"exit_button")
        font5 = QFont()
        font5.setPointSize(15)
        self.exit_button.setFont(font5)
        self.exit_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.exit_button.setStyleSheet(u"QPushButton{\n"
"color:white;\n"
"padding-left: 15px;\n"
"padding-right:13px;\n"
"margin-right:5px;\n"
"}\n"
"QPushButton::hover{\n"
"font-weight:bold;\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u"icons/assets/sign-out-free-icon-font.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.exit_button.setIcon(icon8)
        self.exit_button.setIconSize(QSize(30, 30))

        self.horizontalLayout_7.addWidget(self.exit_button)


        self.vboxLayout.addWidget(self.out_2)


        self.horizontalLayout_6.addWidget(self.left_body)

        self.right_body = QFrame(self.frame)
        self.right_body.setObjectName(u"right_body")
        self.right_body.setFrameShape(QFrame.StyledPanel)
        self.right_body.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.right_body)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.stackedWidget = QStackedWidget(self.right_body)
        self.stackedWidget.setObjectName(u"stackedWidget")
        font6 = QFont()
        font6.setBold(False)
        font6.setKerning(False)
        self.stackedWidget.setFont(font6)
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.verticalLayout_5 = QVBoxLayout(self.home_page)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, 120, -1, -1)
        self.label_2 = QLabel(self.home_page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setEnabled(True)
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy5)
        self.label_2.setMinimumSize(QSize(270, 270))
        self.label_2.setMaximumSize(QSize(270, 270))
        font7 = QFont()
        font7.setPointSize(20)
        self.label_2.setFont(font7)
        self.label_2.setStyleSheet(u"margin-top:10px;\n"
"border:7px solid #0db7ed;\n"
"border-radius:100px;\n"
"padding: 30px;")
        self.label_2.setPixmap(QPixmap(u"icons/visualization.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setMargin(0)

        self.verticalLayout_5.addWidget(self.label_2, 0, Qt.AlignHCenter|Qt.AlignBottom)

        self.label = QLabel(self.home_page)
        self.label.setObjectName(u"label")
        self.label.setEnabled(False)
        self.label.setMinimumSize(QSize(182, 0))
        font8 = QFont()
        font8.setPointSize(35)
        font8.setBold(True)
        self.label.setFont(font8)
        self.label.setStyleSheet(u"color:#384d54;\n"
"margin-left:5px;\n"
"")

        self.verticalLayout_5.addWidget(self.label, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.stackedWidget.addWidget(self.home_page)
        self.create_grid = QWidget()
        self.create_grid.setObjectName(u"create_grid")
        self.verticalLayout_6 = QVBoxLayout(self.create_grid)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.grid_choices = QFrame(self.create_grid)
        self.grid_choices.setObjectName(u"grid_choices")
        self.grid_choices.setMinimumSize(QSize(450, 500))
        self.grid_choices.setMaximumSize(QSize(16777215, 16777215))
        self.grid_choices.setStyleSheet(u"#grid_choices{\n"
"border: 1px solid #384d54 ;\n"
"border-radius: 25px;\n"
"}")
        self.grid_choices.setFrameShape(QFrame.StyledPanel)
        self.grid_choices.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.grid_choices)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_5 = QFrame(self.grid_choices)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 220))
        self.frame_5.setStyleSheet(u"#frame_5{\n"
"border: 1px solid #384d54 ;\n"
"border-radius: 25px;\n"
"margin-bottom: 2px;\n"
"}")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_5)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.frame_8 = QFrame(self.frame_5)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_4 = QLabel(self.frame_8)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(200, 20))
        self.label_4.setSizeIncrement(QSize(100, 0))
        font9 = QFont()
        font9.setPointSize(15)
        font9.setBold(True)
        self.label_4.setFont(font9)
        self.label_4.setStyleSheet(u"padding:5px;\n"
"margin-left:15px;\n"
"color:#384d54 ;\n"
"margin-bottom: 3px;\n"
"")

        self.horizontalLayout_8.addWidget(self.label_4)


        self.verticalLayout_12.addWidget(self.frame_8, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.frame_9 = QFrame(self.frame_5)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_5 = QLabel(self.frame_9)
        self.label_5.setObjectName(u"label_5")
        font10 = QFont()
        font10.setPointSize(11)
        font10.setBold(True)
        self.label_5.setFont(font10)

        self.horizontalLayout_14.addWidget(self.label_5)

        self.lineEdit = QLineEdit(self.frame_9)
        self.lineEdit.setObjectName(u"lineEdit")
        font11 = QFont()
        font11.setPointSize(9)
        font11.setBold(True)
        self.lineEdit.setFont(font11)
        self.lineEdit.setStyleSheet(u"QLineEdit{\n"
"border: 2px solid #384d54 ;\n"
"border-radius:7px;\n"
"padding:1.2px;\n"
"color: black;\n"
"background-color:#384d54 ;\n"
"color: white;\n"
"}\n"
"QLineEdit::hover{\n"
"background-color:#42636E ;\n"
"\n"
"}")

        self.horizontalLayout_14.addWidget(self.lineEdit)


        self.verticalLayout_12.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.frame_5)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_6 = QLabel(self.frame_10)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font10)

        self.horizontalLayout_15.addWidget(self.label_6)

        self.lineEdit_2 = QLineEdit(self.frame_10)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        font12 = QFont()
        font12.setBold(True)
        self.lineEdit_2.setFont(font12)
        self.lineEdit_2.setStyleSheet(u"QLineEdit{\n"
"border: 2px solid #384d54 ;\n"
"border-radius:7px;\n"
"padding:1.2px;\n"
"color: black;\n"
"background-color:#384d54 ;\n"
"color: white;\n"
"}\n"
"QLineEdit::hover{\n"
"background-color:#42636E ;\n"
"\n"
"}")

        self.horizontalLayout_15.addWidget(self.lineEdit_2)


        self.verticalLayout_12.addWidget(self.frame_10)


        self.verticalLayout_11.addWidget(self.frame_5, 0, Qt.AlignTop)

        self.frame_7 = QFrame(self.grid_choices)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 200))
        self.frame_7.setStyleSheet(u"#frame_7{\n"
"border: 1px solid #384d54 ;\n"
"border-radius: 25px;\n"
"margin-top: 2px;\n"
"}")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_7)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_7 = QLabel(self.frame_7)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(200, 20))
        self.label_7.setSizeIncrement(QSize(100, 0))
        font13 = QFont()
        font13.setPointSize(16)
        font13.setBold(True)
        self.label_7.setFont(font13)
        self.label_7.setStyleSheet(u"\n"
"margin-left:15px;\n"
"\n"
"color:#384d54 ;\n"
"")

        self.verticalLayout_13.addWidget(self.label_7, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.frame_11 = QFrame(self.frame_7)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_8 = QLabel(self.frame_11)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font10)

        self.horizontalLayout_16.addWidget(self.label_8)

        self.lineEdit_3 = QLineEdit(self.frame_11)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setFont(font12)
        self.lineEdit_3.setStyleSheet(u"QLineEdit{\n"
"border: 2px solid #384d54 ;\n"
"border-radius:7px;\n"
"padding:1.2px;\n"
"color: black;\n"
"background-color:#384d54 ;\n"
"color: white;\n"
"}\n"
"QLineEdit::hover{\n"
"background-color:#42636E ;\n"
"\n"
"}")

        self.horizontalLayout_16.addWidget(self.lineEdit_3)


        self.verticalLayout_13.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.frame_7)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_9 = QLabel(self.frame_12)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font10)

        self.horizontalLayout_19.addWidget(self.label_9)

        self.lineEdit_4 = QLineEdit(self.frame_12)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setFont(font12)
        self.lineEdit_4.setStyleSheet(u"QLineEdit{\n"
"border: 2px solid #384d54 ;\n"
"border-radius:7px;\n"
"padding:1.2px;\n"
"color: black;\n"
"background-color:#384d54 ;\n"
"color: white;\n"
"}\n"
"QLineEdit::hover{\n"
"background-color:#42636E ;\n"
"\n"
"}")

        self.horizontalLayout_19.addWidget(self.lineEdit_4)


        self.verticalLayout_13.addWidget(self.frame_12)


        self.verticalLayout_11.addWidget(self.frame_7)

        self.frame_6 = QFrame(self.grid_choices)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(0, 30))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.pushButton = QPushButton(self.frame_6)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFont(font12)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"QPushButton{  \n"
"  border: 2px solid #0db7ed;\n"
"  border-radius:10px;\n"
"  background-color: #0595C3;\n"
"  color: white;\n"
"  font-size:19px;\n"
" margin-right:3px;\n"
"padding:6px;\n"
"}\n"
"QPushButton::hover{\n"
"  background-color: #0db7ed;\n"
"}")

        self.horizontalLayout_20.addWidget(self.pushButton)

        self.pushButton_4 = QPushButton(self.frame_6)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(0, 30))
        self.pushButton_4.setFont(font12)
        self.pushButton_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet(u"QPushButton{  \n"
"  border: 2px solid #0db7ed;\n"
"  border-radius:9px;\n"
"  background-color: #0595C3;\n"
"  color: white;\n"
"\n"
" margin-left:3px;\n"
"  font-size:19px;\n"
"padding:6px;\n"
"}\n"
"QPushButton::hover{\n"
"  background-color: #0db7ed;\n"
"}")

        self.horizontalLayout_20.addWidget(self.pushButton_4)


        self.verticalLayout_11.addWidget(self.frame_6, 0, Qt.AlignTop)


        self.verticalLayout_6.addWidget(self.grid_choices, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.stackedWidget.addWidget(self.create_grid)
        self.edit_grid = QWidget()
        self.edit_grid.setObjectName(u"edit_grid")
        self.verticalLayout_7 = QVBoxLayout(self.edit_grid)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.edit_frame = QFrame(self.edit_grid)
        self.edit_frame.setObjectName(u"edit_frame")
        self.edit_frame.setFrameShape(QFrame.StyledPanel)
        self.edit_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.edit_frame)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.frame_2 = QFrame(self.edit_frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"#x_table, #x_grid_label{\n"
"border:2px solid #384d54;\n"
"border-radius: 7px;\n"
"margin-bottom: 3px;\n"
"}\n"
"\n"
"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_2)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.x_grid_label = QLabel(self.frame_2)
        self.x_grid_label.setObjectName(u"x_grid_label")
        self.x_grid_label.setMinimumSize(QSize(0, 0))
        font14 = QFont()
        font14.setPointSize(17)
        font14.setBold(True)
        self.x_grid_label.setFont(font14)
        self.x_grid_label.setCursor(QCursor(Qt.PointingHandCursor))
        self.x_grid_label.setStyleSheet(u"QLabel{\n"
"color:white;\n"
"background-color:#0db7ed;\n"
"border-radius: 7px;\n"
"text-align: center;\n"
"}\n"
"QLabel::hover{\n"
"background-color:#4FCFF7;\n"
"}")

        self.verticalLayout_15.addWidget(self.x_grid_label, 0, Qt.AlignHCenter)

        self.x_table = QTableWidget(self.frame_2)
        self.x_table.setObjectName(u"x_table")
        self.x_table.setMinimumSize(QSize(300, 170))
        self.x_table.setMaximumSize(QSize(500, 16777215))
        font15 = QFont()
        font15.setPointSize(11)
        self.x_table.setFont(font15)
        self.x_table.setStyleSheet(u"border-radius: 0px;\n"
"")

        self.verticalLayout_15.addWidget(self.x_table, 0, Qt.AlignHCenter)


        self.verticalLayout_14.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.edit_frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"#y_table, #y_grid_label{\n"
"border:2px solid #384d54;\n"
"border-radius: 7px;\n"
"margin-bottom: 3px;\n"
"}\n"
"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_3)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.y_grid_label = QLabel(self.frame_3)
        self.y_grid_label.setObjectName(u"y_grid_label")
        self.y_grid_label.setFont(font14)
        self.y_grid_label.setCursor(QCursor(Qt.PointingHandCursor))
        self.y_grid_label.setStyleSheet(u"QLabel{\n"
"color:white;\n"
"background-color:#0db7ed;\n"
"border-radius: 7px;\n"
"}\n"
"QLabel::hover{\n"
"background-color:#4FCFF7;\n"
"}")

        self.verticalLayout_16.addWidget(self.y_grid_label, 0, Qt.AlignHCenter)

        self.y_table = QTableWidget(self.frame_3)
        self.y_table.setObjectName(u"y_table")
        self.y_table.setMinimumSize(QSize(300, 170))
        self.y_table.setMaximumSize(QSize(500, 16777215))
        self.y_table.setFont(font15)
        self.y_table.setStyleSheet(u"border-radius: 0px;")

        self.verticalLayout_16.addWidget(self.y_table, 0, Qt.AlignHCenter)


        self.verticalLayout_14.addWidget(self.frame_3)

        self.pushButton_2 = QPushButton(self.edit_frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet(u"QPushButton{  \n"
"  border: 2px solid #0db7ed;\n"
"  border-radius:9px;\n"
"  background-color: #0595C3;\n"
"  color: white;\n"
"margin-top: 3px;\n"
" margin-left:3px;\n"
"  font-size:19px;\n"
"\n"
"}\n"
"QPushButton::hover{\n"
"  background-color: #0db7ed;\n"
"}")

        self.verticalLayout_14.addWidget(self.pushButton_2, 0, Qt.AlignVCenter)


        self.verticalLayout_7.addWidget(self.edit_frame)

        self.stackedWidget.addWidget(self.edit_grid)
        self.show_grid = QWidget()
        self.show_grid.setObjectName(u"show_grid")
        self.verticalLayout_8 = QVBoxLayout(self.show_grid)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.show = QFrame(self.show_grid)
        self.show.setObjectName(u"show")
        self.show.setFrameShape(QFrame.StyledPanel)
        self.show.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.show)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_3 = QLabel(self.show)
        self.label_3.setObjectName(u"label_3")
        font16 = QFont()
        font16.setPointSize(13)
        self.label_3.setFont(font16)
        self.label_3.setStyleSheet(u"")

        self.verticalLayout_9.addWidget(self.label_3)


        self.verticalLayout_10.addLayout(self.verticalLayout_9)


        self.verticalLayout_8.addWidget(self.show)

        self.stackedWidget.addWidget(self.show_grid)
        self.upload_page = QWidget()
        self.upload_page.setObjectName(u"upload_page")
        self.horizontalLayout_18 = QHBoxLayout(self.upload_page)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.stackedWidget.addWidget(self.upload_page)

        self.verticalLayout_3.addWidget(self.stackedWidget)


        self.horizontalLayout_6.addWidget(self.right_body)


        self.horizontalLayout_5.addWidget(self.frame)


        self.verticalLayout.addWidget(self.Body)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.logo_img.setText("")
        self.logo_name.setText(QCoreApplication.translate("MainWindow", u"GRID", None))
        self.open_close_side_bar.setText("")
        self.minimize.setText("")
        self.expand.setText("")
        self.out.setText("")
        self.home_button.setText(QCoreApplication.translate("MainWindow", u"   Home", None))
        self.create_grid_button.setText(QCoreApplication.translate("MainWindow", u"  Create Grid", None))
        self.edit_grid_button.setText(QCoreApplication.translate("MainWindow", u"  Edit Grid", None))
        self.show_grid_button.setText(QCoreApplication.translate("MainWindow", u"  Show Grid", None))
        self.exit_button.setText(QCoreApplication.translate("MainWindow", u" Exit", None))
        self.label_2.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u" GRID SYSTEM", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Number Of Grid Lines", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"X-direction", None))
        self.lineEdit.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Y-direction", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"  Grid Spacing", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"X-direction", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Y-direction", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Ok", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.x_grid_label.setText(QCoreApplication.translate("MainWindow", u"X Grid Data", None))
        self.y_grid_label.setText(QCoreApplication.translate("MainWindow", u"Y Grid Data", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.label_3.setText("")
    # retranslateUi

