import math
import numpy as np

class Point:
    # The Point class has 2 main objectives. One is to initiated the object with x and y. second is to check if the point is in the regtangle
    # This is a special function __init__ to hold the parameter of the object we are specifying for the class
    def __init__(self, x, y):
        # self here is refered to the object initiated by the class parent, we could name it any name, i.e my_object, self_object
        # if you print self, it return to the object created by initiating the parent class
        # x and y outside the function when we call it is arguments, then self.x and self.y is the attribute of the object
        self.x = x
        self.y = y
    # Now we are defining the method of the class, belong to the object created
    def falls_in_rectangle(self, rectangle):
        # Note that in every method, we need self to declaire it belongs to the class as a method, and that holds the object instance
        if rectangle.lowleft.x < self.x < rectangle.upright.x and rectangle.lowleft.y < self.y < rectangle.upright.y:
            # compare the x-corrdinate and y-corrdinate
            return True
        else:
            return False
    # Now add the distance method to calculate the distance from coordinates to current point (X, Y)
    def distance_from_origin(self):
        return math.sqrt((self.x)**2 + (self.y)**2)
    # Add method to calculate the distance of the point object to the new point
    def distance_from_point(self, x, y):
        # Here remember that the self.x and self.y is the attribute of the object, while x and y are input arguments
        return math.sqrt((self.x - x)**2 + (self.y - y)**2)
    # We could do the method to calcualte distance from several point object
    def distance_from_point_object(self, point):
        x = point.x
        y = point.y
        return math.sqrt((self.x - x)**2 + (self.y - y)**2)

class Rectangle:
    # The Rectangle class has 2 objectives:
    # 1st to initiate the object characterizing the rectangle. We need 2 points: lowleft(x,y) and upright(x,y) to form a rectangle
    def __init__(self, lowleft, upright):
        self.lowleft = lowleft
        self.upright = upright
    # Note that the lowleft and upright are two points --> we can use class Point to initiate the object
    # Create method to calcualte the area of the regtable
    def area(self):
        area = (self.upright.x - self.lowleft.x) * (self.upright.y - self.lowleft.y)
        return area
