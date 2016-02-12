"""Calculate the detour distance between two different rides. Given four
   latitude / longitude pairs, where driver one is traveling from point A to
   point B and driver two is traveling from point C to point D, write a function
   (in your language of choice) to calculate the shorter of the detour distances
   the drivers would need to take to pick-up and drop-off the other driver.
    
.. module:: detour
   :synopsis: Calculates the detour distance between two different rides.
    
.. moduleauthor:: Alexander Simeonov
    
"""

from math import asin, cos, radians, sin, sqrt
from sys import argv, exit


EARTH_RADIUS = 6371 # Kilometers

def distance(a, b):
    """Calculates the distance between two latitude / longitude pairs on Earth.

    :param (float, float) a: point a - latitude / longitude pair
    :param (float, float) b: point b - latitude / longitude pair
    :returns: distance in kilometers
    :rtype: float
      
    """
    # Convert to radians
    a = tuple(map(radians, a))
    b = tuple(map(radians, b))
    
    # Delta between the points
    delta = tuple(x - y for x, y in zip(a, b))
    
    # Haversine distance
    h = sin((delta[0]/2)**2) + (cos(a[0]) * cos(b[0]) * (sin(delta[1]/2)**2))
    return 2 * EARTH_RADIUS * sqrt(h)

def detour(a, b, c, d):
    """Calculates the shorter of the detour distances the drivers would need to
    take to pick-up and drop-off the other driver.
    
    :param (float, float) a: point A - latitude / longitude pair
    :param (float, float) b: point B - latitude / longitude pair
    :param (float, float) c: point C - latitude / longitude pair
    :param (float, float) d: point D - latitude / longitude pair
        
    """
    ab = distance(a, b)
    cd = distance(c, d)

    if ab > cd:
        ac = distance(a, c)
        db = distance(d, b)
        acdb = ac + cd + db
        print(("Driver one - A->C->D->B: " + str(acdb) + " km"))
    else:
        ca = distance(c, a)
        bd = distance(b, d)
        cabd = ca + ab + bd
        if cd > ab:
            print(("Driver two - C->A->D->B: " + str(cabd) + " km"))
        else:
            print(("Either driver (equivalent distances): " + str(cabd) + " km"))

# Make sure we have the correct command line arguments
if len(argv) != 9:
    print("Please provide command line arguments as follows:")
    print("python detour.py latA longA latB longB latC longC latD longD")
    exit(0)

# Calculate the shorter of the detour distances
detour((float(argv[1]), float(argv[2])),
       (float(argv[3]), float(argv[4])),
       (float(argv[5]), float(argv[6])),
       (float(argv[7]), float(argv[8])))
