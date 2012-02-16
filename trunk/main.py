#!/usr/bin/python
import os, os.path
import sys
import webbrowser

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
                
        # makes an instance of scgui as kgui so use kgui to get the functions from scgui
        self.kgui=scgui.klutchguitool()
        
        # On launch find out if a skin is installed and refresh the array with info
        self.kgui.getinstalledskin(self.kgui.steamname)
        #kgui.installskin("Base")
        self.ui.skinName.setText(self.kgui.installedskin["Skin"])
        self.ui.skinAuthor.setText(self.kgui.installedskin["Author"])
        self.ui.skinVersion.setText(self.kgui.installedskin["Version"])
        self.ui.skinWebsite.setText(self.kgui.installedskin["Website"])
        self.ui.skinDescription.setText(self.kgui.installedskin["Info"])
        
        # This gets the available skins into the combobox
        self.ui.comboBox_skins.addItems(os.listdir(self.kgui.skinspath))
        
        # Set the preview image as the installed skin
        self.ui.SkinPreviewImage.setPixmap(QtGui.QPixmap(os.path.join(self.kgui.skinspath, self.kgui.installedskin["Skin"], "preview.jpg")))

        
        self.connect(self.ui.comboBox_skins, QtCore.SIGNAL('activated(QString)'), self.skinchosen)
        self.connect(self.ui.skinWebsite, QtCore.SIGNAL('activated(QString)'), self.skinchosen)
    
    def skinchosen(self, text):
        # makes an instance of scgui as kgui so use kgui to get the functions from scgui
        
        self.kgui.getskindetails(str(text))
        self.ui.SkinPreviewImage.setPixmap(QtGui.QPixmap(os.path.join(self.kgui.skinspath, self.kgui.skindetails["Skin"], "preview.jpg")))
        self.ui.skinName.setText(self.kgui.skindetails["Skin"])
        self.ui.skinAuthor.setText(self.kgui.skindetails["Author"])
        self.ui.skinVersion.setText(self.kgui.skindetails["Version"])
        self.ui.skinWebsite.setText(self.kgui.skindetails["Website"])
        self.ui.skinDescription.setText(self.kgui.skindetails["Info"])
        
    def skinhyperlink(self):
        webbrowser.open_new_tab(self.kgui.skindetails["Website"])
        
        
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