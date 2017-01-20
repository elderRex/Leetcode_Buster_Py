def __init__(self, v1, v2):
    """
    Initialize your data structure here.
    :type v1: List[int]
    :type v2: List[int]
    """
    self.data = [v1, v2]
    self.len = len(v1) + len(v2)


def next(self):
    """
    :rtype: int
    """
    tmp = self.data[0]
    s = tmp.popleft()
    del self.data[0]
    if len(tmp) != 0:
        self.data.append(tmp)
    self.len -= 1
    return s


def hasNext(self):
    """
    :rtype: bool
    """
    return self.len > 0