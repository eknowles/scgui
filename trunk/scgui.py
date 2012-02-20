#!/usr/bin/python
import os, os.path
import re
import shutil
import commands
import distutils.dir_util
import subprocess
import operator
import win32api, win32con
import sys

# Import bits to read edit configs like settings.ini
from ConfigParser import SafeConfigParser

class klutchguitool():
    def __init__(self): 
        
        self.version = "1.0"
        
        self.settings = SafeConfigParser(allow_no_value=True)
        if not os.path.exists("settings.ini"):
            print "settings.ini doesn't exist so making a fresh one"
            # lets create that config file for next time...
            cfgfile = open("settings.ini",'w')
            # add the settings to the structure of the file, and lets write it out...
            self.settings.add_section('main')
            self.settings.set('main','version', self.version)
            self.settings.set('main','steamname', '')
            self.settings.set('main','cstrike', os.environ["ProgramFiles(x86)"]+'\Steam\steamapps\%(steamname)s\counter-strike source\cstrike')
            self.settings.add_section('skin')
            self.settings.set('skin','installedskin', '')
            self.settings.set('skin','teambar', '')
            self.settings.set('skin','playerbar', '')
            self.settings.write(cfgfile)
            cfgfile.close() 
        self.settings.read('settings.ini')
        self.steamname = self.settings.get('main', 'steamname')
        #self.skinspath = os.path.join(os.environ["ProgramFiles(x86)"],"SCGUI\Skins")
        self.skinspath = os.path.join(os.path.dirname(sys.argv[0]),"Skins")
        self.cspath=os.path.join(os.environ["ProgramFiles(x86)"],"Steam/steamapps",self.steamname,"counter-strike source/cstrike")
        self.installedskin = {"Skin":"Welcome to KLUTCH's GUI Tool","Version":"No Skin Detected","Author":"Get involved at SCGUI.com","Type":"No Skin Detected","Info":"Select a skin from the drop down box above and install! Please report any bugs to scgui.com"}
        self.skindetails = {"Skin":"","Version":"","Author":"","Type":"","Info":"","TeamBar":"","PlayerBar":""}
        self.specsettings ={"t1name":"","t1url":"","t1flag":"","t2name":"","t2url":"","t2flag":"","playername":"", "playerflag":""}
        self.cfgsettings ={"spec_player":"","hud_saytext_time":"","hud_deathnotice_time":"","spec_autodirector":"","spec_scoreboard":"","spec_mode":"","net_graph":"","cl_dynamiccrosshair":"","func_break_max_pieces":"","overview_names":""}
        self.cfgheaders =["Console Variable","Value"]
        self.resfiles=["Spectator.res"] #, "ScoreBoard.res"]
        self.cfgfiles=["KLUTCH.cfg"] #, "autoexec.cfg"]
        self.noskininstalled = "SCGUI cannot find any skins installed in your game folder. Try installing one by choosing one from the dropdown list. If this problem persists try reinstalling the program."
        
    # This function opens up the KLUTCH.cfg and gets the installed skins name (this should match a dir in the skins folder)
    def getskindetails(self, skin):
        
        targetfilelocation=os.path.join(self.skinspath,skin,"cfg/KLUTCH.cfg")
        if os.path.exists(targetfilelocation):
            maincfg = open(targetfilelocation,"r")
            for line in maincfg.readlines():
                if re.search(r"// \[[^\]]*?=[^\]]*?\]", line):
                    matches = re.search(r"// \[([^\s]*?)=(.*?)\]", line)
                    if matches is not None:
                        self.skindetails[matches.group(1)] = matches.group(2)
                        
    
    def getinstalledskin(self, accountname):
        targetfilelocation=os.path.normpath(os.path.join(self.cspath,"cfg/KLUTCH.cfg"))
        if os.path.isfile(targetfilelocation):
            maincfg = open(targetfilelocation,"r")
            for line in maincfg.readlines():
                if re.search(r"// \[[^\]]*?=[^\]]*?\]", line):
                    matches = re.search(r"// \[([^\s]*?)=(.*?)\]", line)
                    if matches is not None:
                        self.installedskin[matches.group(1)] = matches.group(2)
                
                if re.search(r"// \[Skin=[^\]]*?\]", line):
                    matches = re.search(r"// \[Skin=(.*?)\]", line)
                    print matches.group(1)
                    # This will then open and write the installedskin to the settings
                    cfgfile = open("settings.ini", "w")            
                    self.settings.set('skin', 'installedskin', matches.group(1))
                    self.settings.write(cfgfile)
                    cfgfile.close()
        else:
            print "Warning: No skin installed or incorrect steam username."
            # This will then open and write the installedskin to the settings
            cfgfile = open("settings.ini", "w")            
            self.settings.set('skin', 'installedskin', '')
            self.settings.write(cfgfile)
            cfgfile.close()
    
    # This will remove all skins from the cstrike dir
    def count_files(self,in_directory):
        joiner= (in_directory + os.path.sep).__add__
        return sum(
            os.path.isfile(filename)
            for filename
            in map(joiner, os.listdir(in_directory))
        )
    
    def uninstallskin(self, status):
        currentskindir = os.path.join(self.skinspath,self.settings.get('skin','installedskin'))
        print "___UNINSTALLING_SKIN________________________________________________"
        for subdir, dirs, files in os.walk(currentskindir):
            for name in files:
                filepath = os.path.join(subdir,name)
                filepathrel = os.path.relpath(filepath, currentskindir)
                filepathmain = os.path.normpath(os.path.join(self.cspath, filepathrel))
                if os.path.exists(filepathmain):
                    fileAtt = win32api.GetFileAttributes(filepathmain)
                    if (fileAtt & win32con.FILE_ATTRIBUTE_READONLY):
                        # File is read-only, so make it writeable
                        win32api.SetFileAttributes(filepathmain, ~win32con.FILE_ATTRIBUTE_READONLY)
                    os.remove(filepathmain)
                    print "Removing file "+name+"..."
                filebasemain = os.path.dirname(filepathmain)    
                if os.path.exists(filebasemain) and os.listdir(filebasemain) == []:
                    os.rmdir(filebasemain)
                    print "Removing folder "+filebasemain+"..."
        # This will then open and write the installedskin to the settings
        cfgfile = open("settings.ini", "w")            
        self.settings.set('skin', 'installedskin', '')
        self.settings.write(cfgfile)
        cfgfile.close()
        print "____________________________________________________________________"
        print "Files have been removed."
    
    # This will copy the desired skin files into the game folder and create any folders it may need
    def installskin(self, desiredskin):  
        dirtydesiredskindir = os.path.join(self.skinspath, desiredskin)
        desiredskindir = os.path.normpath(dirtydesiredskindir)
        distutils.dir_util.copy_tree(desiredskindir, self.settings.get('main', 'cstrike'))
        
        # This will then open and write our new desiredskin to the settings
        cfgfile = open("settings.ini", "w")            
        self.settings.set('skin', 'installedskin', desiredskin)
        self.settings.write(cfgfile)
        cfgfile.close()
        
        print "____________________________________________________________________"
        print desiredskin + " installed successfully."
        
    
    # Gets a list of folders in the skins folder
    def listskins(self):
        print "lol"#os.listdir(self.skinspath)
        
        
    # This reads resorce files and puts key settings into variables
    def resfileinterp(self, targetfile):
        targetfilelocation=os.path.join(self.cspath,"resource/UI",targetfile)
        resfile = open(targetfilelocation,"r")
        for line in resfile.readlines():
            if re.search(r"\"[^\"]*\"[\s]*?\"[^\"]*\"[\s]*?//%[^%]*%", line):
                matches = re.search(r"\"([^\"]*)\"[\s]*?\"([^\"]*)\"[\s]*?//%([^%]*)%", line)
                self.specsettings[matches.group(3)] = matches.group(2)
                
    def cfgfileinterp(self,targetfile):
        targetfilelocation=os.path.join(self.cspath,"cfg/KLUTCH.cfg")
        cfgfile = open(targetfilelocation,"r")
        for line in cfgfile.readlines():
            if re.search(r"\"[^\"]*\"[\s]*?\"[^\"]*\"", line):
                matches = re.search(r"\"([^\"]*)\"[\s]*?\"([^\"]*)\"", line)
                self.cfgsettings[matches.group(1)] = matches.group(2)
        print self.cfgsettings
    
    def editres(self,targetfile):
        tgfile = os.path.join(self.cspath,"resource/UI",targetfile)
        targetfilelocation= os.path.normpath(tgfile)
        resfile = open(targetfilelocation,"r")
        resfile_output = resfile.read();
        resfile.close()
        for key, setting  in self.specsettings.iteritems():
            resfile_output=re.sub(r"\"([^\"]*)\"[\s]*?\"([^\"]*)\"[\s]*?//%"+key+ "%","\""+r"\1"+"\" \""+setting+ "\" //%"+key+ "%", resfile_output)
        resfile = open(targetfilelocation,"w")
        resfile.write(resfile_output)
        resfile.close()
        #print resfile_output    
        
    def editcfg(self,targetfile):
        targetfilelocation=os.path.join(self.cspath,"cfg/KLUTCH.cfg")
        cfgfile = open(targetfilelocation,"r")
        cfgfile_output = cfgfile.read();
        cfgfile.close()
        for key, setting  in self.cfgsettings.iteritems():
            #print key,setting
            cfgfile_output=re.sub(r"\""+key+ r"\"[\s]*?\"([^\"]*)\"", "\""+key+"\" \""+setting+ "\"",cfgfile_output)
        cfgfile = open(targetfilelocation,"w")
        cfgfile.write(cfgfile_output)
        cfgfile.close()
        #print cfgfile_output
        
    def readfiles(self):
        for guifile in self.resfiles:
            self.resfileinterp(guifile)
        for guifile in self.cfgfiles:
            self.cfgfileinterp(guifile)
            
    def launchcs(self):
        os.execv("C:\Program Files (x86)\Steam\Steam.exe", ['-applaunch 240','-novid','-sw','-w 1280','-h 720','-x 0','-y 0','-noborder','+fps_max 240'])

    def openskinsfolder(self):
        subprocess.Popen('explorer ' + self.skinspath)
        
    def opencstrikefolder(self):
        subprocess.Popen('explorer ' + os.path.normpath(self.cspath))
        print os.path.normpath(self.cspath)