#! /usr/bin/python

import prman

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

ri.Sphere(1, -1, 1, 360)

# end of the world
ri.WorldEnd()

# end of rib file
ri.End()

