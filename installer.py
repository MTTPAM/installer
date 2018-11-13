#################################
#    MTTPAM's Git Installer     #
#     Development Launcher      #
#   For  Testing  uses  only    #
#################################

import os
import sys
dev = False
if os.path.exists("C:/Program Files (x86)/Git/bin") == 0 and os.path.exists("C:/Program Files/Git/bin") == 0:
    os.system("Color 04")
    print("Git Is not installed! please install and run again\n")
    print("Git MUST be installed to the default directory")
    print("https://git-scm.com/download/win")
    sys.exit()
else:
    os.system("color 06")
    print("running first time setup . . .")
    print("This will take a while.")
    if dev:
        print("intitalizing Git")
    os.system("git init .")
    if dev:
        print("adding remote repo")
    os.system("git remote add origin https://github.com/MTTPAM/PublicRelease.git")
    if dev:
        print("Fetching files, and updating.")
    os.system("git fetch --all")
    os.system("git reset --hard")
    os.system("color 09")
    print("Done; Launching launcher")
    os.system("del installer.py /A")
    os.system("del installer.bat /A")
    os.system("start launcher.bat")
os.exit()
