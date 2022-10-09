from collections import namedtuple

Point = namedtuple("Point", "x,y")

# Create Class of Point
pt = Point(2, 3)

print(pt, pt.x, pt.y)
