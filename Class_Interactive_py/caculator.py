
import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

# calculator

# initial globals
store = 0
operand = 0

# event handlers for calculator with a store and operand

def output():
	print "store = ", store
	print "operand = ", operand
	print " "

def swap():
	global store, operand
	store, operand = operand, store
	output()

def sub():
	global store
	store = store - operand
	output()

def mult():
	global store
	store = store * operand
	output()

def div():
	global store
	store = store / operand
	output()

def  add():
	global store
	store = store + operand
	output()

def enter(inp):
	global operand
	operand = int(inp)
	output()


# create frame

f = simplegui.create_frame("Calculator",300,300)

# register event handlers
f.add_button("Print", output, 100)
f.add_button("Swap", swap, 100)
f.add_button("Add", add, 100)
f.add_button("Sub", sub, 100)
f.add_button("Mult", mult, 100)
f.add_button("Div", div, 100)
f.add_input("Enter operand", enter, 100)

# get frame rolling
f.start()
