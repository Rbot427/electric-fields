import math

NORM_MAG = 2

def v2_mag(v):
	#Error checking
	return math.sqrt(v[0]**2 + v[1]**2)

def v2_norm(v):
	#Error checking
	mag = float(v2_mag(v))
	return (NORM_MAG*v[0]/mag, NORM_MAG*v[1]/mag)

def v2_sum(v1, v2):
	return (v1[0] + v2[0], v1[1] + v2[1])

def v2_scalar_multiple(s, v):
	return (v[0]*s, v[1]*s)

def test_v2_norm():
	v = (0.1, 0.1)
	print v2_norm(v)

