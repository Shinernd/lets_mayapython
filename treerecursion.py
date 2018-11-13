#by professor Park in maya python study

import maya.cmds as mc;
import random;

def tree (rootX,rootY,rootZ,rotX,rotY,rotZ,sizeOfBranch):
    if sizeOfBranch<0.4: 
        return;
    if random.random()<0.2: #cut some branches randomly
        return;
        
    myCube = mc.polyCube();
    mc.move(0, -0.5 * sizeOfBranch, 0, myCube[0] + '.scalePivot', myCube[0] + '.rotatePivot',localSpace=True); #move pivot
    mc.move(rootX+0, rootY+0.5*sizeOfBranch, rootZ+0); #move to pivot
    mc.scale(0.3* sizeOfBranch,3 * sizeOfBranch,0.3 *sizeOfBranch); #change scale
    mc.rotate(rotX,rotY,rotZ,relative=True);
    print("Reccursiving.....")
    newSizeOfBranch=sizeOfBranch*0.85;
    
    #find center point
    newLocationTemp1 = mc.xform(myCube[0] + '.vtx[3]', q=True, ws=True, t=True); 
    newLocationTemp2 = mc.xform(myCube[0] + '.vtx[4]', q=True, ws=True, t=True);
    childRootX = (newLocationTemp1[0]+newLocationTemp2[0])/2.0;
    childRootY = newLocationTemp1[1];
    childRootZ = (newLocationTemp1[2]+newLocationTemp2[2])/2.0;

    #recursive
    tree(childRootX,childRootY,childRootZ,
    rotX+random.random()*40-40,
    rotY+random.random()*40-20,
    rotZ+random.random()*40-20,
    newSizeOfBranch);
    tree(childRootX,childRootY,childRootZ,
    rotX+random.random()*40-0,
    rotY+random.random()*40-20,
    rotZ+random.random()*40-20,
    newSizeOfBranch);
    tree(childRootX,childRootY,childRootZ,
    rotX+random.random()*40-20,
    rotY+random.random()*40-20,
    rotZ+random.random()*40-40,
    newSizeOfBranch);
    tree(childRootX,childRootY,childRootZ,
    rotX+random.random()*40-20,
    rotY+random.random()*40-20,
    rotZ+random.random()*40-0,
    newSizeOfBranch);

tree(0.0,0.0,0.0,0.0,0.0,0.0,1.0);
