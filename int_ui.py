# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'V3.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 800)
        MainWindow.setMinimumSize(QtCore.QSize(1280, 800))
        MainWindow.setMaximumSize(QtCore.QSize(1280, 800))
        MainWindow.setStyleSheet("background-color:#f5f1ed;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.VBat = QtWidgets.QProgressBar(self.centralwidget)
        self.VBat.setGeometry(QtCore.QRect(1209, 1, 71, 23))
        self.VBat.setStyleSheet("QProgressBar {\n"
"    border: 1px solid grey;\n"
"    border-color: #30323d;\n"
"    border-radius: 4px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #64B64C;\n"
"    width: 10px;\n"
"    margin: 0.5px;\n"
"    border-radius: 2px;\n"
"}")
        self.VBat.setProperty("value", 24)
        self.VBat.setObjectName("VBat")
        self.NavData = QtWidgets.QGroupBox(self.centralwidget)
        self.NavData.setGeometry(QtCore.QRect(930, 50, 321, 300))
        self.NavData.setStyleSheet("QGroupBox {\n"
"    border: 2px solid gray;\n"
"    border-color : #2a2d34;\n"
"    border-radius: 5px;\n"
"    margin-top: 9px;\n"
"    margin-bottom: 3px;\n"
"    font: 9pt \"Comic Sans MS\";\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    color:\"#508484\";\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding:0px;\n"
"}")
        self.NavData.setObjectName("NavData")
        self.Vx = QtWidgets.QGroupBox(self.NavData)
        self.Vx.setGeometry(QtCore.QRect(11, 51, 96, 60))
        self.Vx.setObjectName("Vx")
        self.lcdNumber_VX = QtWidgets.QLCDNumber(self.Vx)
        self.lcdNumber_VX.setGeometry(QtCore.QRect(10, 20, 70, 25))
        self.lcdNumber_VX.setObjectName("lcdNumber_VX")
        self.Vy = QtWidgets.QGroupBox(self.NavData)
        self.Vy.setGeometry(QtCore.QRect(113, 51, 95, 60))
        self.Vy.setObjectName("Vy")
        self.lcdNumber_VY = QtWidgets.QLCDNumber(self.Vy)
        self.lcdNumber_VY.setGeometry(QtCore.QRect(10, 20, 70, 25))
        self.lcdNumber_VY.setStyleSheet("")
        self.lcdNumber_VY.setObjectName("lcdNumber_VY")
        self.Vz = QtWidgets.QGroupBox(self.NavData)
        self.Vz.setGeometry(QtCore.QRect(214, 51, 96, 59))
        self.Vz.setObjectName("Altitude")
        self.lcdNumber_VZ = QtWidgets.QLCDNumber(self.Vz)
        self.lcdNumber_VZ.setGeometry(QtCore.QRect(10, 20, 70, 25))
        self.lcdNumber_VZ.setObjectName("lcdNumber_VZ")
        self.Phi_GB = QtWidgets.QGroupBox(self.NavData)
        self.Phi_GB.setGeometry(QtCore.QRect(113, 116, 95, 60))
        self.Phi_GB.setObjectName("Phi_GB")
        self.lcdNumber_Phi = QtWidgets.QLCDNumber(self.Phi_GB)
        self.lcdNumber_Phi.setGeometry(QtCore.QRect(10, 20, 70, 25))
        self.lcdNumber_Phi.setObjectName("lcdNumber_Phi")
        self.Theta_GB = QtWidgets.QGroupBox(self.NavData)
        self.Theta_GB.setGeometry(QtCore.QRect(11, 116, 96, 60))
        self.Theta_GB.setObjectName("Theta_GB")
        self.lcdNumber_Theta = QtWidgets.QLCDNumber(self.Theta_GB)
        self.lcdNumber_Theta.setGeometry(QtCore.QRect(10, 20, 70, 25))
        self.lcdNumber_Theta.setObjectName("lcdNumber_Theta")
        self.Psi_GB = QtWidgets.QGroupBox(self.NavData)
        self.Psi_GB.setGeometry(QtCore.QRect(214, 116, 96, 60))
        self.Psi_GB.setObjectName("Psi_GB")
        self.lcdNumber_Psi = QtWidgets.QLCDNumber(self.Psi_GB)
        self.lcdNumber_Psi.setGeometry(QtCore.QRect(10, 20, 70, 25))
        self.lcdNumber_Psi.setObjectName("lcdNumber_Psi")
        self.DroneState_GB = QtWidgets.QGroupBox(self.NavData)
        self.DroneState_GB.setGeometry(QtCore.QRect(10, 190, 300, 70))
        self.DroneState_GB.setObjectName("DroneState_GB")
        self.lcdNumber_DroneState = QtWidgets.QLCDNumber(self.DroneState_GB)
        self.lcdNumber_DroneState.setGeometry(QtCore.QRect(10, 21, 280, 35))
        self.lcdNumber_DroneState.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lcdNumber_DroneState.setStyleSheet("")
        self.lcdNumber_DroneState.setSmallDecimalPoint(False)
        self.lcdNumber_DroneState.setDigitCount(33)
        self.lcdNumber_DroneState.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_DroneState.setProperty("value", 0.0)
        self.lcdNumber_DroneState.setProperty("intValue", 0)
        self.lcdNumber_DroneState.setObjectName("lcdNumber_DroneState")
        self.Camera = QtWidgets.QGroupBox(self.centralwidget)
        self.Camera.setGeometry(QtCore.QRect(30, 50, 365, 293))
        self.Camera.setStyleSheet("QGroupBox {\n"
"    border: 2px solid gray;\n"
"    border-color : #2a2d34;\n"
"    border-radius: 5px;\n"
"    margin-top: 9px;\n"
"    margin-bottom: 3px;\n"
"    font: 9pt \"Comic Sans MS\";\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    color:\"#508484\";\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding:0px;\n"
"}")
        self.Camera.setObjectName("Camera")
        self.Camera_label = QtWidgets.QLabel(self.Camera)
        self.Camera_label.setGeometry(QtCore.QRect(10, 20, 345, 260))
        self.Camera_label.setFrameShape(QtWidgets.QFrame.Box)
        self.Camera_label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Camera_label.setLineWidth(1)
        self.Camera_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Camera_label.setObjectName("Camera_label")
        self.DroneCAM = QtWidgets.QGroupBox(self.centralwidget)
        self.DroneCAM.setGeometry(QtCore.QRect(30, 370, 365, 229))
        self.DroneCAM.setStyleSheet("QGroupBox {\n"
"    border: 2px solid gray;\n"
"    border-color : #2a2d34;\n"
"    border-radius: 5px;\n"
"    margin-top: 9px;\n"
"    margin-bottom: 3px;\n"
"    font: 9pt \"Comic Sans MS\";\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    color:\"#508484\";\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding:0px;\n"
"}")
        self.DroneCAM.setObjectName("DroneCAM")
        self.DroneCAM_label = QtWidgets.QLabel(self.DroneCAM)
        self.DroneCAM_label.setGeometry(QtCore.QRect(10, 20, 345, 196))
        self.DroneCAM_label.setFrameShape(QtWidgets.QFrame.Box)
        self.DroneCAM_label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.DroneCAM_label.setLineWidth(1)
        self.DroneCAM_label.setAlignment(QtCore.Qt.AlignCenter)
        self.DroneCAM_label.setObjectName("DroneCAM_label")
        self.Animations = QtWidgets.QGroupBox(self.centralwidget)
        self.Animations.setGeometry(QtCore.QRect(480, 50, 365, 293))
        self.Animations.setStyleSheet("QGroupBox {\n"
"    border: 2px solid gray;\n"
"    border-color : #2a2d34;\n"
"    border-radius: 5px;\n"
"    margin-top: 9px;\n"
"    margin-bottom: 3px;\n"
"    font: 9pt \"Comic Sans MS\";\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    color:#508484;\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding:0px;\n"
"}")
        self.Animations.setObjectName("Animations")
        self.Animation_label = QtWidgets.QLabel(self.Animations)
        self.Animation_label.setGeometry(QtCore.QRect(10, 20, 345, 260))
        self.Animation_label.setStyleSheet("QGroupBox {\n"
"    border: 2px solid gray;\n"
"    border-radius: 5px;\n"
"    margin-top: 1px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    color:\"#FFFFFF\";\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding:3px;\n"
"}")
        self.Animation_label.setFrameShape(QtWidgets.QFrame.Box)
        self.Animation_label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Animation_label.setLineWidth(1)
        self.Animation_label.setMidLineWidth(0)
        self.Animation_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Animation_label.setObjectName("Animation_label")
        self.LastCom_label = QtWidgets.QLabel(self.Animations)
        self.LastCom_label.setGeometry(QtCore.QRect(20, 30, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.LastCom_label.setFont(font)
        self.LastCom_label.setStyleSheet("background-color:transparent;\n"
"font: 12pt \"Comic Sans MS\";\n"
"color: #17a398;\n"
"\n"
"")
        self.LastCom_label.setText("")
        self.LastCom_label.setObjectName("LastCom_label")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(480, 370, 365, 400))
        self.groupBox.setStyleSheet("QGroupBox {\n"
"    border: 2px solid gray;\n"
"    border-color : #2a2d34;\n"
"    border-radius: 5px;\n"
"    margin-top: 9px;\n"
"    margin-bottom: 3px;\n"
"    font: 9pt \"Comic Sans MS\";\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    color:\"#508484\";\n"
"    subcontrol-origin: margin;\n"
"    font: bold;\n"
"    subcontrol-position: top center;\n"
"    padding:0px;\n"
"}")
        self.groupBox.setObjectName("groupBox")
        self.DroneUP = QtWidgets.QPushButton(self.groupBox)
        self.DroneUP.setGeometry(QtCore.QRect(134, 34, 100, 40))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.DroneUP.setFont(font)
        self.DroneUP.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.DroneUP.setStyleSheet("QPushButton {\n"
"    background-color: #4d5061;\n"
"    color: #FFFFFF;\n"
"    border-style: outset;\n"
"    padding: 2px;\n"
"    font: bold 12px;\n"
"    border-width: 6px;\n"
"    border-radius: 10px;\n"
"    border-color: #30323d;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: #30323d;\n"
"    border-color: #4d5061;\n"
"}")
        self.DroneUP.setObjectName("DroneUP")
        self.DroneRight = QtWidgets.QPushButton(self.groupBox)
        self.DroneRight.setGeometry(QtCore.QRect(251, 121, 100, 40))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.DroneRight.setFont(font)
        self.DroneRight.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.DroneRight.setStyleSheet("QPushButton {\n"
"    background-color: #4d5061;\n"
"    color: #FFFFFF;\n"
"    border-style: outset;\n"
"    padding: 2px;\n"
"    font: bold 12px;\n"
"    border-width: 6px;\n"
"    border-radius: 10px;\n"
"    border-color: #30323d;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: #30323d;\n"
"    border-color: #4d5061;\n"
"}")
        self.DroneRight.setObjectName("DroneRight")
        self.DroneLeft = QtWidgets.QPushButton(self.groupBox)
        self.DroneLeft.setGeometry(QtCore.QRect(17, 121, 100, 40))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.DroneLeft.setFont(font)
        self.DroneLeft.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.DroneLeft.setStyleSheet("QPushButton {\n"
"    background-color: #4d5061;\n"
"    color: #FFFFFF;\n"
"    border-style: outset;\n"
"    padding: 2px;\n"
"    font: bold 12px;\n"
"    border-width: 6px;\n"
"    border-radius: 10px;\n"
"    border-color: #30323d;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: #30323d;\n"
"    border-color: #4d5061;\n"
"}")
        self.DroneLeft.setObjectName("DroneLeft")
        self.DroneDown = QtWidgets.QPushButton(self.groupBox)
        self.DroneDown.setGeometry(QtCore.QRect(134, 208, 100, 40))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.DroneDown.setFont(font)
        self.DroneDown.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.DroneDown.setStyleSheet("QPushButton {\n"
"    background-color: #4d5061;\n"
"    color: #FFFFFF;\n"
"    border-style: outset;\n"
"    padding: 2px;\n"
"    font: bold 12px;\n"
"    border-width: 6px;\n"
"    border-radius: 10px;\n"
"    border-color: #30323d;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: #30323d;\n"
"    border-color: #4d5061;\n"
"}")
        self.DroneDown.setObjectName("DroneDown")
        self.DroneHover = QtWidgets.QPushButton(self.groupBox)
        self.DroneHover.setGeometry(QtCore.QRect(134, 91, 100, 100))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.DroneHover.setFont(font)
        self.DroneHover.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.DroneHover.setStyleSheet("QPushButton {\n"
"    background-color: #4d5061;\n"
"    color: #FFFFFF;\n"
"    border-style: outset;\n"
"    padding: 2px;\n"
"    font: bold 12px;\n"
"    border-width: 6px;\n"
"    border-radius: 30px;\n"
"    border-color: #30323d;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: #30323d;\n"
"    border-color: #4d5061;\n"
"}")
        self.DroneHover.setObjectName("DroneHover")
        self.DroneEmergency = QtWidgets.QPushButton(self.groupBox)
        self.DroneEmergency.setGeometry(QtCore.QRect(104, 330, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.DroneEmergency.setFont(font)
        self.DroneEmergency.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.DroneEmergency.setStyleSheet("QPushButton {\n"
"    background-color: #9a031e ;\n"
"    color: #FFFFFF;\n"
"    border-style: outset;\n"
"    padding: 2px;\n"
"    font: bold 15px;\n"
"    border-width: 3px;\n"
"    border-radius: 10px;\n"
"    border-color: #823329;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:#4b7f52;\n"
"    border-color: #4a7c59;\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Assets/Emergency.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.DroneEmergency.setIcon(icon)
        self.DroneEmergency.setObjectName("DroneEmergency")
        self.DroneTakeoff = QtWidgets.QPushButton(self.groupBox)
        self.DroneTakeoff.setGeometry(QtCore.QRect(14, 257, 120, 60))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.DroneTakeoff.setFont(font)
        self.DroneTakeoff.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.DroneTakeoff.setStyleSheet("QPushButton {\n"
"    background-color: #4d5061;\n"
"    color: #FFFFFF;\n"
"    border-style: outset;\n"
"    padding: 2px;\n"
"    font: bold 12px;\n"
"    border-width: 6px;\n"
"    border-radius: 10px;\n"
"    border-color: #30323d;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: #30323d;\n"
"    border-color: #4d5061;\n"
"}")
        self.DroneTakeoff.setObjectName("DroneTakeoff")
        self.DroneLand = QtWidgets.QPushButton(self.groupBox)
        self.DroneLand.setGeometry(QtCore.QRect(234, 257, 120, 60))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.DroneLand.setFont(font)
        self.DroneLand.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.DroneLand.setStyleSheet("QPushButton {\n"
"    background-color: #4d5061;\n"
"    color: #FFFFFF;\n"
"    border-style: outset;\n"
"    padding: 2px;\n"
"    font: bold 12px;\n"
"    border-width: 6px;\n"
"    border-radius: 10px;\n"
"    border-color: #30323d;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: #30323d;\n"
"    border-color: #4d5061;\n"
"}")
        self.DroneLand.setObjectName("DroneLand")
        self.DroneBackward = QtWidgets.QPushButton(self.groupBox)
        self.DroneBackward.setGeometry(QtCore.QRect(17, 172, 100, 40))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.DroneBackward.setFont(font)
        self.DroneBackward.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.DroneBackward.setStyleSheet("QPushButton {\n"
"    background-color: #4d5061;\n"
"    color: #FFFFFF;\n"
"    border-style: outset;\n"
"    padding: 2px;\n"
"    font: bold 12px;\n"
"    border-width: 6px;\n"
"    border-radius: 10px;\n"
"    border-color: #30323d;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: #30323d;\n"
"    border-color: #4d5061;\n"
"}")
        self.DroneBackward.setObjectName("DroneBackward")
        self.DroneForward = QtWidgets.QPushButton(self.groupBox)
        self.DroneForward.setGeometry(QtCore.QRect(251, 70, 100, 40))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.DroneForward.setFont(font)
        self.DroneForward.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.DroneForward.setStyleSheet("QPushButton {\n"
"    background-color: #4d5061;\n"
"    color: #FFFFFF;\n"
"    border-style: outset;\n"
"    padding: 2px;\n"
"    font: bold 12px;\n"
"    border-width: 6px;\n"
"    border-radius: 10px;\n"
"    border-color: #30323d;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: #30323d;\n"
"    border-color: #4d5061;\n"
"}")
        self.DroneForward.setObjectName("DroneForward")
        self.DroneClockwise = QtWidgets.QPushButton(self.groupBox)
        self.DroneClockwise.setGeometry(QtCore.QRect(251, 172, 100, 40))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.DroneClockwise.setFont(font)
        self.DroneClockwise.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.DroneClockwise.setStyleSheet("QPushButton {\n"
"    background-color: #4d5061;\n"
"    color: #FFFFFF;\n"
"    border-style: outset;\n"
"    padding: 2px;\n"
"    font: bold 12px;\n"
"    border-width: 6px;\n"
"    border-radius: 10px;\n"
"    border-color: #30323d;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: #30323d;\n"
"    border-color: #4d5061;\n"
"}")
        self.DroneClockwise.setObjectName("DroneClockwise")
        self.DroneAntiClockwise = QtWidgets.QPushButton(self.groupBox)
        self.DroneAntiClockwise.setGeometry(QtCore.QRect(17, 70, 100, 40))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.DroneAntiClockwise.setFont(font)
        self.DroneAntiClockwise.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.DroneAntiClockwise.setStyleSheet("QPushButton {\n"
"    background-color: #4d5061;\n"
"    color: #FFFFFF;\n"
"    border-style: outset;\n"
"    padding: 2px;\n"
"    font: bold 12px;\n"
"    border-width: 6px;\n"
"    border-radius: 10px;\n"
"    border-color: #30323d;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: #30323d;\n"
"    border-color: #4d5061;\n"
"}")
        self.DroneAntiClockwise.setObjectName("DroneAntiClockwise")
        self.label_barre = QtWidgets.QLabel(self.centralwidget)
        self.label_barre.setGeometry(QtCore.QRect(0, 0, 1280, 25))
        self.label_barre.setStyleSheet("background-color:#30323d;")
        self.label_barre.setText("")
        self.label_barre.setObjectName("label_barre")
        self.label_Time = QtWidgets.QLabel(self.centralwidget)
        self.label_Time.setGeometry(QtCore.QRect(640, 4, 41, 16))
        self.label_Time.setStyleSheet("color:white;\n"
"background-color:transparent;\n"
"font: 9pt \"Comic Sans MS\";")
        self.label_Time.setText("")
        self.label_Time.setObjectName("label_Time")
        self.label_barre.raise_()
        self.VBat.raise_()
        self.NavData.raise_()
        self.Camera.raise_()
        self.DroneCAM.raise_()
        self.Animations.raise_()
        self.groupBox.raise_()
        self.label_Time.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.NavData.setTitle(_translate("MainWindow", "NavData"))
        self.Vx.setTitle(_translate("MainWindow", "Vx"))
        self.Vy.setTitle(_translate("MainWindow", "Vy"))
        self.Vz.setTitle(_translate("MainWindow", "Altitude"))
        self.Phi_GB.setTitle(_translate("MainWindow", "Phi"))
        self.Theta_GB.setTitle(_translate("MainWindow", "Theta"))
        self.Psi_GB.setTitle(_translate("MainWindow", "Psi"))
        self.DroneState_GB.setTitle(_translate("MainWindow", "Drone State"))
        self.Camera.setTitle(_translate("MainWindow", "Camera"))
        self.Camera_label.setText(_translate("MainWindow", "Camera"))
        self.DroneCAM.setTitle(_translate("MainWindow", "Drone\'s Camera"))
        self.DroneCAM_label.setText(_translate("MainWindow", "Drone\'s Camera"))
        self.Animations.setTitle(_translate("MainWindow", "Animations"))
        self.Animation_label.setText(_translate("MainWindow", "Animation"))
        self.groupBox.setTitle(_translate("MainWindow", "Command Center"))
        self.DroneUP.setText(_translate("MainWindow", "UP"))
        self.DroneUP.setShortcut(_translate("MainWindow", "Up"))
        self.DroneRight.setText(_translate("MainWindow", "RIGHT"))
        self.DroneRight.setShortcut(_translate("MainWindow", "Right"))
        self.DroneLeft.setText(_translate("MainWindow", "LEFT"))
        self.DroneLeft.setShortcut(_translate("MainWindow", "Left"))
        self.DroneDown.setText(_translate("MainWindow", "DOWN"))
        self.DroneDown.setShortcut(_translate("MainWindow", "Down"))
        self.DroneHover.setText(_translate("MainWindow", "HOVER"))
        self.DroneHover.setShortcut(_translate("MainWindow", "H"))
        self.DroneEmergency.setText(_translate("MainWindow", "Emergency"))
        self.DroneEmergency.setShortcut(_translate("MainWindow", "U"))
        self.DroneTakeoff.setText(_translate("MainWindow", "TAKE OFF"))
        self.DroneTakeoff.setShortcut(_translate("MainWindow", "T"))
        self.DroneLand.setText(_translate("MainWindow", "LAND"))
        self.DroneLand.setShortcut(_translate("MainWindow", "L"))
        self.DroneBackward.setText(_translate("MainWindow", "Backward"))
        self.DroneBackward.setShortcut(_translate("MainWindow", "B"))
        self.DroneForward.setText(_translate("MainWindow", "Forward"))
        self.DroneForward.setShortcut(_translate("MainWindow", "F"))
        self.DroneClockwise.setText(_translate("MainWindow", "Clockwise"))
        self.DroneClockwise.setShortcut(_translate("MainWindow", "C"))
        self.DroneAntiClockwise.setText(_translate("MainWindow", "Anti-Clockwise"))
        self.DroneAntiClockwise.setShortcut(_translate("MainWindow", "A"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
