# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 13:28:46 2020

@author: nki
"""
from PyQt5 import QtGui, QtCore, QtWidgets
import cv2
import sys, glob, os
from pathlib import Path
cwd = Path(os.getcwd())


ip =0# 'http://83.91.176.250/mjpg/video.mjpg'
#cap = cv2.VideoCapture(ip)


class DisplayImageWidget(QtWidgets.QWidget):
    def __init__(self, parent=None, ip=ip):
        super().__init__(parent)
        self.ip = 0

#        self.demo = QtCore.

        self.button = QtWidgets.QPushButton('Take picture')
        self.button.clicked.connect(self.show_image)
        self.entry_ip_cam = QtWidgets.QLineEdit(text = f'{ip}')
        self.button_ip = QtWidgets.QPushButton('Connect to ip camera')
        self.button_ip.clicked.connect(self.connect_ipcam)
        self.button_save = QtWidgets.QPushButton('Save current picture')
        self.button_save.clicked.connect(self.save_picture)

        self.image_frame = QtWidgets.QLabel(text='IP camera placeholder')

        self.button_left = QtWidgets.QPushButton('<')
        self.button_left.clicked.connect(lambda: print('left'))
        self.button_right = QtWidgets.QPushButton('>')
        self.button_right.clicked.connect(lambda: print('right'))

        self.layout = QtWidgets.QVBoxLayout()
        self.layout_top_buttons = QtWidgets.QHBoxLayout()
        self.layout.addLayout(self.layout_top_buttons)
        self.layout_top_buttons.addWidget(self.button)
        self.layout_top_buttons.addWidget(self.entry_ip_cam)
        self.layout_top_buttons.addWidget(self.button_ip)
        self.layout_top_buttons.addWidget(self.button_save)


        self.layout.addWidget(self.image_frame)

        self.layout_bottom_buttons = QtWidgets.QHBoxLayout()
        self.layout.addLayout(self.layout_bottom_buttons)
        self.layout_bottom_buttons.addWidget(self.button_left)
        self.layout_bottom_buttons.addWidget(self.button_right)



        self.setLayout(self.layout)
        self.connect_ipcam()

    @QtCore.pyqtSlot()
    def show_image(self):
        #self.cap.release()
        #self.cap.open(self.ip)
        [self.cap.read() for _ in range(4)]
        b, self.im    = self.cap.read() # cv2.imread('placeholder4.PNG')
        if b:
            self.image = QtGui.QImage(self.im.data, self.im.shape[1], self.im.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
            self.image_frame.setPixmap(QtGui.QPixmap.fromImage(self.image))
        else:
            print('No Image available')

    @QtCore.pyqtSlot()
    def connect_ipcam(self):
        if self.ip != self.entry_ip_cam.text():
            self.ip = self.entry_ip_cam.text()
            if self.ip.isdigit():
                self.cap = cv2.VideoCapture(int(self.ip))
            else:
                self.cap = cv2.VideoCapture(self.ip)
            #self.cap.release()

    @QtCore.pyqtSlot()
    def save_picture(self):
        cv2.imwrite('test.png', self.im)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    display_image_widget = DisplayImageWidget()
    display_image_widget.show()
    sys.exit(app.exec_())
