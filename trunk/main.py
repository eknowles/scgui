#!/usr/bin/python
import os, os.path
import sys

# Import Qt modules
from PyQt4 import QtCore,QtGui

# Import the compiled UI module
from windowUi import Ui_MainWindow
 
# Import our backend
import scgui

# Create a class for our main window
class Main(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        # This is always the same
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
                
        # makes an instance of scgui as kgui
        # so use kgui to get the functions from scgui
        kgui=scgui.klutchguitool()
        
        # On launch find out if a skin is installed and refresh the array with info
        kgui.getinstalledskin(kgui.steamname)
        #kgui.installskin("Base")
        self.ui.installed_skin.setText(kgui.installedskin["Skin"])
        self.ui.skinVersion.setText(kgui.installedskin["Author"])
        self.ui.skinCreator.setText(kgui.installedskin["Version"])
        self.ui.skinWebsite.setText(kgui.installedskin["Website"])
        self.ui.skinDescription.setText(kgui.installedskin["Info"])
        
        # This gets the available skins into the combobox
        self.ui.comboBox_skins.addItems(os.listdir(kgui.skinspath))
        self.currentskinimage = QtGui.QImage(os.path.join(kgui.skinspath, kgui.installedskin["Skin"], "preview.jpg"))
        self.ui.skinPreviewImage.setBackgroundBrush(QtGui.QBrush(self.currentskinimage))
        
        
        self.connect(self.ui.comboBox_skins, QtCore.SIGNAL('activated(QString)'), self.skinchosen)
    
    def skinchosen(self, text):
        kgui=scgui.klutchguitool()
        kgui.getskindetails(text)
        self.ui.installed_skin.setText(kgui.skindetails["Skin"])
        self.ui.skinVersion.setText(kgui.skindetails["Author"])
        self.ui.skinCreator.setText(kgui.skindetails["Version"])
        self.ui.skinWebsite.setText(kgui.skindetails["Website"])
        self.ui.skinDescription.setText(kgui.skindetails["Info"])
        
        
def main():
    # Again, this is boilerplate, it's going to be the same on
    # almost every app you write
    app = QtGui.QApplication(sys.argv)
    window=Main()
    window.show()
    # It's exec_ because exec is a reserved word in Python
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()