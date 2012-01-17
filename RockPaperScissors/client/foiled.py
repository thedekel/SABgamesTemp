import curses

# call at beginning
def init():
	global screen
	screen = curses.initscr()

# displays multipe lines of text with a prompt at the end
def text(message):
	screen.clear()
	msg = message.split("\n")
	i = 0
	for k in range(0, len(msg)):
		screen.addstr(i+2, 2, msg[i])
		i+=1
	screen.addstr(i+4, 2, "Press any key to continue...")
	screen.getch()

# displays a line of information
def info(message):
	screen.addstr(message+"\n")
	screen.refresh()

# gets input from the user
def get_param(prompt):
	screen.clear()
	screen.addstr(2, 2, prompt)
	screen.refresh()
	return screen.getstr(4, 4, 60)

# creates a menu, returns the number of the menu item the user selected
def menu(prompt, *args):
	curses.noecho()
	screen.clear()
	screen.addstr(2, 2, prompt)
	for i in range(0, len(args)):
		screen.addstr(2*(i+1)+2, 4, "%i. %s" % (i+1, args[i]))
	screen.refresh()
	a = -1
	while not(0 < a <= len(args)):
		a = screen.getch()-48
	curses.echo()
	return a

# call at end
def exit():
	curses.endwin()
