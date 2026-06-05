import maya.cmds as cmds
import math

# Parameters
radius = 5.0
pitch = 2.0
turns = 4.0
segments = 100

c = pitch / (2 * math.pi)
t_max = turns * 2 * math.pi
points = []

for i in range(segments + 1):
    t = (float(i) / segments) * t_max
    x = radius * math.cos(t)
    z = radius * math.sin(t) # Maya standard default up-axis is Y
    y = c * t
    points.append((x, y, z))

# Generate the curve curve degree 3
cmds.curve(p=points, degree=3)
