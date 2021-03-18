import math
class Point(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y
class Line(Point):
    def Length (self,x1,y1,x2,y2):
        return math.sqrt((x1+x2)**2+(y1+y2)**2)
x=input("Insert the coordinates: \n")
x=x.split(" ")
point1=Point(float(x[0]),float(x[1]))
point2=Point(float(x[2]),float(x[3]))
len=Line(point1, point2)
print(len.Length(point1.x, point2.x, point1.y, point2.y))
