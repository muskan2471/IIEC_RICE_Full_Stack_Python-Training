import os

while True:
	print("Chat With Me with Your requirment of opening application :" ,end='') #ask user to enter its reqirement
	str=input()								# take input of user
	
	if("exit" in str or "quit" in str or "shut down" in str ):
		break
	elif( str.__contains__("not") or str.__contains__("dont") or str.__contains__("never") or str.__contains__("do not")):
		pass

	elif ( ("run" in str) or ("execute" in str) or ("open" in str) or ("start" in str) ):
		if(  ("chrome" in str) or ("Google Chrome" in str) or ("web browser" in str) ):
			os.system("chrome")
		elif ( ("notepad" in str) or ("editor" in str) or ("text editor" in str) ):
			os.system("notepad")
		elif ( ("microsoft edge" in str) or ("edge browser" in str)):
			os.sysetm("msedge")
		elif( ("vlc player" in str) or ("vlc" in str)or ("vlc media player" in str)  ):
			os.system("vlc")
		elif ( ("windows media player" in str) or ("windows player" in str) or ("media player" in str) ):
			os.system("wmplayer")
		else :
			print("this application is not installed")
	
	
	