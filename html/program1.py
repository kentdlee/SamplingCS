R1_width = 10
R1_height = 8

R2_height = R1_height + 3 - 2
R2_width = 4 + R1_width - 9

R1_area = R1_width * R1_height
R2_area = R2_width * R2_height

totalArea = R1_area + R2_area - 1 * 6

print "R2's height is",R2_height
print "R2's width is",R2_width
print "The total area of the polygon is"
print totalArea, "square meters."
