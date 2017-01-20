def longestConsecutive(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    dis = dfs(self,root,0,root.val)

    return dis


def dfs(self, root, lenth, val):
    '''
    if root.val is larger than val, then we expande lenth
    other wise, the branch ends, and sets lenth to 1
    '''
    lenth = (lenth + 1) if root.val - val == 1 else 1
    L = dfs(self,root.left, lenth, root.val)
    R = dfs(self,root.right, lenth, root.val)
    return max(max(L, R), lenth)