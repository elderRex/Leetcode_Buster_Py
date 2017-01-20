def numberOfBoomerangs(self, points):
    """
    :type points: List[List[int]]
    :rtype: int
    """
    tot = 0
    for pt in points:
        mydict = {}
        for qt in points:
            x = pt[0] - qt[0]
            y = pt[1] - qt[1]
            mydict[x*x+y*y] = 1 + mydict.get(x*x+y*y,0)
        for key in mydict:
            tot += mydict[key] * (mydict[key]-1)

    return tot