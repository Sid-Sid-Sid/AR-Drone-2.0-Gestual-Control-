from int_ui import *
from BackgroundProcess import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import (QApplication, QWidget, QMessageBox)
import cv2
import os

# Set a communication with the drone's video PORT with TCP/IP Protocol
cam = cv2.VideoCapture('tcp://192.168.1.1:5555')

SPEED = 0.4

from pyardrone import ARDrone,at

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    Navdata_file = open(r"C:\Users\Sid\Documents\Sid Project's\PFE\donnees.txt", 'w')

# Drone Initialisation 
    drone = ARDrone()

# Wait for NavData
    drone.navdata_ready.wait()

# Send an AT command to the drone to receive Navdata
    drone.send(at.CONFIG('general:navdata_demo', True))

# Drone Commands Functions: 

    def _DroneTakeOff():
        ui.LastCom_label.setText("Take Off")
        ui.LastCom_label.setStyleSheet("font: 12pt \"Comic Sans MS\";\n"
        "color: #f1dac4;\n"
        "background-color:transparent; \n"
        "")
        drone.send(at.REF(at.REF.input.start))
    
    def _DroneUP():
        ui.LastCom_label.setText("Up")
        ui.LastCom_label.setStyleSheet("font: 12pt \"Comic Sans MS\";\n" "color: #17a398;\n"
        "background-color:transparent; \n"
        "")
        drone.send(at.PCMD(at.PCMD.flag.progressive, 0, 0, SPEED, 0))

    def _DroneDown():
        ui.LastCom_label.setText("Down")
        ui.LastCom_label.setStyleSheet("font: 12pt \"Comic Sans MS\";\n" "color: #17a398;\n"
        "background-color:transparent; \n"
        "")
        drone.send(at.PCMD(at.PCMD.flag.progressive, 0, 0, -SPEED, 0))

    def _DroneRight():
        ui.LastCom_label.setText("Right")
        ui.LastCom_label.setStyleSheet("font: 12pt \"Comic Sans MS\";\n" "color: #17a398;\n"
        "background-color:transparent; \n"
        "")
        drone.send(at.PCMD(at.PCMD.flag.progressive, SPEED, 0, 0, 0))

    def _DroneLeft():
        ui.LastCom_label.setText("Left")
        ui.LastCom_label.setStyleSheet("font: 12pt \"Comic Sans MS\";\n" "color: #17a398;\n"
        "background-color:transparent; \n"
        "")
        drone.send(at.PCMD(at.PCMD.flag.progressive, -SPEED, 0, 0, 0))


    def _DroneCounterClockwise():
        ui.LastCom_label.setText("Anticlockwise")
        ui.LastCom_label.setStyleSheet("font: 10pt \"Comic Sans MS\";\n" "color: #17a398;\n"
        "background-color:transparent; \n"
        "")   
        drone.send(at.PCMD(at.PCMD.flag.progressive, 0, 0, 0, -SPEED))

    def _DroneClockwise():
        ui.LastCom_label.setText("Clockwise")
        ui.LastCom_label.setStyleSheet("font: 12pt \"Comic Sans MS\";\n" "color: #17a398;\n"
        "background-color:transparent; \n"
        "")   
        drone.send(at.PCMD(at.PCMD.flag.progressive, 0, 0, 0, SPEED))

    def _DroneBackward():
        ui.LastCom_label.setText("Backward")
        ui.LastCom_label.setStyleSheet("font: 12pt \"Comic Sans MS\";\n" "color: #17a398;\n"
        "background-color:transparent; \n"
        "")  
        drone.send(at.PCMD(at.PCMD.flag.progressive, 0, SPEED, 0, 0))

    def _DroneForward():
        ui.LastCom_label.setText("Forward")
        ui.LastCom_label.setStyleSheet("font: 12pt \"Comic Sans MS\";\n" "color: #17a398;\n"
        "background-color:transparent; \n"
        "") 
        drone.send(at.PCMD(at.PCMD.flag.progressive, 0, -SPEED, 0, 0))

    def _DroneHover():
        ui.LastCom_label.setText("Hover")
        ui.LastCom_label.setStyleSheet("font: 12pt \"Comic Sans MS\";\n" "color: #17a398;\n"
        "background-color:transparent; \n"
        "")
        drone.send(at.PCMD(flag=0))

    def _DroneLand():
        ui.LastCom_label.setText("Land")
        ui.LastCom_label.setStyleSheet("font: 12pt \"Comic Sans MS\";\n" "color: #17a398;\n"
        "background-color:transparent; \n"
        "")
        drone.send(at.REF())

    def _DroneEmergency():
        ui.LastCom_label.setText("Emergency")
        ui.LastCom_label.setStyleSheet("font: 12pt \"Comic Sans MS\";\n"
        "color: #823329;\n"
        "background-color:transparent; \n"
        "")
        drone.send(at.REF(at.REF.input.select))


# Binding the commands buttons to their specific action
    ui.DroneTakeoff.clicked.connect(_DroneTakeOff)
    ui.DroneUP.clicked.connect(_DroneUP)
    ui.DroneDown.clicked.connect(_DroneDown)
    ui.DroneRight.clicked.connect(_DroneRight)
    ui.DroneLeft.clicked.connect(_DroneLeft)
    ui.DroneAntiClockwise.clicked.connect(_DroneCounterClockwise)
    ui.DroneClockwise.clicked.connect(_DroneClockwise)
    ui.DroneForward.clicked.connect(_DroneForward)
    ui.DroneBackward.clicked.connect(_DroneBackward)
    ui.DroneHover.clicked.connect(_DroneHover)
    ui.DroneLand.clicked.connect(_DroneLand)
    ui.DroneEmergency.clicked.connect(_DroneEmergency)

# Set a communication with the PC's Webcam
    capture = cv2.VideoCapture(0)
    detector_h = HandDetector(detectionCon=0.8, maxHands= 2)

# the utility of this vector is to draw lines between different landmarks
    liaisons_hand = [[0, 1], [1, 2], [2, 3], [3, 4], [5, 6], [6, 7], [7, 8], [9, 10], [10, 11], [11, 12], [13, 14], [14, 15], [15, 16], [17, 18], [18, 19], [19, 20], [5, 9], [9, 13], [13, 17], [2, 5], [0, 17]]

# Left / Right

    #Sign for the Take Off command
    DRONE_TAKE_OFF = [[0, 0, 0, 0, 0],[0, 0, 0, 0, 0]]

    #Sign for the drone Up command
    DRONE_UP = [[0, 1, 0, 0, 0],[0, 1, 0, 0, 0]]

    #Sign for the drone Down command
    DRONE_DOWN = [[1, 1, 1, 0, 0],[1, 1, 1, 0, 0]]
    
    #Sign for the drone Right command
    DRONE_RIGHT = [[0, 0, 0, 0, 0],[1, 1, 1, 1, 1]]
    
    #Sign for the drone Left command
    DRONE_LEFT = [[1, 1, 1, 1, 1],[0, 0, 0, 0, 0]]

    #Sign for the drone Clockwise command
    DRONE_Clockwise = [[0, 0, 0, 0, 0],[1, 1, 1, 0, 0]]

    #Sign for the drone Counter-Clockwise command
    DRONE_CounterClockwise = [[1, 1, 1, 0, 0],[0, 0, 0, 0, 0]]

    #Sign for the drone Forward command
    DRONE_Forward = [[0, 1, 1, 0, 0],[0, 0, 0, 0, 0]]

    #Sign for the drone Backward command
    DRONE_Backward = [[0, 0, 0, 0, 0],[0, 1, 1, 0, 0]]

    #Sign for the drone Hover command
    DRONE_HOVER = [[1, 1, 1, 1, 1],[1, 1, 1, 1, 1]]
    
    #Sign for the drone Land command
    DRONE_LAND = [[1, 1, 0, 0, 0],[1, 1, 0, 0, 0]]
    
    #Sign for the drone Emergency command
    DRONE_EMERGENCY = [[0, 1, 1, 0, 0],[0, 1, 1, 0, 0]]

# Boolean Variables for the command limitation fucntion
    BOOL_TAKEOFF = True
    BOOL_UP = True
    BOOL_DOWN = True
    BOOL_RIGHT = True
    BOOL_LEFT = True
    BOOL_HOVER = True
    BOOL_LAND = True
    BOOL_EMERGENCY = True
    BOOL_CLOCKWISE = True
    BOOL_COUNTER_CLOCKWISE = True
    BOOL_FORWARD = True
    BOOL_BACKWARD = True


    def Command_Limitation(takeoff=True, up=True, down=True, right=True, left=True, hover=True, land=True, emergency=True, cw=True, ccw=True, forward=True, backward=True):

        """
        Block the last drone's command to avoid command overflow
        :param : Boolean Variable

        """
        global BOOL_TAKEOFF, BOOL_UP, BOOL_DOWN, BOOL_RIGHT, BOOL_LEFT, BOOL_HOVER, BOOL_LAND, BOOL_EMERGENCY, BOOL_CLOCKWISE, BOOL_COUNTER_CLOCKWISE, BOOL_FORWARD, BOOL_BACKWARD

        BOOL_TAKEOFF = takeoff
        BOOL_UP = up
        BOOL_DOWN = down
        BOOL_RIGHT = right
        BOOL_LEFT = left
        BOOL_HOVER = hover
        BOOL_LAND = land
        BOOL_EMERGENCY = emergency
        BOOL_CLOCKWISE = cw 
        BOOL_COUNTER_CLOCKWISE = ccw 
        BOOL_FORWARD = forward 
        BOOL_BACKWARD = backward 


# Get the drone's NavData function
    def store_navdata():
        """
        Put’s NavData in a file
        """
        navdata = drone.navdata.demo
        
        # Psi
        Navdata_file.write(str(navdata.psi * 0.001))
        Navdata_file.write(' ')
        # Phi
        Navdata_file.write(str(navdata.phi * 0.001))
        Navdata_file.write(' ')
        # Theta
        Navdata_file.write(str(navdata.theta * 0.001))
        Navdata_file.write(' ')
        #altitude
        Navdata_file.write(str(navdata.altitude))
        Navdata_file.write('\n')


# Get the current time and display it in the UI function   
    def Get_current_time():
        """
        Get the current time and display it in the UI
        """
    # Getting current time
        current_time = QTime.currentTime()
    # Converting QTime object to string
        label_time = current_time.toString('hh:mm')
    # Showing it to the label
        ui.label_Time.setText(label_time)

# Creating a function that updates the LCDs
    def update_lcd():
        """
        Updates the LCDs
        """
        navdata = drone.navdata.demo
        # Getting angular NavDatas then converting them from milidegrees to degrees
        ui.lcdNumber_Phi.display(navdata.phi * 0.001)
        ui.lcdNumber_Psi.display(navdata.psi * 0.001)
        ui.lcdNumber_Theta.display(navdata.theta * 0.001)

        # Getting the velocity of the X,Y,Z axis
        ui.lcdNumber_VX.display(navdata.vx)
        ui.lcdNumber_VY.display(navdata.vy)
        ui.lcdNumber_VZ.display(navdata.altitude * 0.01)

        # Getting the drone state NavData
        ui.lcdNumber_DroneState.display(bin(drone.navdata.metadata.state)[2:])

        # Getting the battery %
        ui.VBat.setValue(navdata.vbat_flying_percentage)
        ui.VBat.setProperty("value", f"{navdata.vbat_flying_percentage} %")





# Creating a function to display the drone's frames in a Pixmap
    def get_drone_frame():

        # Reading the drone's frames
        _,drone_frame = cam.read()

        # Converting the frames to QImage format
        image_d = QImage(drone_frame, *drone_frame.shape[1::-1], QImage.Format_RGB888).rgbSwapped()
        # Binding the QImage to a Pixmap
        pixmap = QPixmap.fromImage(image_d)
        pixmap = pixmap.scaled(ui.DroneCAM_label.width(), ui.DroneCAM_label.height(), QtCore.Qt.KeepAspectRatio)

        # Displaying the drone's frames in our label
        ui.DroneCAM_label.setPixmap(pixmap)

# Function that updates the battery QProgressBar depending it's %
    def update_BP():  

        navdata = drone.navdata.demo  

        if navdata.vbat_flying_percentage > 70:
            ui.VBat.setStyleSheet("QProgressBar {\n"
            "    border: 1px solid grey;\n"
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

        elif navdata.vbat_flying_percentage > 30:

            ui.VBat.setStyleSheet("QProgressBar {\n"
            "    border: 1px solid grey;\n"
            "    border-radius: 4px;\n"
            "    text-align: center;\n"
            "}\n"
            "\n"
            "QProgressBar::chunk {\n"
            "    background-color: #ffc300;\n"
            "    width: 10px;\n"
            "    margin: 0.5px;\n"
            "    border-radius: 2px;\n"
            "}")

        else:

            ui.VBat.setStyleSheet("QProgressBar {\n"
            "    border: 1px solid grey;\n"
            "    border-radius: 4px;\n"
            "    text-align: center;\n"
            "}\n"
            "\n"
            "QProgressBar::chunk {\n"
            "    background-color: #bf211e;\n"
            "    width: 10px;\n"
            "    margin: 0.5px;\n"
            "    border-radius: 2px;\n"
            "}")           

# Creating a function to display the Webcam's frames in a Pixmap && the hand gesture in an another Pixmap

    def get_frame():
        _, frame = capture.read(0)
        image = QImage(frame, *frame.shape[1::-1], QImage.Format_RGB888).rgbSwapped()
        pixmap = QPixmap.fromImage(image)
        pixmap = pixmap.scaled(ui.Camera_label.width(), ui.Camera_label.height(), QtCore.Qt.KeepAspectRatio)
        ui.Camera_label.setPixmap(pixmap)

        hands, img, = detector_h.findHands(frame)
        black = np.zeros(img.shape, dtype = "uint8")

# Creating the hand animation
        for hand in hands:
            
            for i, j in liaisons_hand:
                x1, y1, _ = hand['lmList'][i]
                x2, y2, _ = hand['lmList'][j]
                cv2.line(black, (x1,y1), (x2,y2), (204,255,255), thickness=5)

            for cx, cy, id in hand['lmList']:
                cv2.circle(black, (cx, cy), 10, (182, 161, 54), cv2.FILLED)
     
        image = QImage(black, *frame.shape[1::-1], QImage.Format_RGB888).rgbSwapped()
        pixmap = QPixmap.fromImage(image)
        pixmap = pixmap.scaled(ui.Animation_label.width(), ui.Animation_label.height(), QtCore.Qt.KeepAspectRatio)
        ui.Animation_label.setPixmap(pixmap)

# Hand Gesture Control part
        if hands:
            #1
            hand1 = hands[0]
            fingers_L = detector_h.fingersUp(hand1)

            if len(hands) == 2:
                hand2 = hands[1]
                fingers_R = detector_h.fingersUp(hand2)

                if [fingers_L, fingers_R] == DRONE_TAKE_OFF and BOOL_TAKEOFF:
                    _DroneTakeOff()
                    Command_Limitation(takeoff=False)
                    
                if [fingers_L, fingers_R] == DRONE_UP and BOOL_UP:
                    _DroneUP()
                    Command_Limitation(up=False)

                if [fingers_L, fingers_R] == DRONE_DOWN and BOOL_DOWN:
                    _DroneDown()
                    Command_Limitation(down=False)
                            
                if [fingers_L, fingers_R] == DRONE_LEFT and BOOL_LEFT:
                    _DroneLeft()
                    Command_Limitation(left=False)

                if [fingers_L, fingers_R] == DRONE_RIGHT and BOOL_RIGHT:
                    _DroneRight()
                    Command_Limitation(right=False)
                
                if [fingers_L, fingers_R] == DRONE_Clockwise and BOOL_CLOCKWISE:
                    _DroneClockwise()
                    Command_Limitation(cw=False)

                if [fingers_L, fingers_R] == DRONE_CounterClockwise and BOOL_COUNTER_CLOCKWISE:
                    _DroneCounterClockwise()
                    Command_Limitation(ccw=False)

                if [fingers_L, fingers_R] == DRONE_Forward and BOOL_FORWARD:
                    _DroneForward()
                    Command_Limitation(forward=False)
                
                if [fingers_L, fingers_R] == DRONE_Backward and BOOL_BACKWARD:
                    _DroneBackward()
                    Command_Limitation(backward=False)

                if [fingers_L, fingers_R] == DRONE_HOVER and BOOL_HOVER:
                    _DroneHover()
                    Command_Limitation(hover=False)
                    
                if [fingers_L, fingers_R] == DRONE_LAND and BOOL_LAND:
                    _DroneLand()
                    Command_Limitation(land=False)

                if [fingers_L, fingers_R] == DRONE_EMERGENCY and BOOL_EMERGENCY:
                    _DroneEmergency()
                    Command_Limitation(emergency=False)

    def close_connexion():
        Navdata_file.close()
        drone.emergency()
        drone._close()
        os._exit(0)
    
    fps =30
    
    timer = QTimer(MainWindow)
    timer.setInterval(int(1000/fps))
    timer.timeout.connect(get_frame)
    timer.start()

    fps = 120
    timer2 = QTimer(MainWindow)
    timer2.setInterval(int(1000/fps))
    timer2.timeout.connect(get_drone_frame)
    timer2.start()

    timer3 = QTimer(MainWindow)
    timer3.setInterval(1000)
    timer3.timeout.connect(update_lcd)
    timer3.start()

    timer4 = QTimer(MainWindow)
    timer4.setInterval(1000)
    timer4.timeout.connect(Get_current_time)
    timer4.start()


    timer5 = QTimer(MainWindow)
    timer5.setInterval(1000)
    timer5.timeout.connect(update_BP)
    timer5.start()

    timer6 = QTimer(MainWindow)
    timer6.setInterval(3000)
    timer6.timeout.connect(Command_Limitation)
    timer6.start()


    timer7 = QTimer(MainWindow)
    timer7.setInterval(30)
    timer7.timeout.connect(store_navdata)
    timer7.start()

    MainWindow.show()
    app.aboutToQuit.connect(close_connexion)
    sys.exit(app.exec_())
    