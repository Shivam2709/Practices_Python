# Problem: Create a function that returns both the area and circumference of a circle given its radius.

import math

def circle(radius):
    area = math.pi * (radius ** 2)
    circumferance = 2 * (math.pi * radius)

    return area, circumferance


a, c = circle(5)
Area = round(a, 2)
Circumferance = round(c, 2)

print('Area', Area, 'Circumferance', Circumferance)