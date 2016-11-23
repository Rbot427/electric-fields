from Tkinter import *
from vectors import *

ARROW_DISTANCE = 100 #Measured in pixels
ARROW_LENGTH = 3
ARROW_BODY_LENGTH = 5

PP_X = 0
PP_Y = 1
RADIUS = 2
CHARGE = 3

def draw_arrow(canvas, x, y, v):
	v_perp = v2_norm(v2_perp(v))
	canvas.create_line(x, y, (x-v[0]*ARROW_BODY_LENGTH) + ARROW_LENGTH*v_perp[0], (y-v[1]*ARROW_BODY_LENGTH) + ARROW_LENGTH*v_perp[1], fill="red")
	canvas.create_line(x, y, (x-v[0]*ARROW_BODY_LENGTH) - ARROW_LENGTH*v_perp[0], (y-v[1]*ARROW_BODY_LENGTH) - ARROW_LENGTH*v_perp[1], fill="red")

def draw_pp(canvas, pp):
	rad = pp[RADIUS]
	f = "red"
	if pp[CHARGE] < 0: f = "blue"
	canvas.create_oval(pp[PP_X]-rad, pp[PP_Y]-rad, pp[PP_X]+rad, pp[PP_Y]+rad, fill=f, width=2)