#!/usr/bin/python
import os, os.path
import sys
import webbrowser

"""
SCGUI.com
Shout Casters Graphical User Interface
Also known as KLUTCH's GUI Tool.

To compile from source you will need:
python 2.7 32bit
pyqt4 for 32bit (py2.7)
pywin32-217.win32-py2.7.exe (http://sourceforge.net/projects/pywin32)
"""

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
        if self.kgui.installedskin["Skin"] == "":
            print "No Skin is installed on __init__"
        else:
            print "Found '" + self.kgui.installedskin["Skin"] + "' installed on __init__"
        self.skinchosen(self.kgui.installedskin["Skin"])
        #kgui.installskin("Base")
        self.ui.skinName.setText(self.kgui.installedskin["Skin"])
        self.ui.skinAuthor.setText(self.kgui.installedskin["Author"])
        self.ui.skinVersion.setText(self.kgui.installedskin["Version"])
        self.ui.skinType.setText(self.kgui.installedskin["Type"])
        self.ui.skinDescription.setText(self.kgui.installedskin["Info"])
        
        if not self.kgui.steamname == "":
            self.setWindowTitle("SCGUI - " + self.kgui.steamname)
            
        else:
            self.setWindowTitle("SCGUI - Unregistered")
        
        # !!! TODO: for each name in skins folder > if exists name/cfg/klutch.cfg > addItems to combo, else ignore !!!
        
        # This gets the available skins into the combobox
        self.ui.comboBox_skins.addItems(os.listdir(self.kgui.skinspath))
        # Set the preview image as the installed skin
        self.ui.SkinPreviewImage.setPixmap(QtGui.QPixmap("default.jpg"))
        # Connects the combo box to the update skins chosen def
        self.connect(self.ui.comboBox_skins, QtCore.SIGNAL('activated(QString)'), self.skinchosen)
        self.ui.BTN_skinFolder.clicked.connect(self.kgui.openskinsfolder)
        self.ui.BTN_cstrikeFolder.clicked.connect(self.kgui.opencstrikefolder)
        self.ui.BTN_uninstallSkin.clicked.connect(self.kgui.uninstallskin)
        self.ui.BTN_installSkin.clicked.connect(self.clickedinstallskin)
        self.ui.BTN_launchCSSpec.clicked.connect(self.kgui.launchcs)
        
        self.ui.steaminput.setText(self.kgui.steamname)
        self.ui.BTN_steamname.clicked.connect(self.setsteamname)
        
    def setsteamname(self):
        getsteamacc = str(self.ui.steaminput.displayText())
        self.kgui.steamname = getsteamacc
        print "Steam account set to " + self.kgui.steamname
        if not self.kgui.steamname == "":
            self.setWindowTitle("SCGUI - " + self.kgui.steamname)
        else:
            self.setWindowTitle("SCGUI - Unregistered")
        
    

    def clickedinstallskin(self):
        self.kgui.installskin(self.kgui.skindetails["Skin"])
    
    def skinchosen(self, text):
        # makes an instance of scgui as kgui so use kgui to get the functions from scgui
        
        # On launch find out if a skin is installed and refresh the array with info
        self.kgui.getinstalledskin(self.kgui.steamname)
        #kgui.installskin("Base")
        self.ui.skinName.setText(self.kgui.installedskin["Skin"])
        self.ui.skinAuthor.setText(self.kgui.installedskin["Author"])
        self.ui.skinVersion.setText(self.kgui.installedskin["Version"])
        self.ui.skinType.setText(self.kgui.installedskin["Type"])
        self.ui.skinDescription.setText(self.kgui.installedskin["Info"])
        
        self.kgui.getskindetails(str(text))
        self.ui.SkinPreviewImage.setPixmap(QtGui.QPixmap(os.path.join(self.kgui.skinspath, self.kgui.skindetails["Skin"], "preview.jpg")))
        self.ui.skinName.setText(self.kgui.skindetails["Skin"])
        self.ui.skinAuthor.setText(self.kgui.skindetails["Author"])
        self.ui.skinVersion.setText(self.kgui.skindetails["Version"])
        self.ui.skinType.setText(self.kgui.skindetails["Type"])
        self.ui.skinDescription.setText(self.kgui.skindetails["Info"])
        
        if self.kgui.skindetails["Skin"] == self.kgui.installedskin["Skin"]:
            print "Skin: " + self.kgui.skindetails["Skin"] + " is installed"
            self.ui.BTN_installSkin.setEnabled(False)
            self.ui.BTN_uninstallSkin.setEnabled(True)
            self.ui.skinName.setText(self.kgui.skindetails["Skin"] + " (Installed)")
        else:
            self.ui.BTN_uninstallSkin.setEnabled(False)
            self.ui.BTN_installSkin.setEnabled(True)
            print "Skin: " + self.kgui.skindetails["Skin"] + " is NOT installed"
        
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