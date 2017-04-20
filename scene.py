#! /usr/bin/python
import getpass
import time
import prman
import math

#function for hyperboloid shapes in the pin
def hyperboloid_wrapper(height, base_radius, top_radius):
    ri.TransformBegin()
    ri.Rotate(-90, 1, 0, 0)
    p_base = [base_radius, 0, 0]
    p_top = [top_radius, 0, height]
    ri.Hyperboloid(p_base, p_top, 360)
    ri.TransformEnd()

#the instance for renderman
ri = prman.Ri()

filename = "scene.rib"

ri.Begin(filename)

ri.Declare("Ambient" ,"string")
ri.Declare("Light1" ,"string")
ri.Declare("Light2" ,"string")
ri.Declare("Light3" ,"string")



# set up the scene
ri.Display("scene.exr", "framebuffer", "rgba")
ri.Format(720, 575, 1)
ri.Projection(ri.PERSPECTIVE)

# set up the world
ri.WorldBegin()

# place the lights
ri.LightSource("ambientlight", {ri.HANDLEID:"Ambient", "float intensity": [0.1]})

ri.LightSource( "pointlight", {ri.HANDLEID:"Light1", "point from":[-2,2,4], "float intensity": [13]})

ri.TransformBegin()
ri.Translate(2,2,4)
ri.LightSource("pointlight", {ri.HANDLEID:"Light2", "point from":[0,0,0] ,"float intensity" :[17]})
ri.TransformEnd()

ri.TransformBegin()
ri.LightSource("pointlight",{ri.HANDLEID: "Light3","point from": [2,1,3] ,"float intensity": [7]})

# turn on the lights
ri.Illuminate("Light1",1)
ri.Illuminate("Light2",1)
ri.Illuminate("Light3",1)

#adjust camera position
ri.Translate(0, -1.5, 4)
ri.Rotate(-20, 1, 0, 0)

# the groundplane
ri.AttributeBegin()
ri.Color([0.7, 0.7, 0.8])
ri.Surface("plastic")
face=[10, 0, 10, 10, 0, -10, -10, 0, 10, -10, 0, -10]
ri.Patch("bilinear",{'P':face})
ri.AttributeEnd()

ri.Rotate(45, 1, 0, 0)

#model the pin
# the pointy end
ri.TransformBegin()
end_height = 0.35
metal_radius = 0.06
ri.Translate(0, end_height, 0)
ri.TransformBegin()
ri.AttributeBegin()
ri.Color([1, 1, 1])
ri.Rotate(90, 1, 0, 0)
ri.Surface("metal")
ri.Cone(end_height, metal_radius, 360)
ri.AttributeEnd()
ri.TransformEnd()

#the metal thing
metal_height = 0.9
ri.TransformBegin()
ri.AttributeBegin()
ri.Color([1,1,1])
ri.Rotate(-90, 1, 0, 0)
ri.Surface("metal")
ri.Cylinder(metal_radius, 0, metal_height, 360)
ri.AttributeEnd()
ri.TransformEnd()

# base for bowly shaped thing
ri.TransformBegin()
ri.Translate(0, metal_height, 0)
ri.TransformBegin()
ri.AttributeBegin()
ri.Color([0.2,0.2,0.8])
ri.Rotate(-90, 1, 0, 0)
disk_radius = 0.45
ri.Surface("plastic")
ri.Disk(0, disk_radius, 360)
ri.AttributeEnd()
ri.TransformEnd()

# bowly thing
ri.TransformBegin()
ri.AttributeBegin()
ri.Color([0.2,0.2,0.8])
bowl_radius = 0.47
ri.Translate(0, -0.05, 0)
ri.Rotate(-90, 1, 0, 0)
y_max = 0.433
y_min = 0.05
ri.Surface("plastic")
ri.Sphere(bowl_radius, y_min, y_max, 360)
ri.AttributeEnd()
ri.TransformEnd()

# plastic body
ri.TransformBegin()
ri.Translate(0, y_max - y_min, 0)
ri.AttributeBegin()
ri.Color([0.2,0.2,0.8])
body_height = 0.7
body_br = 0.2
body_tr = 0.15
ri.Surface("plastic")
hyperboloid_wrapper(body_height, body_br, body_tr)
ri.AttributeEnd()

# top base (tb)
ri.TransformBegin()
ri.Translate(0, body_height, 0)
ri.AttributeBegin()
ri.Color([0.2,0.2,0.8])
tb_height = 0.08
tb_tr = 0.375
ri.Surface("plastic")
hyperboloid_wrapper(tb_height, body_tr, tb_tr)
ri.AttributeEnd()

# top top (tt)
ri.TransformBegin()
ri.AttributeBegin()
ri.Color([0.2,0.2,0.8])
ri.Translate(0, tb_height, 0)
tt_tr = 0.35
ri.Surface("plastic")
hyperboloid_wrapper(tb_height, tb_tr, tt_tr)
ri.AttributeEnd()

# top cup (tc)
ri.TransformBegin()
ri.AttributeBegin()
ri.Color([0.2,0.2,0.8])
ri.Translate(0, tb_height, 0)
ri.Rotate(-90, 1, 0, 0)
tc_radius = tt_tr
ri.Surface("plastic")
ri.Disk(0, tc_radius, 360)
ri.AttributeEnd()


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
