####################################
###    MTTPA's Git Installer     ###
###    Development Launcher      ###
###   For  Testing  uses  only   ###
####################################

#I see your Curious if this is a virus or something
#Well I'll describe whats going on here in detail.

#First we bring in some things already built into python
import os, sys
#we then tell the cmd to clear
os.system('cls')
#we ask the system do either one of these file paths exist? If not then:
if (os.path.exists("C:/Program Files (x86)/Git/bin") == 0 and os.path.exists("C:/Program Files/Git/bin") == 0):
     #set the batch file color to red
     os.system("Color 04")
     #Print out these messages to the cmd for the user to read
     print("Git Is not installed! please install and run again\n")
     print("Git MUST be installed to the default directory")
     print("https://git-scm.com/download/win")
     #Exit Don't Keep Going.
     sys.exit()  
#Does This file exist? If not then:
if (os.path.isfile('dontrunme.bat') == 0):
        #Print out to cmd
		print("Checking for updates . . .")
        #Set Color to green 
		os.system("color 02")
		#Fetch the github repo for changes
		os.system("git fetch")
		#Force any modified files to be redownloaded/update
		os.system("git reset --hard origin/master")
#does this file exist? If It DOES then:
if (os.path.isfile('dontrunme.bat') == 1):
        #set Color To Gold
        os.system("color 06")
		#Print Out to cmd:
        print("running first time setup . . .")
        print("This will take a while.")
		#Run Batch File
        os.system('dontrunme.bat')	
#Set Color to Cyan
os.system("color 09")
#Print out to CMD
print("Done; Launching launcher")
#Launch the launcher this should have downloaded.
os.system("start launcher.bat")
#Exit
os.exit()