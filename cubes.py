import pymel.core as pm

myCubes = []

for n in range (1000):
    myCubes.append(pm.polyCube())

count = 0
for x in range (10):
    for y in range (10):
        for z in range (10):
            pm.select(myCubes[count])
            pm.move(x, y, z)
            pm.scale(x/10.0, y/10.0, z/10.0)
            pm.rotate(x*10.0, y*10.0, z*10.0)
            pm.polyColorPerVertex(colorRGB=[1-x/10.0, 1-y/10.0, 1-z/10.0], colorDisplayOption=True)
            count = count +1
