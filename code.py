import fileinput
	
	
def guffyInput(msg=""):
	if(msg != ""):
		print(msg)

	try:
		return _GetCharWindows()
	except ImportError:
		return _GetCharUnix()
		
def _GetCharUnix():
	import sys, tty, termios
	fd = sys.stdin.fileno()
	old_settings = termios.tcgetattr(fd)
	try:
		tty.setraw(sys.stdin.fileno())
		ch = sys.stdin.read(1)
	finally:
		termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
	return ch
	
def _GetCharWindows():
	import msvcrt
	return msvcrt.getch()


if(__name__=="__main__"):
	c = guffyInput("Enter A or K")
	print(c)