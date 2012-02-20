#!/usr/bin/python
import os, os.path
import sys
import webbrowser
import scgui

from PyQt4 import QtCore,QtGui,QtNetwork
from windowUi import Ui_MainWindow
"""

SCGUI.com
Shout Casters Graphical User Interface
Also known as KLUTCH's GUI Tool.

To compile from source you will need:
python 2.7 32bit
pyqt4 for 32bit (py2.7)
pywin32-217.win32-py2.7.exe (http://sourceforge.net/projects/pywin32)

"""
# Create a class for our main window
class Main(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        # This is always the same
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        
#        self.ui.twitter.setAttribute(QWebSettings::JavascriptEnabled, true)
#        self.ui.twitter.setAttribute(QWebSettings::PluginsEnabled, true)
#        self.ui.twitter.setAttribute(QWebSettings::AutoLoadImages, true)
#        self.ui.twitter.setAttribute(QWebSettings::JavaEnabled, false)
#        self.ui.twitter.setAttribute(QWebSettings::JavascriptCanOpenWindows, true)
        
        
        # makes an instance of scgui as kgui so use kgui to get the functions from scgui
        self.kgui=scgui.klutchguitool()
        # On launch find out if a skin is installed and refresh the array with info
        self.kgui.getinstalledskin(self.kgui.steamname)
        if self.kgui.settings.get('skin', 'installedskin') == "":
            print "No Skin is installed on main __init__"
        else:
            print "Found '" + self.kgui.settings.get('skin', 'installedskin') + "' installed on main __init__"
        print self.kgui.settings.get('main', 'cstrike')
        self.skinchosen(self.kgui.installedskin["Skin"])
        #kgui.installskin("Base")
        self.ui.skinName.setText(self.kgui.installedskin["Skin"])
        self.ui.skinAuthor.setText(self.kgui.installedskin["Author"])
        self.ui.skinVersion.setText(self.kgui.installedskin["Version"])
        self.ui.skinType.setText(self.kgui.installedskin["Type"])
        self.ui.skinDescription.setPlainText(self.kgui.installedskin["Info"])
        if not self.kgui.steamname == "":
            self.setWindowTitle("SCGUI " + self.kgui.settings.get('main', 'version') + " - " + self.kgui.steamname)
        else:
            self.setWindowTitle("SCGUI " + self.kgui.settings.get('main', 'version') + " - Unregistered")
        # This gets the available skins into the combobox
        self.ui.comboBox_skins.addItems(os.listdir(self.kgui.skinspath))
        # Set the preview image as the installed skin
        self.ui.SkinPreviewImage.setPixmap(QtGui.QPixmap("default.jpg"))
        # Connects the combo box to the update skins chosen def
        self.connect(self.ui.comboBox_skins, QtCore.SIGNAL('activated(QString)'), self.skinchosen)
        #Folder buttons
        self.ui.BTN_skinFolder.clicked.connect(self.kgui.openskinsfolder)
        self.ui.BTN_cstrikeFolder.clicked.connect(self.kgui.opencstrikefolder)
        #install/uninstall buttons
        self.ui.BTN_uninstallSkin.clicked.connect(self.clickedremoveskin)
        self.ui.BTN_uninstallSkin.setEnabled(False)
        self.ui.BTN_installSkin.clicked.connect(self.clickedinstallskin)
        self.ui.BTN_installSkin.setEnabled(False)
        self.ui.BTN_launchCSSpec.clicked.connect(self.kgui.launchcs)
        #Steam account connection
        self.ui.steaminput.setText(self.kgui.settings.get('main', 'steamname'))
        self.ui.BTN_steamname.setAutoDefault(True)
        self.ui.BTN_steamname.clicked.connect(self.setsteamname)
        self.ui.BTN_refreshteams.clicked.connect(self.resetteamtab)
        self.ui.BTN_updateTeams.clicked.connect(self.applyteamupdate)
        self.ui.BTN_swapSides.clicked.connect(self.clickedswapteams)
        self.ui.BTN_refreshCfg.clicked.connect(self.cfgrefresh)
        
    def cfgrefresh(self):
        self.kgui.cfgfileinterp(self.kgui.cfgfiles[0])
    
    def resetteamtab(self):
        self.kgui.readfiles()
        self.ui.Box_t1name.setText(self.kgui.specsettings["t1name"])
        self.ui.Box_t1url.setText(self.kgui.specsettings["t1url"])
        self.ui.Box_t2name.setText(self.kgui.specsettings["t2name"])
        self.ui.Box_t2url.setText(self.kgui.specsettings["t2url"])
        self.flagspath = os.path.join(self.kgui.settings.get('main','cstrike'),'materials','vgui','klutch','flags')
        os.chdir(str(self.flagspath))
        for files in os.listdir("."):
            if files.endswith(".vtf"): # So we dont have vtf and vmt in our list
                files=files[:-4]
                self.ui.comboBox_t1flag.addItem(files)
                self.ui.comboBox_t2flag.addItem(files)
                
                
    def clickedswapteams(self):
        team1name = str(self.ui.Box_t1name.displayText())
        team1url = str(self.ui.Box_t1url.displayText())
        team2name = str(self.ui.Box_t2name.displayText())
        team2url = str(self.ui.Box_t2url.displayText())
        team1flag = self.kgui.specsettings["t1flag"]
        team2flag = self.kgui.specsettings["t2flag"]
        
        self.kgui.specsettings["t1name"]=team2name
        self.kgui.specsettings["t1url"]=team2url
        self.kgui.specsettings["t2name"]=team1name
        self.kgui.specsettings["t2url"]=team1url
        self.kgui.specsettings["t1flag"]=team2flag
        self.kgui.specsettings["t2flag"]=team1flag
        
        self.kgui.editres(self.kgui.resfiles[0])
        
        self.ui.Box_t1name.setText(self.kgui.specsettings["t1name"])
        self.ui.Box_t1url.setText(self.kgui.specsettings["t1url"])
        self.ui.Box_t2name.setText(self.kgui.specsettings["t2name"])
        self.ui.Box_t2url.setText(self.kgui.specsettings["t2url"])

    def applyteamupdate(self):
        print "moo" # Because I like cows :)
        team1name = str(self.ui.Box_t1name.displayText())
        team1url = str(self.ui.Box_t1url.displayText())
        team2name = str(self.ui.Box_t2name.displayText())
        team2url = str(self.ui.Box_t2url.displayText())
        team1flag = str(self.ui.comboBox_t1flag.currentText())
        team2flag = str(self.ui.comboBox_t2flag.currentText())
        print self.ui.comboBox_t1flag.currentText()
        print self.ui.comboBox_t2flag.currentText()
        
        #format flag output
        outputflag1 = "../vgui/klutch/flags/" + team1flag
        outputflag2 = "../vgui/klutch/flags/" + team2flag
        
        self.kgui.specsettings["t1name"]=team1name
        self.kgui.specsettings["t1url"]=team1url
        self.kgui.specsettings["t1flag"]=outputflag1
        self.kgui.specsettings["t2name"]=team2name
        self.kgui.specsettings["t2url"]=team2url
        self.kgui.specsettings["t2flag"]=outputflag2
        self.kgui.editres(self.kgui.resfiles[0])
        
        
    
    def setsteamname(self):
        getsteamacc = str(self.ui.steaminput.displayText())
        accpath = os.path.join(os.environ["ProgramFiles(x86)"],"Steam\steamapps",getsteamacc,"counter-strike source\cstrike")
        if os.path.exists(accpath): 
            self.ui.steamstatus.setText("Success! Account is valid")
            self.ui.steamstatus.setStyleSheet("color: rgb(170, 170, 0)")
            self.kgui.steamname = getsteamacc
            self.kgui.getinstalledskin(self.kgui.steamname)
            print "Steam account set to " + self.kgui.steamname
            
            # This will then open and write our new steamname to the settings
            cfgfile = open("settings.ini", "w")            
            self.kgui.settings.set('main', 'steamname', self.kgui.steamname)
            self.kgui.settings.write(cfgfile)
            cfgfile.close()
            
            print "Steam account set to " + self.kgui.steamname
            print self.kgui.settings.get('main', 'cstrike')
            if not self.kgui.steamname == "":
                self.setWindowTitle("SCGUI " + self.kgui.settings.get('main', 'version') + " - " + self.kgui.steamname)
            else:
                self.setWindowTitle("SCGUI " + self.kgui.settings.get('main', 'version') + " - Unregistered")
        else:
            self.ui.steamstatus.setText("Error: Account Not Found!")
            self.ui.steamstatus.setStyleSheet("color: rgb(255, 0, 0)")
            self.setWindowTitle("SCGUI " + self.kgui.settings.get('main', 'version') + " - Unregistered")
            self.kgui.settings.set('main', 'steamname', '')
            QtGui.QMessageBox.warning(self
                , "Error"
                , "The Steam account name you have entered can not be found in your Steam directory. Enter the name or email address you use to sign into steam."
                , QtGui.QMessageBox.Ok)
        
    
    def clickedremoveskin(self):
        self.kgui.uninstallskin(self)
        QtGui.QMessageBox.information(self
            , "Skin Removed"
            , self.kgui.skindetails["Skin"] + " was removed successfully. You now have a clean game folder."
            , QtGui.QMessageBox.Ok)
        
        if self.kgui.skindetails["Skin"] == self.kgui.settings.get('skin', 'installedskin'):           
            #print "Skin: " + self.kgui.settings.get('main', 'installedskin') + " is installed"
            self.ui.BTN_installSkin.setEnabled(False)
            self.ui.BTN_uninstallSkin.setEnabled(True)
            self.ui.skinName.setText(self.kgui.skindetails["Skin"] + " (Installed)")
        else:
            self.ui.BTN_uninstallSkin.setEnabled(False)
            self.ui.BTN_installSkin.setEnabled(True)
            self.ui.skinName.setText(self.kgui.skindetails["Skin"])
            #print "Skin: " + self.kgui.settings.get('main', 'installedskin') + " is NOT installed"
        

    def clickedinstallskin(self):
        if not self.kgui.settings.get('main', 'steamname') == "":
            if self.kgui.settings.get('skin', 'installedskin') == "":
                self.kgui.installskin(self.kgui.skindetails["Skin"])
                QtGui.QMessageBox.information(self
                    , "Skin installed"
                    , self.kgui.skindetails["Skin"] + " was installed successfully."
                    , QtGui.QMessageBox.Ok)
                
            else:
                QtGui.QMessageBox.warning(self
                    , "Warning"
                    , "Please uninstall '" + self.kgui.settings.get('main', 'installedskin') + "' before trying to install another skin"
                    , QtGui.QMessageBox.Ok)
                print "Warning: Please set your steam account name before trying to install a skin"
        else:
            QtGui.QMessageBox.warning(self
                , "Warning"
                , "Please set your steam account name before trying to install a skin"
                , QtGui.QMessageBox.Ok)
            print "Warning: Please set your steam account name before trying to install a skin"
            
        if self.kgui.skindetails["Skin"] == self.kgui.settings.get('skin', 'installedskin'):           
            #print "Skin: " + self.kgui.settings.get('main', 'installedskin') + " is installed"
            self.ui.BTN_installSkin.setEnabled(False)
            self.ui.BTN_uninstallSkin.setEnabled(True)
            self.ui.skinName.setText(self.kgui.skindetails["Skin"] + " (Installed)")
        else:
            self.ui.BTN_uninstallSkin.setEnabled(False)
            self.ui.BTN_installSkin.setEnabled(True)
            self.ui.skinName.setText(self.kgui.skindetails["Skin"])
            #print "Skin: " + self.kgui.settings.get('main', 'installedskin') + " is NOT installed"
            
    
    def skinchosen(self, text):
        # makes an instance of scgui as kgui so use kgui to get the functions from scgui
        
        # On launch find out if a skin is installed and refresh the array with info
        self.kgui.getinstalledskin(self.kgui.settings.get('main', 'steamname'))
        #kgui.installskin("Base")
        self.ui.skinName.setText(self.kgui.installedskin["Skin"])
        self.ui.skinAuthor.setText(self.kgui.installedskin["Author"])
        self.ui.skinVersion.setText(self.kgui.installedskin["Version"])
        self.ui.skinType.setText(self.kgui.installedskin["Type"])
        self.ui.skinDescription.setPlainText(self.kgui.installedskin["Info"])
        
        self.kgui.getskindetails(str(text))
        self.ui.SkinPreviewImage.setPixmap(QtGui.QPixmap(os.path.join(self.kgui.skinspath, self.kgui.skindetails["Skin"], "preview.jpg")))
        self.ui.skinName.setText(self.kgui.skindetails["Skin"])
        self.ui.skinAuthor.setText(self.kgui.skindetails["Author"])
        self.ui.skinVersion.setText(self.kgui.skindetails["Version"])
        self.ui.skinType.setText(self.kgui.skindetails["Type"])
        self.ui.skinDescription.setPlainText(self.kgui.skindetails["Info"])
        
        # Set the teams tab enables
        if not self.kgui.skindetails["TeamBar"] == "yes":
            #Disable team groups
            self.ui.teamgrouphome.setEnabled(False)
            self.ui.teamgroupaway.setEnabled(False)
            print "disabled team groups"
        else:
            #Enable team groups
            self.ui.teamgrouphome.setEnabled(True)
            self.ui.teamgroupaway.setEnabled(True)
            print "enabled team groups"
        if not self.kgui.skindetails["PlayerBar"] == "yes":
            #Disable PlayerBar
            self.ui.playergroup.setEnabled(False)
            print "disabled player group"
        else:
            #Enable PlayerBar
            self.ui.playergroup.setEnabled(True)
            print "enabled player group"
            
        
        if self.kgui.skindetails["Skin"] == self.kgui.settings.get('skin', 'installedskin'):
            #print "Skin: " + self.kgui.settings.get('main', 'installedskin') + " is installed"
            self.ui.BTN_installSkin.setEnabled(False)
            self.ui.BTN_uninstallSkin.setEnabled(True)
            self.ui.skinName.setText(self.kgui.skindetails["Skin"] + " (Installed)")
        else:
            self.ui.BTN_uninstallSkin.setEnabled(False)
            self.ui.BTN_installSkin.setEnabled(True)
            self.ui.skinName.setText(self.kgui.skindetails["Skin"])
            #print "Skin: " + self.kgui.settings.get('main', 'installedskin') + " is NOT installed"
        
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