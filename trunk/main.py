#!/usr/bin/python
import os, os.path
import re
import shutil
import commands
import distutils.dir_util

class scgui():
    def __init__(self):
        self.steamname = "3fk"
        self.skinspath = os.path.join(os.environ["ProgramFiles(x86)"],"SCGUI\Skins")
        self.installedskin = {"Skin":"","Version":"","Author":"","Website":"","Info":""}
        self.cspath=os.path.join(os.environ["ProgramFiles(x86)"],"Steam/steamapps",self.steamname,"counter-strike source/cstrike")
        self.specsettings ={"t1name":"","t1url":"","t1flag":"","t2name":"","t2url":"","t2flag":""}
        self.cfgsettings ={"spec_player":"","hud_saytext_time":"","hud_deathnotice_time":"","spec_autodirector":"","spec_scoreboard":"","spec_mode":"","net_graph":"","cl_dynamiccrosshair":"","func_break_max_pieces":"","overview_names":""}
        self.resfiles=["Spectator.res", "ScoreBoard.res"]
        self.cfgfiles=["KLUTCH.cfg", "autoexec.cfg"]
        self.noskininstalled = "SCGUI cannot find any skins installed in your game folder. Try installing one by choosing one from the dropdown list. If this problem persists try reinstalling the program."
        
    # This function opens up the KLUTCH.cfg and gets the installed skins name (this should match a dir in the skins folder)
    def getinstalledskin(self, accountname):
        
        targetfilelocation=os.path.join(self.cspath,"cfg/KLUTCH.cfg")
        if os.path.exists(targetfilelocation):
            maincfg = open(targetfilelocation,"r")
            for line in maincfg.readlines():
                if re.search(r"// \[[^\]]*?=[^\]]*?\]", line):
                    matches = re.search(r"// \[([^\s]*?)=(.*?)\]", line)
                    if matches is not None:
                        self.installedskin[matches.group(1)] = matches.group(2)
        else:
            print self.noskininstalled
        
        
    
    # This will remove all skins from the cstrike dir
    def uninstallskin(self):
        currentskindir = os.path.join(self.skinspath,self.installedskin["Skin"])
        
        for subdir, dirs, files in os.walk(currentskindir):
            for name in files:
                filepath = os.path.join(subdir,name)
                filepathrel = os.path.relpath(filepath, currentskindir)
                filepathmain = os.path.join(self.cspath, filepathrel)
                if os.path.exists(filepathmain):
                    os.remove(filepathmain)
                    print "File "+filepath+" deleted."
                filebasemain = os.path.dirname(filepathmain)    
                if os.path.exists(filebasemain) and os.listdir(filebasemain) == []:
                    os.rmdir(filebasemain)
                    print "Folder "+filepath+" deleted." 
        #print self.installedskin
    
    # This will copy the desired skin files into the game folder and create any folders it may need
    def installskin(self, desiredskin):                  
        desiredskindir = os.path.join(self.skinspath, desiredskin)
        distutils.dir_util.copy_tree(desiredskindir, self.cspath)
    
    # Gets a list of folders in the skins folder
    def listskins(self):
        os.listdir(self.skinspath)
        
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
    
    def editres(self,targetfile):
        targetfilelocation=os.path.join(self.cspath,"resource/UI",targetfile)
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

makedo=scgui()
#makedo.readfiles()
#makedo.specsettings["t1name"]="Team VeryGames"
#makedo.specsettings["t1url"]="www.team-verygames.com"
#makedo.specsettings["t1flag"]="../vgui/klutch/team/VeryGames"
#makedo.specsettings["t2name"]="Copenhagen WOLVES"
#makedo.specsettings["t2url"]="www.copenhagenwolves.com"
#makedo.specsettings["t2flag"]="../vgui/klutch/team/Wolves"

#print makedo.specsettings
#print makedo.cfgsettings
makedo.getinstalledskin(makedo.steamname)
makedo.uninstallskin()
#makedo.installskin('Base')
#makedo.listskins()
#makedo.editcfg(makedo.cfgfiles[1])
#makedo.editres(makedo.resfiles[0])
#makedo.launchcs()
