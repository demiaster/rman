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

ri.Translate(0, 0, 2)

# the pointy end
ri.TransformBegin()
end_height = 0.3
ri.Translate(0, end_height, 0)
ri.Rotate(90, 1, 0, 0)
ri.Cone(end_height, 0.1, 360)
ri.TransformEnd()

#the metal thing
#ri.TransformBegin()
#ri.Rotate(-90, 1, 0, 0)
#ri.Cilinder(0.3, 0.1, 360)
#ri.TransformEnd()

# end of the world
ri.WorldEnd()

# end of rib file
ri.End()

