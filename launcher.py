####################################
###  This is Toontown Journey's  ###
###    Development Launcher      ###
###   For  Testing  uses  only   ###
####################################
#Start Updater BEFORE launching GUI
import os, sys
os.system('cls')
if (os.path.exists("git") == 0):
     os.system("Color 04")
     print("You failed to follow instructions")
     print("You're installer is invalid please re-extract")
     sys.exit()  
if (os.path.isfile('FirstTimeSetup.bat') == 0):
		print("Checking for updates . . .")
		os.system("color 02")
		os.system("git/bin/git fetch")
		os.system("git/bin/git reset --hard origin/master")
if (os.path.isfile('FirstTimeSetup.bat')):
        os.system("color 06")
        print("running first time setup . . .")
        print("This will take a while.")
        os.system('FirstTimeSetup.bat')	
else (print("uhhh I honestly don't know how its possible you\n are seeing this."))
os.system('cls')
os.system("color 09")
print("Done; Launching launcher")

from panda3d.core import *
loadPrcFileData("", "window-title Mr. Tankthrusts Toontown: Project Altis Modifications")
loadPrcFileData("", "win-size 1200 600")
loadPrcFileData("", "win-origin 200 200")
import direct.directbase.DirectStart
from direct.gui.DirectGui import *
from uuid import getnode as get_mac
#get mac adress used later
mac = str(hex(get_mac()))

background=OnscreenImage(image = 'resources/phase_3/maps/background.jpg', pos = (0, 0, 0),parent=render2d)
background.setTransparency(TransparencyAttrib.MAlpha)

logo=OnscreenImage(image = 'resources/phase_3/maps/toontown-logo.png', pos = (0, 0, .2),parent=render2d)
logo.setTransparency(TransparencyAttrib.MAlpha)
logo.setScale(0.5)

buttonup=OnscreenImage(image = 'resources/launcher/Button_Up.png', pos = (0, 0, 0))
buttonup.setTransparency(TransparencyAttrib.MAlpha)
buttonup.setScale(0.0)

buttondown=OnscreenImage(image = 'resources/launcher/Button_Down.png', pos = (0, 0, 0))
buttondown.setTransparency(TransparencyAttrib.MAlpha)
buttondown.setScale(0.0)

username = mac
ip = "gs2.toontownjourney.com"
#setup mythod to to ask for user input
	
def setIp(textEntered):
    global ip
    ip__t.hide()
    ip_b.hide()
    play_b.show()
    ip = textEntered

#Add IP Address Box
ip_b = DirectEntry(text = "" ,scale=.05,command=setIp,\
pos = (-.35, 0, -.48 ), numLines = 1,width=15,obscured=0)

ip_t = TextNode('ip')
ip__t = aspect2d.attachNewNode(ip_t)
ip__t.setScale(0.07), ip_t.setText("ip:")
ip__t.setPos(-.45 , 0, -.48 ), ip_t.setShadow(0.10, 0.10), ip_t.setShadowColor(0, 0, 0, 1)

def launch():

    #Preparing for launching
	#Cheap way of killing the launcher XD
	os.environ['launcher'] = str(os.getpid())
	os.environ['islauncher'] = str("1")
	
	#Grabbing the play cookie(YUMMY COOKIE :D)
	#also takes the game server here too
	os.environ['TT_PLAYCOOKIE'] = str(mac)
	
	os.environ['TT_GAMESERVER'] = str(ip)
	#Tell it where PPYTHON.exe is
	os.system('set /P PPYTHON_PATH=<PPYTHON_PATH')
	
	#and LAUNCH the game
	os.system('%PPYTHON_PATH%' + ' -m toontown.toonbase.ClientStart')	

#setting up the play button
play_b = DirectButton(frameSize=None, image=(buttonup,buttondown,buttonup), relief=None,  
command=launch, pos = (0, 0, -.7 ), scale=0.27)

#start the GUI
base.run()
