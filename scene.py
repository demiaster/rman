#! /usr/bin/python
import getpass
import time
import prman
import math

def hyperboloid_wrapper(height, base_radius, top_radius):
    ri.TransformBegin()
    ri.Rotate(-90, 1, 0, 0)
    p_base = [base_radius, 0, 0]
    p_top = [top_radius, 0, height]
    ri.Hyperboloid(p_base, p_top, 360)
    ri.TransformEnd()

ri = prman.Ri()

filename = "scene.rib"

ri.Begin(filename)

# set up the scene
ri.Display("scene.exr", "framebuffer", "rgba")
ri.Format(720, 575, 1)
ri.Projection(ri.PERSPECTIVE)

# set up the world

ri.WorldBegin()

ri.Translate(0, -1.5, 4)

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
ri.TransformBegin()
bowl_radius = 0.47
ri.Translate(0, -0.05, 0)
ri.Rotate(-90, 1, 0, 0)
y_max = 0.433
y_min = 0.05
ri.Sphere(bowl_radius, y_min, y_max, 360)
ri.TransformEnd()

# plastic body
ri.TransformBegin()
ri.Translate(0, y_max - y_min, 0)
body_height = 0.7
body_br = 0.2
body_tr = 0.15
hyperboloid_wrapper(body_height, body_br, body_tr)

# top base (tb)
ri.TransformBegin()
ri.Translate(0, body_height, 0)
tb_height = 0.08
tb_tr = 0.375
hyperboloid_wrapper(tb_height, body_tr, tb_tr)

# top top (tt)
ri.TransformBegin()
ri.Translate(0, tb_height, 0)
tt_tr = 0.35
hyperboloid_wrapper(tb_height, tb_tr, tt_tr)

# top cup (tc)
ri.TransformBegin()
ri.Translate(0, tb_height, 0)
ri.TransformBegin()
ri.Rotate(-90, 1, 0, 0)
tc_radius = tt_tr
ri.Disk(0, tc_radius, 360)
ri.TransformEnd()

ri.TransformEnd()
ri.TransformEnd()
ri.TransformEnd()
ri.TransformEnd()
ri.TransformEnd()
ri.TransformEnd()

# end of the world
ri.WorldEnd()

# end of rib file
ri.End()

