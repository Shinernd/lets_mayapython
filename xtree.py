import pymel.core as pm
import random

myPyramids = []

#make pyramids
for n in range (2872):
    myPyramids.append(pm.polyPyramid())
      
count = 0
for x in range (20):
    yran = 20 - x
    for y in range (yran):
        zran = 20 - y
        for z in range (zran):
            pm.select(myPyramids[count])
            pm.move(0.05*x*x, y, 0.05*z*z) #curve
            pm.scale(0.5, 0.5, 0.5)
            rg = int(random.random()*10)%2 #red or green?
            if (rg): #green
                pm.polyColorPerVertex(colorRGB=[0, 1-random.random(), 0], colorDisplayOption=True)
            else: #red
                pm.polyColorPerVertex(colorRGB=[1-random.random(), 0, 0], colorDisplayOption=True)
            pm.rotate(x*10.0, y*10.0, z*10.0)
            pm.polyMirrorFace(direction=0, mergeMode=1)
            pm.polyMirrorFace(direction=4, mergeMode=1)
            count = count + 1

#star 1
pm.select(myPyramids[count])
pm.move(0, 20.1, 0.2)
pm.scale(1, 1, 1)
pm.rotate(0, 90, 0)
pm.polyColorPerVertex(colorRGB=[1,1,0], colorDisplayOption=True)
count = count + 1

#star 2
pm.select(myPyramids[count])
pm.move(0, 20.1, -0.2)
pm.scale(1, 1, 1)
pm.rotate(45, 270, 0)
pm.polyColorPerVertex(colorRGB=[1,1,0], colorDisplayOption=True)
