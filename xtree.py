import maya.cmds as cmds
import random

pyramid_list = []

#make pyramids
for n in range (2872):
    pyramid_list.append(cmds.polyPyramid())
    
#make a tree
count = 0
for x in range (20):
    yran = 20 - x
    for y in range (yran):
        zran = 20 - y
        for z in range (zran):
            cmds.select(pyramid_list[count])
            cmds.move(x, y, z)
            cmds.move(0.05*x*x, y, 0.05*z*z) #curve
            
            #animation - breath
            for k in range (20):
                if not k % 2:
                    cmds.setKeyframe(v=y, at='translateY', t=k*20)
                else:
                    cmds.setKeyframe(v=0.05*y*y, at='translateY', t=k*20)
                    
            cmds.scale(0.5, 0.5, 0.5)
            rg = int(random.random()*10)%2 #red or green?
            if rg: #green
                cmds.polyColorPerVertex(colorRGB=[0, 1-random.random(), 0], colorDisplayOption=True)
            else: #red
                cmds.polyColorPerVertex(colorRGB=[1-random.random(), 0, 0], colorDisplayOption=True)
            cmds.polyMirrorFace(direction=0, mergeMode=1)
            cmds.polyMirrorFace(direction=4, mergeMode=1)
            #cmds.rotate(x*10.0, y*10.0, z*10.0)
            count = count + 1

#star 1
cmds.select(pyramid_list[count])
cmds.move(0, 20.1, 0.2)
cmds.scale(1, 1, 1)
cmds.rotate(90, 0, 0)
for i in range (80):
    cmds.setKeyframe(v=i*45, at='rotateZ', t=i*5)
cmds.polyColorPerVertex(colorRGB=[1,1,0], colorDisplayOption=True)
count = count + 1

#star 2
cmds.select(pyramid_list[count])
cmds.move(0, 20.1, -0.2)
cmds.scale(1, 1, 1)
cmds.rotate(270, 0, 45)
for j in range (80):
    cmds.setKeyframe(v=(j+1)*45, at='rotateZ', t=j*5)
cmds.polyColorPerVertex(colorRGB=[1,1,0], colorDisplayOption=True)
