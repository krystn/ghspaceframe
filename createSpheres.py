import Rhino as r
import rhinoscriptsyntax as rs
import ghpythonlib.components as com
import ghpythonlib.treehelpers as TH
import random

pts = TH.tree_to_list(pts, lambda x:x)

lstDots = []

def createDots(points, radius):
    rndm = random.uniform(0, 2)
    newRad = radius + rndm
    dots = rs.AddSphere(points, newRad)
    return dots


for i in xrange( len(pts) ):
    lstDots.append([])
    for j in xrange( len(pts[i]) ):
        dot = createDots(pts[i][j], rad)
        lstDots[i].append(dot)
        
    

dotsOut = TH.list_to_tree(lstDots, True, [])