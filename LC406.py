import collections

def reconstructQueue(people):
    """
    :type people: List[List[int]]
    :rtype: List[List[int]]
    """
    mydict = []
    fulldict = collections.defaultdict(list)
    for pp in people:
        fulldict[pp[0]].append(pp)

    for k,v in fulldict.items():
        mydict.append([k,v])
    mydict = sorted(mydict,key=lambda x:x[0],reverse=True)
    #print mydict
    ans = []

    for h,hl in mydict:
        hl = sorted(hl,key=lambda x:x[1])
        for pp in hl:
            ans.insert(pp[1],pp)
        print ans

    #print ans

    return ans

test = [[9,0],[7,0],[1,9],[3,0],[2,7],[5,3],[6,0],[3,4],[6,2],[5,2]]

reconstructQueue(test)