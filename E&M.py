from Tkinter import *
from vectors import *
import math

E_NAUGHT = 8.854*(10**(-12))
K = 1/(4*math.pi*E_NAUGHT)

PP_X = 0
PP_Y = 1
RADIUS = 2
CHARGE = 3

def createPP(x, y, r, charge):
	#Simple error checking
	return (x, y, r, charge)

def e_field(x, y, pp): 
	"""Returns the electric field at a point from point particle pp"""
	e_mag = K*pp[CHARGE]/(distance(x, y, pp[PP_X], pp[PP_Y])**2)
	dx = x - pp[PP_X]
	dy = y - pp[PP_Y]
	scalar = e_mag/v2_mag((dx, dy))
	return v2_norm((dx*scalar, dy*scalar))

def e_field_total(x, y, pp_all):
	tot = (0, 0)
	for i in pp_all:
		tot = v2_sum(tot, e_field(x, y, i))
	return tot

def line_for_v2(v, x, y):
	#Error checking
	return (int(x), int(y), int(v[0]+x), int(v[1]+y))

#I foresee no problems with this function /s
def distance(x1, y1, x2, y2):
	return math.sqrt((x1-x2)**2 + (y1-y2)**2)

def test_pp_lines(canvas, pp):
	theta = 0
	rad = pp[RADIUS]
	while theta < 2*math.pi:
		x = pp[PP_X] + rad*math.cos(theta)
		y = pp[PP_Y] + rad*math.sin(theta)
		e = e_field(x, y, pp)
		l = line_for_v2(e, x, y)
		canvas.create_line(l[0], l[1], l[2], l[3], fill='blue')
		theta += math.pi/8

def test_all_pp_lines(canvas, pp_all, target):
	theta = 0
	pp = pp_all[target]
	rad = pp[RADIUS]
	while theta < 2*math.pi:
		x = pp[PP_X] + rad*math.cos(theta)
		y = pp[PP_Y] + rad*math.sin(theta)
		e = e_field_total(x, y, pp_all)
		l = line_for_v2(e, x, y)
		canvas.create_line(l[0], l[1], l[2], l[3], fill='blue')
		theta += math.pi/8

def draw_pp(canvas, pp):
	rad = pp[RADIUS]
	canvas.create_oval(pp[PP_X]-rad/2, pp[PP_Y]-rad/2, pp[PP_X]+rad/2, pp[PP_Y]+rad/2, fill="red", width=2)

all_pp = []
p1 = createPP(200/3.0, 50, 10, 0.000000001)
all_pp.append(p1)
p2 = createPP(400/3.0, 50, 10, 0.000000001)
all_pp.append(p2)
root = Tk()
w = Canvas(root, width=200, height=100)
draw_pp(w, p1)
draw_pp(w, p2)
w.pack()
test_all_pp_lines(w, all_pp, 0)
test_all_pp_lines(w, all_pp, 1)
root.mainloop()