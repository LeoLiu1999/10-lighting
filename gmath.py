import math
from display import *

AMBIENT = 0
DIFFUSE = 1
SPECULAR = 2
LOCATION = 0
COLOR = 1
SPECULAR_EXP = 4

#lighting functions
def get_lighting(normal, view, ambient, light, areflect, dreflect, sreflect ):
    normalize(normal)
    normalize(view)
    normalize(light[LOCATION])

    
    ambi = limit_part_color(calculate_ambient(ambient, areflect))
    diff = limit_part_color(calculate_diffuse(light, dreflect, normal))
    spec = limit_part_color(calculate_specular(light, sreflect, view, normal))
    
    r = limit_final_color(ambi[0] + diff[0] + spec[0])
    g = limit_final_color(ambi[1] + diff[1] + spec[1])
    b = limit_final_color(ambi[2] + diff[2] + spec[2])

    return [r,g,b]

def calculate_ambient(alight, areflect):
    return map(lambda x: x[0] * x[1], zip(alight, areflect))

def calculate_diffuse(light, dreflect, normal):
    return map(lambda x: x[0] * x[1] * dot_product(normal, light[LOCATION]), zip(dreflect, light[COLOR]))

def calculate_specular(light, sreflect, view, normal):
    #return [0,0,0]
    pass
    

def limit_final_color(color):
    return 255 if color > 255 else int(color)

def limit_part_color(color):
    for c in color:
        if color < 0:
            color = 0
    return color

#vector functions
def normalize(vector):
    length = vector[0]**2 + vector[1]**2 + vector[2]**2
    for dimention in vector:
        dimention /= length

def dot_product(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]

def calculate_normal(polygons, i):

    A = [0, 0, 0]
    B = [0, 0, 0]
    N = [0, 0, 0]

    A[0] = polygons[i+1][0] - polygons[i][0]
    A[1] = polygons[i+1][1] - polygons[i][1]
    A[2] = polygons[i+1][2] - polygons[i][2]

    B[0] = polygons[i+2][0] - polygons[i][0]
    B[1] = polygons[i+2][1] - polygons[i][1]
    B[2] = polygons[i+2][2] - polygons[i][2]

    N[0] = A[1] * B[2] - A[2] * B[1]
    N[1] = A[2] * B[0] - A[0] * B[2]
    N[2] = A[0] * B[1] - A[1] * B[0]

    return N
