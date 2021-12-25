from pprint import pprint
from typing import DefaultDict

def getIntermediatePoints(points):
    x1, y1 = points[0]
    x2, y2 = points[1]

    if x1==x2:
        if y1 > y2:
            y1,y2 = y2, y1
        pointsList = [(x1,y) for y in range(y1,y2+1,1) ]
    elif y1==y1:
        if x1 > x2:
            x1,x2 = x2,x1
        pointsList = [(x,y1) for x in range(x1,x2+1,1)]
    return pointsList  

def bresenham(points): 
      # Setup initial conditions
    x1, y1 = points[0]
    x2, y2 = points[1] 
    dx = x2 - x1
    dy = y2 - y1
 
    # Determine how steep the line is
    is_steep = abs(dy) > abs(dx)
 
    # Rotate line
    if is_steep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2
 
    # Swap start and end points if necessary and store swap state
    swapped = False
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
        swapped = True
 
    # Recalculate differentials
    dx = x2 - x1
    dy = y2 - y1
 
    # Calculate error
    error = int(dx / 2.0)
    ystep = 1 if y1 < y2 else -1
 
    # Iterate over bounding box generating points between start and end
    y = y1
    points = []
    for x in range(x1, x2 + 1):
        coord = (y, x) if is_steep else (x, y)
        points.append(coord)
        error -= abs(dy)
        if error < 0:
            y += ystep
            error += dx
 
    # Reverse the list if the coordinates were swapped
    if swapped:
        points.reverse()
    return points

def partOne():
    with open("./day-5/data.txt",'r') as file:
        lines = file.readlines()

    #parse the data file into a list of tuples 
    coOrdinatesList = [ eval(elem) for ln in lines for elem in ln.strip().split(" -> ")]

    filteredList = []
    # keep only vertical and horizontal lines
    for i in range(0,len(coOrdinatesList)-1,2):
        x1,y1 = coOrdinatesList[i] 
        x2,y2 = coOrdinatesList[i+1]

        if x1==x2 or y1==y2:
            filteredList.append([coOrdinatesList[i],coOrdinatesList[i+1]])
            # filteredList.append(coOrdinatesList[i+1])


    # pprint(coOrdinatesList)    
    # pprint(filteredList)

    coverPoints = DefaultDict(list)

    # find the covering points 
    for i in range(len(filteredList)):
        coverPoints[i] = getIntermediatePoints(filteredList[i])

    # pprint(coverPoints)

    overlapPointsCount = DefaultDict(int)

    # find the overlapping points between the lines
    for pointList in coverPoints.values():
        for point in pointList:
            for anotherList in coverPoints.values():
                if anotherList != pointList:
                    if point in anotherList:
                        overlapPointsCount[point] += 1
    
    # pprint(overlapPointsCount)

    print("answer ::", len(overlapPointsCount))

def partTwo():
    with open("./day-5/data.txt",'r') as file:
        lines = file.readlines()

    #parse the data file into a list of tuples 
    coOrdinatesList = [ eval(elem) for ln in lines for elem in ln.strip().split(" -> ")]
    
    coOrdinatesList = [[coOrdinatesList[i],coOrdinatesList[i+1]] for i in range(0,len(coOrdinatesList)-1,2)]

    coverPoints = DefaultDict(list)

    # find the covering points 
    for i in range(len(coOrdinatesList)):
        coverPoints[i] = bresenham(coOrdinatesList[i])

    # pprint(coverPoints)

    overlapPointsCount = DefaultDict(int)

    # find the overlapping points between the lines
    for pointList in coverPoints.values():
        for point in pointList:
            for anotherList in coverPoints.values():
                if anotherList != pointList:
                    if point in anotherList:
                        overlapPointsCount[point] += 1
    
    # pprint(overlapPointsCount)

    print("answer ::", len(overlapPointsCount))


def main():
    partTwo()

if __name__ ==  "__main__":
    main()