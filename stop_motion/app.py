# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 13:28:46 2020

@author: nki
"""
from PyQt5 import QtGui, QtCore, QtWidgets
import cv2
import sys, glob, os, time, re
from pathlib import Path
cwd = Path(os.getcwd())


ip =0# 'http://83.91.176.250/mjpg/video.mjpg'
#cap = cv2.VideoCapture(ip)


class WorkerSignals(QtCore.QObject):
    '''
    https://www.learnpyqt.com/courses/concurrent-execution/multithreading-pyqt-applications-qthreadpool/
    Defines the signals available from a running worker thread.

    Supported signals are:

    finished
        No data
    
    error
        `tuple` (exctype, value, traceback.format_exc() )
    
    result
        `object` data returned from processing, anything

    progress
        `int` indicating % progress 

    '''
    finished = QtCore.pyqtSignal()
    error = QtCore.pyqtSignal(tuple)
    result = QtCore.pyqtSignal(object)
    progress = QtCore.pyqtSignal(int)

class Worker(QtCore.QRunnable):
    def __init__(self, func, *args, **kwargs):
        super().__init__()
        self.func = func
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()    

        # Add the callback to our kwargs
        self.kwargs['progress_callback'] = self.signals.progress

    @QtCore.pyqtSlot()
    def run(self):
        print('thread started')
        i = 0
        while self.active:#for i in range(n):
            i+=1
            if not i % 50:
                print(f'{i}/42   worker active: {self.active}')

            try:
                result = self.func()
            except:
                traceback.print_exc()
                exctype, value = sys.exc_info()[:2]
                self.signals.error.emit((exctype, value, traceback.format_exc()))
            else:
                self.signals.result.emit(result)  # Return the result of the processing
            finally:
                self.signals.finished.emit()  # Done

        print('thread completed')



class StopMotion(QtWidgets.QWidget):
    def closeEvent(self, event):
        print('closing...')
        print(dir(self.threadpool))
        self.worker.active = False
        super().closeEvent(event)

    def __init__(self, parent=None, ip=ip, projectname='test'):
        super().__init__(parent)
        self.ip = 0
        self.threadpool = QtCore.QThreadPool()
        self.projectname = projectname
        self.filename = f'{self.projectname}_0001000.png'
        self.path = os.path.join(cwd, self.projectname)
        os.makedirs(self.path, exist_ok=True)
        print(dir(self))
        #self.closeEvent.connect(self.print_func)
        #time.sleep(200)


        # self.demo = QtCore.

        self.button = QtWidgets.QPushButton('Stop stream')
        self.button.clicked.connect(lambda context: self.stop_worker)
        self.entry_ip_cam = QtWidgets.QLineEdit(text = f'{ip}')
        self.button_ip = QtWidgets.QPushButton('Connect to ip camera')
        self.button_ip.clicked.connect(self.connect_ipcam)
        self.button_save = QtWidgets.QPushButton('Take picture')
        self.button_save.clicked.connect(lambda context: self.show_image(context=True))

        self.streaming_frame = QtWidgets.QLabel(text='Steaming frame')
        self.image_frame = QtWidgets.QLabel(text='Picture taken')

        self.button_left = QtWidgets.QPushButton('<')
        self.button_left.clicked.connect(lambda: print('left'))
        self.button_right = QtWidgets.QPushButton('>')
        self.button_right.clicked.connect(lambda: print('right'))

        self.master_layout = QtWidgets.QHBoxLayout()
        self.layout = QtWidgets.QVBoxLayout()

        self.layout_top_buttons = QtWidgets.QHBoxLayout()
        self.layout.addLayout(self.layout_top_buttons)
        self.layout_top_buttons.addWidget(self.button)
        self.layout_top_buttons.addWidget(self.entry_ip_cam)
        self.layout_top_buttons.addWidget(self.button_ip)
        self.layout_top_buttons.addWidget(self.button_save)


        self.layout.addWidget(self.streaming_frame)
        self.layout.addWidget(self.image_frame)

        self.layout_bottom_buttons = QtWidgets.QHBoxLayout()
        self.layout.addLayout(self.layout_bottom_buttons)
        self.layout_bottom_buttons.addWidget(self.button_left)
        self.layout_bottom_buttons.addWidget(self.button_right)

        self.master_layout.addLayout(self.layout)

        self.setLayout(self.master_layout)

        self.connect_ipcam()
        self.stream()

    def stream(self):
        self.worker = Worker(self.show_image)
        #self.worker.setAutoDelete(True)
        self.worker.active = True
        self.threadpool.start(self.worker)
        dir(self.threadpool)

    def stop_worker(self):
        self.worker.active = False

    @QtCore.pyqtSlot()
    def show_image(self, context=None):
        context = self.streaming_frame if context is None else self.image_frame
        ret, im    = self.cap.read() # cv2.imread('placeholder4.PNG')
        if ret:
            image = QtGui.QImage(im.data, im.shape[1], im.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
            context.setPixmap(QtGui.QPixmap.fromImage(image))
            if context == self.image_frame:
                self.save_picture(im)
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

    def next_filename(self):
        while self.filename in os.listdir(self.path):
            _, number, ext = re.split(f'{self.projectname}_|\.', self.filename)
            self.filename = f'{self.projectname}_{int(number)+1000:07d}.{ext}'


    @QtCore.pyqtSlot()
    def save_picture(self, im, filename=None):
        self.next_filename()
        cv2.imwrite(os.path.join(self.path, self.filename), im)


    @QtCore.pyqtSlot()
    def __del__(self, *args, **kwargs):
        print(args, kwargs)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    display_image_widget = StopMotion(projectname='name')
    display_image_widget.show()
    sys.exit(app.exec_())
    del display_image_widget
