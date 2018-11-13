#by gtchoi of maya python study

import maya.cmds as cmds
import random as random

def mdg(rootname, num,scalesize):
    nowname = rootname + 'Dot'
    cmds.duplicate(rootname,name=nowname)
    cmds.scale(scalesize* 1.2,scalesize * 1.2,scalesize *1.2)
    cmds.move(scalesize/(-2),scalesize/(-2),scalesize/(-2))
    cmds.rotate(random.random()* 360,random.random() * 360,random.random()*360)
    if(num>0):
        mdg(nowname,num-1,scalesize*2)

cmds.polyCube(name='rootcube',sx = 10, sy = 10, sz = 10)

for i in range(599,0,-1):
    if i%100<90 and i%100>10 and i%10<9 and i%10>0 : # 모서리만 남기고 face 지움
        cmds.select('rootcube.f['+str(i)+']') 
        cmds.delete()

cmds.select('rootcube')
originScale = 0.2
cmds.scale(originScale,originScale,originScale)

mdg('rootcube',8,originScale)
