#from glob import glob
#from logging.config import stopListening
import sys
import winreg
import os
import pyautogui
import time
import pyperclip
from eth_account import Account

from PyQt5.QtCore import Qt,pyqtSlot
from PyQt5.QtWidgets import QMainWindow,QApplication,QWidget,QFileDialog,QMessageBox,QTableWidget,QTableWidgetItem
from Ui_luFoxTable import Ui_Form #导入你写的界面类

###定义变量
glist = []

###定义函数
def desktop_path():#通过注册表获得桌面路径
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
    return winreg.QueryValueEx(key,"Desktop")[0]



class MyMainWindow(QMainWindow,Ui_Form): 

    #引入全局变量
    global glist

    #初始化窗口
    def __init__(self,parent =None):
        super(MyMainWindow,self).__init__(parent)
        self.setupUi(self)
        #初始化延迟时间comboBox
        mlistSleep = ['1.5','1','2','3','5','8','10']
        self.comboBoxDelay.addItems(mlistSleep)


        #初始化表格tableWidget的表头
        mheadText = ['私钥','助记词','公钥','地址']
        self.tableWidget.clearContents()
        self.tableWidget.setHorizontalHeaderLabels(mheadText)
        self.tableWidget.setColumnWidth(1, 75)

    
        #绑定槽函数
        self.pushButtonOpen.clicked.connect(self.fOpenFile)
        self.tableWidget.cellClicked.connect(self.fcellClicked)

    #定义槽函数
    def fOpenFile(self):
        mfileName, mfiltUsed = QFileDialog.getOpenFileName(self, '打开保存小狐狸的文件', desktop_path(), \
        '小狐狸文件(*.txt)', '小狐狸文件(*.txt)', QFileDialog.ReadOnly)
        
        glist.clear()
        f = open( mfileName, mode = 'r',encoding='utf-8')
        mlist = f.readlines()
        for i in mlist:
            glist.append( i.split('+'))
        f.close()

        self.lineEditProjectName.setText(glist[0][0])

        mrowCount = len(mlist)
        self.tableWidget.setRowCount(mrowCount)

        # mtextPri = QTableWidgetItem('私钥')
        # mtextMnemonic = QTableWidgetItem('助记词')
        # mtextPub = QTableWidgetItem('公钥')
        # mtextAddr = QTableWidgetItem('地址')

        for i in range(0, mrowCount):
            mtextPri = QTableWidgetItem('私钥')
            mtextPri.setTextAlignment(Qt.AlignCenter)
            mtextMnemonic = QTableWidgetItem('助记词')
            mtextMnemonic.setTextAlignment(Qt.AlignCenter)
            mtextPub = QTableWidgetItem('公钥')
            mtextPub.setTextAlignment(Qt.AlignCenter)
            mtextAddr = QTableWidgetItem('地址')
            mtextAddr.setTextAlignment(Qt.AlignCenter)

            self.tableWidget.setItem(i, 0, mtextPri)
            self.tableWidget.setItem(i, 1, mtextMnemonic)
            self.tableWidget.setItem(i, 2, mtextPub)
            self.tableWidget.setItem(i, 3, mtextAddr)

    @pyqtSlot(int, int)
    def fcellClicked(self, mrow, mcolumn):
        pyperclip.copy(glist[mrow][mcolumn+2])      #记得+2

        if self.checkBoxAutoPaste.isChecked():
            msleep = float(self.comboBoxDelay.currentText())
            time.sleep(msleep)
            pyautogui.hotkey('ctrl','v')


        



        






#以下主程序创建不适应高分屏，在高分屏电脑上 文本显示不完整
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
sys.exit(app.exec_()) 