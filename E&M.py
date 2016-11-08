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
	return (dx*scalar, dy*scalar)

def e_field_total(x, y, pp_all):
	tot = (0, 0)
	for i in pp_all:
		tot = v2_sum(tot, e_field(x, y, i))
	return v2_norm(tot)

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
		draw_full_field_line(canvas, pp_all, x, y)
		theta += math.pi/8

def draw_full_field_line(canvas, pp_all, x, y):
	c = 0
	while c < 5000:
		e = e_field_total(x, y, pp_all)
		l = line_for_v2(e, x, y)
		canvas.create_line(l[0], l[1], l[2], l[3], fill='blue')
		x = x + e[0]
		y = y + e[1]
		c += 1

def draw_pp(canvas, pp):
	rad = pp[RADIUS]
	f = "red"
	if pp[CHARGE] < 0: f = "blue"
	canvas.create_oval(pp[PP_X]-rad, pp[PP_Y]-rad, pp[PP_X]+rad, pp[PP_Y]+rad, fill=f, width=2)

all_pp = []
p1 = createPP(600/3.0, 200, 10, 0.000000001)
all_pp.append(p1)
p2 = createPP(399, 200, 10, -0.000000001)
all_pp.append(p2)
#p3 = createPP(150, 75, 10, 0.000000001)
#all_pp.append(p3)
#p4 = createPP(300, 150, 10, 0.000000001)
#all_pp.append(p4)
root = Tk()
w = Canvas(root, width=600, height=400)
w.pack()

draw_pp(w, p1)
draw_pp(w, p2)
#draw_pp(w, p3)
#draw_pp(w, p4)

test_all_pp_lines(w, all_pp, 0)
#test_all_pp_lines(w, all_pp, 1)
#test_all_pp_lines(w, all_pp, 2)
#test_all_pp_lines(w, all_pp, 3)
root.mainloop()