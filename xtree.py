import pymel.core as pm
import random

myPyramids = []

#make pyramids
for n in range (386):
    myPyramids.append(pm.polyPyramid())
            
count = 0
for x in range (10):
    yran = 10 - x
    for y in range (yran):
        zran = 10 - y
        for z in range (zran):
            pm.select(myPyramids[count])
            pm.move(0.1*x*x, y, 0.1*z*z) #curve
            pm.scale(1, 1, 1)
            rg = int(random.random()*10)%2 #red or green?
            if (rg): #green
                pm.polyColorPerVertex(colorRGB=[0, 1-random.random(), 0], colorDisplayOption=True)
            else: #red
                pm.polyColorPerVertex(colorRGB=[1-random.random(), 0, 0], colorDisplayOption=True)
            pm.rotate(x*10.0, y*10.0, z*10.0)
            pm.polyMirrorFace(direction=0, mergeMode=1)
            count = count + 1

#a star
pm.select(myPyramids[count])
pm.move(0, 10.1, 0)
pm.scale(1,1,1)
pm.rotate(0, 90, 0)
pm.polyColorPerVertex(colorRGB=[1,1,0], colorDisplayOption=True)
