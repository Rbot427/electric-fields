from Tkinter import *
from E_and_M import *

WIDTH = 600
HEIGHT = 400

all_pp = []
p1 = createPP(200, 200, 10, 0.000000001)
all_pp.append(p1)
p2 = createPP(400, 200, 10, -0.000000001)
all_pp.append(p2)

root = Tk()
w = Canvas(root, width=WIDTH, height=HEIGHT)
w.pack()

draw_pp(w, p1)
draw_pp(w, p2)


test_all_pp_lines(w, all_pp, 0)
test_all_pp_lines(w, all_pp, 1)

vm = get_voltage_matrix(w, all_pp)
draw_equipotential_line(w, vm, 0.1)
draw_equipotential_line(w, vm, 0.2)

root.mainloop()
