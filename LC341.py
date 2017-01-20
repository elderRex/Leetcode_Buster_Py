class NestedIterator(object):
    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.flattened = [self.flat(ni) for ni in nestedList]
        self.cnt = 0

    def flat(self, ni):
        ans = []
        if ni.isInteger():
            ans.append(ni.getInteger())
        else:
            for item in ni.getList():
                ans += self.flat(item)

        return ans

    def next(self):
        """
        :rtype: int
        """
        a = self.flattened[self.cnt]
        self.cnt += 1
        return a

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.cnt < len(self.flattened)
