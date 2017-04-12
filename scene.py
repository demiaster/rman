#! /usr/bin/python
import getpass
import time
import prman
import math

ri = prman.Ri()

filename = "scene.rib"

ri.Begin(filename)

# set up the scene
ri.Display("scene.exr", "framebuffer", "rgba")
ri.Format(720, 575, 1)
ri.Projection(ri.PERSPECTIVE)

# set up the world

ri.WorldBegin()

ri.Translate(0, -1, 4)

# the pointy end

ri.TransformBegin()
end_height = 0.35
metal_radius = 0.06
ri.Translate(0, end_height, 0)
ri.TransformBegin()
ri.Rotate(90, 1, 0, 0)
ri.Cone(end_height, metal_radius, 360)
ri.TransformEnd()

#the metal thing
metal_height = 0.9
ri.TransformBegin()
ri.Rotate(-90, 1, 0, 0)
ri.Cylinder(metal_radius, 0, metal_height, 360)
ri.TransformEnd()

# base for bowly shaped thing
ri.TransformBegin()
ri.Translate(0, metal_height, 0)
ri.TransformBegin()
ri.Rotate(-90, 1, 0, 0)
disk_radius = 0.45
ri.Disk(0, disk_radius, 360)
ri.TransformEnd()

# bowly thing


ri.TransformEnd()
ri.TransformEnd()
# end of the world
ri.WorldEnd()

# end of rib file
ri.End()

