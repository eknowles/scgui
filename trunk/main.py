#!/usr/bin/python
import os, os.path
import re

class scgui():
    def __init__(self):
        self.steamname = "3fk"
        self.cspath=os.path.join("C:/Program Files (x86)/Steam/steamapps",self.steamname,"counter-strike source")
        self.specsettings ={
                              "t1name":"", 
                              "t1url":"", 
                              "t1flag":"", 
                              "t2name":"", 
                              "t2url":"", 
                              "t2flag":"", 
                               }
        self.cfgsettings ={
                              "spec_player":"", 
                              "hud_saytext_time":"", 
                              "hud_deathnotice_time":"", 
                              "spec_autodirector":"", 
                              "spec_scoreboard":"", 
                              "spec_mode":"", 
                              "net_graph":"",  
                              "cl_dynamiccrosshair":"", 
                              "func_break_max_pieces":"", 
                              "overview_names":"", 
                               }
        self.resfiles=["Spectator.res", "ScoreBoard.res"]
        
    def getinstalledskin(self, accountname):
        targetfilelocation=os.path.join(self.cspath,"cstrike/cfg/KLUTCH.cfg")
        maincfg = open(targetfilelocation,"r")
        for line in maincfg.readlines():
            if re.search(r"// \[[^\]]*?=[^\]]*?\]", line):
                matches = re.search(r"// \[Skin=([^\s]*?)\]", line)
                if matches is not None:
                    installedskin = matches.group(1)
                    print installedskin
        
    def resfileinterp(self, targetfile):
        targetfilelocation=os.path.join(self.cspath,"cstrike/resource/UI",targetfile)
        resfile = open(targetfilelocation,"r")
        for line in resfile.readlines():
            if re.search(r"\"[^\"]*\"[\s]*?\"[^\"]*\"[\s]*?//%[^%]*%", line):
                matches = re.search(r"\"([^\"]*)\"[\s]*?\"([^\"]*)\"[\s]*?//%([^%]*)%", line)
                self.specsettings[matches.group(3)] = matches.group(2)
                
    def cfgfileinterp(self,targetfile):
        targetfilelocation=os.path.join(self.cspath,"cstrike/cfg/KLUTCH.cfg")
        cfgfile = open(targetfilelocation,"r")
        for line in cfgfile.readlines():
            if re.search(r"\"[^\"]*\"[\s]*?\"[^\"]*\"", line):
                matches = re.search(r"\"([^\"]*)\"[\s]*?\"([^\"]*)\"", line)
                self.cfgsettings[matches.group(1)] = matches.group(2)
    
    def editres(self,targetfile):
        targetfilelocation=os.path.join(self.cspath,"cstrike/resource/UI",targetfile)
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
        targetfilelocation=os.path.join(self.cspath,"cstrike/cfg/KLUTCH.cfg")
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

#makedo.editcfg(makedo.cfgfiles[1])
#makedo.editres(makedo.resfiles[0])