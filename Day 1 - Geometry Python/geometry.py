import math

ongoing = True

class Circle():

    pi = math.pi
    circumferenceFormula = '2π * r'
    areaFormula = 'π * r**2'

    def __init__(self, r=1):

        self.r = r

    def __str__(self):

        return f'''
The circumference of a circle is calculated by {self.circumferenceFormula}
The area of a circle is calculated by {self.areaFormula}
                '''

    def circumference(self):

        print(f'Calculating {self.circumferenceFormula}')
        return 2 * math.pi * self.r

    def area(self):

        print(f'Calculating {self.areaFormula}')
        return math.pi * self.r**2

def calculateCircle(x):

    if x == 'a':

        radius = int(input('What is the radius? '))
        circle = Circle(radius)
        area = circle.area()
        return area

    elif x == 'c':

        radius = int(input('What is the radius? '))
        circle = Circle(radius)
        circumference = circle.circumference()
        return circumference

# circle = Circle(3)
# print(circle)
# print(circle.circumference())


while ongoing:

    shape = input('What shape do you want? Circle = ci. (q to quit) ').lower()

    if shape == 'ci':

        circle = Circle()
        print(circle)
        geo = input('Do you want the area or the circumference? a = area, c = circumference. (q to quit) ').lower()

        if geo == 'a':

            result = calculateCircle('a')
            print(result)

        elif geo == 'c':

            result = calculateCircle('c')
            print(result)

        elif geo == 'q':

            ongoing = False
            break



    elif shape == 'q':

        ongoing = False
        break

    else:
        continue
