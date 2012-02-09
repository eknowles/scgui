#!/usr/bin/python
import os, os.path
import shutil
import re
import filecmp

source_file = r"C:\Users\Edward\Desktop\GUI\Source"
destination = r"C:\Users\Edward\Desktop\GUI\Destination"
steamname = "3fk"


def getinstalledskin(steamname):
    targetfilelocation=os.path.join('C:\Program Files (x86)\Steam\steamapps',steamname,'counter-strike source\cstrike\cfg\KLUTCH.cfg')
    maincfg = open(targetfilelocation,"r")
    for line in maincfg.readlines():
        if re.search(r"// \[[^\]]*?=[^\]]*?\]", line):
            matches = re.search(r"// \[Skin=([^\s]*?)\]", line)
            if matches is not None:
                installedskin = matches.group(1)
                print installedskin


## This will copy a folder to the cstrike bit
def installskin(src, dst):    
    names = os.listdir(src)
    if not os.path.exists(dst): # no error if already exists
        os.makedirs(dst)
    errors = []
    for name in names:
        srcname = os.path.join(src, name)
        dstname = os.path.join(dst, name)
        try:
            if os.path.isdir(srcname):
                shutil.copytree(srcname, dstname)
            else:
                shutil.copy2(srcname, dstname)
        except (IOError, os.error), why:
            errors.append((srcname, dstname, str(why)))
        # catch the Error from the recursive copytree so that we can
        # continue with other files
        
installskin(source_file, destination)
getinstalledskin(steamname)