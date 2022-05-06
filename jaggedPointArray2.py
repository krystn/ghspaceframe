import Rhino as r
import ghpythonlib.components as com
import ghpythonlib.treehelpers as TH

pts = TH.tree_to_list(pts, lambda x:x)

lstText = []
newCrvs = []
upperPts = []
normals = []
centroids = []
plyCrvs = []

#FUNCTION TO FIND RAISED POINT
def findRaisedPt(refPts, refCentroid, newZ):
    
    newLstPts = []
    
    #find 2 vectors of a triangle
    vector, length = com.Vector2Pt(refPts[0], refPts[2], True)
    vector2, length2 = com.Vector2Pt(refPts[0], refPts[1], True)
    
    #find normal from 2 vectors
    normal = r.Geometry.Vector3d.CrossProduct(vector, vector2)
    
    #unitize vectors, check if True
    success = normal.Unitize()
    
    normal *= newZ #increase Z direction
    raisedPnt = refCentroid + normal #add the new Z to the centroid coordinates
    
    return raisedPnt

#FUNCTION TO DRAW LINES FROM EACH POINT OF THE TRIANGLE TO THE RAISED POINT
def findNewCrv(refPts, refRaisedPt):
    newLstCrv = []
    for i in xrange( len(refPts) ):
        
        newCrv = com.Line(refPts[i], refRaisedPt)
        newLstCrv.append(newCrv)
        
    return newLstCrv
"""
FUNCTION TO LABEL THE UPPER PTS
def createTextLabel(a, b):
    list = []
    text = '[{0}][{1}]'.format(a, b)
    lstText[i].append(text)
    
    return list
"""

#FOR LOOP FOR CREATING THE SPACE FRAME
for i in xrange( len(pts) -1):
    upperPts.append([])
    
    for j in xrange( len(pts[i]) ):
        
        listPts = [ pts[i][j], pts[i+1][j+1], pts[i+1][j] ]
        #print listPts[0]
        
        lstCrvs = []
        
        
        plyCrv = com.PolyLine(listPts, True)
        lstCrvs.append(plyCrv)
        plyCrvs.append(lstCrvs)
        
        #find centroid
        area, centroid = com.Area(plyCrv)
        centroids.append(centroid)
        
        #use function to find raised point
        raisedPt = findRaisedPt(listPts, centroid, newZ)
        
        upperPts[i].append(raisedPt)
        
        #use function to find new triangle curves
        newCrv = findNewCrv(listPts, raisedPt)
        newCrvs.append(newCrv)
        """
        #use function to label text
        txt = createTextLabel(i, j)
        lstText.append(txt)
        """

#upper layer of spaceframe using the raisedPts

upperPlyCrvs = []

#FOR LOOP FOR DRAWING THE POLYLINES FOR THE UPPER PART OF THE SPACE FRAME
#create similar for loop but for the raised points (upperPts) we found 
for i in xrange( len(upperPts) -1):
    #upperPlyCrvs is an empty list, this line adds an empty list 
    #for every item in the outer list
    upperPlyCrvs.append([]) 
    
    for j in xrange( len(upperPts[i]) ):
        #copy the pattern from the first for loop and make sure to be taking 
        #the index of upperPts not pts
        lstUpperPts = [ upperPts[i][j], upperPts[i+1][j+1], upperPts[i+1][j] ]
        
        #create polylines using the (3) points of the triangle
        upperPlyCrv = com.PolyLine(lstUpperPts, True)
        upperPlyCrvs[i].append(upperPlyCrv)

upperPlyCrvsOut = upperPlyCrvs

upperPlyCrvsOut = TH.list_to_tree(upperPlyCrvs, True, [])

#plyOut = plyCrvs
#ctrOut = centroids
#normOut = normals#
#normPtsOut = normPts
#newCrvOut = newCrvs
#textOut = lstText

plyOut = TH.list_to_tree(plyCrvs, True, [])
newCrvOut = TH.list_to_tree(newCrvs, True, [])
upperPtsOut = TH.list_to_tree(upperPts, True, [])
textOut = TH.list_to_tree(lstText, True, [])

"""
CREATING THE POLYLINES FOR THE INTERMEDIATE TRIANGLES, NOT
USED IN THIS EXERCISE
plyCrvs2 = []
for i in xrange( len(pts) -1):
    for j in xrange( len(pts[i]) -1):
        
        listPts2 = pts[i][j], pts[i][j+1], pts[i+1][j+1]
        plyCrv2 = com.PolyLine(listPts2, True)
        plyCrvs2.append(plyCrv2)
        
plyOut2 = plyCrvs2
"""

###FINDING THE PATTERN FOR THE TRIANGLES
#listPtsA = [ pts[0][0], pts[1][1], pts[1][0] ]
#listPtsA2 = [ pts[1][0], pts[2][1], pts[2][0] ]
#listPtsA3 = [ pts[2][0], pts[3][1], pts[3][0] ]

#listPtsB = [ pts[1][0], pts[1][1], pts[2][1] ]
#listPtsB2 = [ pts[2][0], pts[2][1], pts[3][1] ]
#listPtsB3 = [ pts[3][0], pts[3][1], pts[4][1] ]

#plyCrv = com.PolyLine(listPts, True)
#plyCrv2 = com.PolyLine(listPts2, True)
#plyCrv3 = com.PolyLine(listPts3, True)

#print plyCrv

#find the centroid



"""
FINDING THE VECTORS, NORMAL AND NEW RAISED CENTROID
def TriangleCenter(input1, input2):
    
    area, centroid = com.Area(polyline)
    centroid = pt0 + pt1 + pt2)/3
    
    r.Geometry.
    r.Geometry.Vector3d(X, Y, Z)
    r.Geometry.Vector3d.Unitize()
    r.Geometry.Vector3d.CrossProduct(
    
    centroid = r.Geometry.Point3d(
    
    
    return result,
    
"""





