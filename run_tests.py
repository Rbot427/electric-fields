from Tkinter import *
from E_and_M import *

all_pp = []
p1 = createPP(600/3.0, 200, 10, 0.000000001)
all_pp.append(p1)
p2 = createPP(399, 50, 10, 0.000000001)
all_pp.append(p2)
p3 = createPP(150, 75, 10, -0.000000001)
all_pp.append(p3)
#p4 = createPP(300, 150, 10, 0.000000001)
#all_pp.append(p4)
root = Tk()
w = Canvas(root, width=600, height=400)
w.pack()
#Test
draw_pp(w, p1)
draw_pp(w, p2)
#draw_pp(w, p4)

test_all_pp_lines(w, all_pp, 0)
test_all_pp_lines(w, all_pp, 1)
draw_pp(w, p3)
#test_all_pp_lines(w, all_pp, 2)
#test_all_pp_lines(w, all_pp, 3)
root.mainloop()