from Tkinter import *
import math
import os

E_NAUGHT = 8.854*(10**(-12))
K = 1/(4*math.pi*E_NAUGHT)
CHARGE = 3
RADIUS = 2
PP_X = 0
PP_Y = 1
NORM_MAG = 30

def createPP(x, y, r, charge):
	#Simple error checking
	return (x, y, r, charge)

def e_field(x, y, pp): #return a magnitude or components of a vector?
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

def v2_mag(v):
	#Error checking
	return math.sqrt(v[0]**2 + v[1]**2)

def v2_norm(v):
	#Error checking
	mag = float(v2_mag(v))
	return (NORM_MAG*v[0]/mag, NORM_MAG*v[1]/mag)

def v2_sum(v1, v2):
	return (v1[0] + v2[0], v1[1] + v2[1])

def line_for_v2(v, x, y):
	#Error checking
	return (int(x), int(y), int(v[0]+x), int(v[1]+y))

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

def draw_pp(canvas, pp):
	rad = pp[RADIUS]
	canvas.create_oval(rad, rad, pp[PP_X], pp[PP_Y], fill="red", width=2)

p = createPP(100, 50, 10, 0.000000001)
root = Tk()
w = Canvas(root, width=200, height=100)
draw_pp(w, p)
w.pack()
test_pp_lines(w, p)
root.mainloop()