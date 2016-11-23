from Tkinter import *
from vectors import *
from visuals import *
import math

E_NAUGHT = 8.854*(10**(-12))
K = 1/(4*math.pi*E_NAUGHT)

PP_X = 0
PP_Y = 1
RADIUS = 2
CHARGE = 3
DELTAV_TOLERANCE = 0.1

W_WIDTH = 600
W_HEIGHT = 400

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
	dist = 0
	while c < 1000:
		e = e_field_total(x, y, pp_all)
		l = line_for_v2(e, x, y)
		canvas.create_line(l[0], l[1], l[2], l[3], fill='blue')
		x = x + e[0]
		y = y + e[1]
		dist += v2_mag(e) #Since I normalize, this will always be 2
		if not inBounds(x,y) or in_any_pp(x, y, pp_all): return
		if dist >= ARROW_DISTANCE: 
			#canvas.create_oval(x, y, x + 4, y + 4, fill='red', width=2)
			draw_arrow(canvas, x, y, e)
			dist = 0
		c += 1


def get_voltage_at_point(x, y, pp_all):
	v = 0
	for pp in pp_all:
		if distance(x, y, pp[PP_X], pp[PP_Y]) == 0: return None
		v += K*pp[CHARGE]/abs(distance(x, y, pp[PP_X], pp[PP_Y]))
	return v

#returns a matrix of voltage values at every point
def get_voltage_matrix(canvas, pp_all):
	voltage_matrix = [[None for i in range(600)] for j in range(400)]
	for rowNum in range(len(voltage_matrix)):
		for colNum in range(len(voltage_matrix[0])):
			voltage_matrix[rowNum][colNum] = get_voltage_at_point(rowNum, colNum, pp_all)
	return voltage_matrix

def get_color_of_equipotential_line(voltage):
	if voltage==0: return 'orange'
	if voltage > 0: return 'red'
	return 'green'

def draw_equipotential_line(canvas, voltage_matrix, voltage):
	for height in range(len(voltage_matrix) - 1):
		for width in range(len(voltage_matrix[0])-1):
			if voltage_matrix[height][width] != None:
				if voltage_matrix[height+1][width]!=None and ((voltage_matrix[height][width] >= voltage and voltage_matrix[height+1][width] <= voltage) or (voltage_matrix[height][width] <= voltage and voltage_matrix[height+1][width] >= voltage)):
					#deltaV = abs(voltage_matrix[height][width] - voltage_matrix[height+1][width])
					canvas.create_line(height, width, height+1, width+1, fill=get_color_of_equipotential_line(voltage))
				elif voltage_matrix[height][width+1]!=None and ((voltage_matrix[height][width] >= voltage and voltage_matrix[height][width+1] <= voltage) or (voltage_matrix[height][width] <= voltage and voltage_matrix[height][width+1] >= voltage)):
					#deltaV = abs(voltage_matrix[height][width] - voltage_matrix[height][width+1])
					canvas.create_line(height, width, height+1, width+1, fill=get_color_of_equipotential_line(voltage))

def in_any_pp(x, y, pp_all):
	for pp in pp_all:
		if inPP(x, y, pp): return True
	return False

def inPP(x, y, pp):
	return distance(x, y, pp[PP_X], pp[PP_Y]) <= pp[RADIUS]

def inBounds(x, y):
	return (x >= 0 or x <= W_WIDTH) and (y >= 0 or y <= W_HEIGHT)

