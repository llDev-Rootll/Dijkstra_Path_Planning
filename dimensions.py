import math

x_max = 400
y_max = 250 

sixty = math.pi/3
h1 = [200, 100+(35/math.sin(sixty))]
h2 = [235, 100+(35/math.tan(sixty))]
h3 = [235, 100-(35/math.tan(sixty))]
h4 = [200, 100-(35/math.sin(sixty))]
h5 = [165, 100-(35/math.tan(sixty))]
h6 = [165, 100+(35/math.tan(sixty))]
h1_i = [200, 100+(35/math.sin(sixty))+5]
h2_i = [235+5, 100+(35/math.tan(sixty))+5]
h3_i = [235+5, 100-(35/math.tan(sixty))-5]
h4_i = [200, 100-(35/math.sin(sixty))-5]
h5_i = [165-5, 100-(35/math.tan(sixty))-5]
h6_i = [165-5, 100+(35/math.tan(sixty))+5]




p1 = [36, 185]
p2 = [115, 210]
p3 = [80, 180]
p4 = [105, 100]
p1_i = [31, 185]
p2_i = [120+5/math.cos(math.pi/5), 210+5/math.sin(math.pi/5)]
p3_i = [85, 180]
p4_i = [105+5/math.cos(math.pi/5), 100-5/math.sin(math.pi/5)]


centre = [300, 185]
radius = 40
radius_i = 45