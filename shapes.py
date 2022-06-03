from cmath import pi

class Circle:
    

    def __init__(self,radius):
        self.radius= radius


        
    
    def area_of_circle(self):
        area = pi*self.radius**2
        return area


    def circumference_of_circle(self):

        circumference = 2*pi*self.radius

        return circumference


class Square:

    def __init__(self,a):
        self.a = a
    

    
    def area_of_square(self):
        area = self.a**2
        return area


    def perimeter_of_square(self):
        perimeter = 4*self.a
        return perimeter


class Rectangle:
    def __init__(self,width,length):
        self.width = width
        self.length = length


    def area_of_rectangle(self):

        area = self.width*self.length
        return area

    def peremiter_of_rectangle(self):

        perimeter = 2*(self.width+self.length)
        return perimeter


class Sphere:
    def __init__(self, radius):
        self.radius = radius

    def surface_area(self):
        sa =  4 * pi* self.radius * self.radius
        return sa

    def volume(self):
        Volume = (4 / 3) * pi * self.radius * self.radius * self.radius

