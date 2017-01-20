'''
Given a string, find the length of the longest substring T that contains at most k distinct characters.

For example, Given s = 'eceba' and k = 2,

T is "ece" which its length is 3.
'''

def lengthOfLongestSubstringKDistinct(self, s, k):
    """
    :type s: str
    :type k: int
    :rtype: int
    """
    mydict = {}
    L = 0
    len_max = 0
    for i in range(0,len(s)):
        if mydict.has_key(s[i]):
            mydict[s[i]] = mydict.get(s[i]) + 1
        else:
            mydict[s[i]] = 1

        if len(mydict) <= k:
            cur_len = i - L
            len_max = len_max if cur_len < len_max else cur_len
        elif len(mydict) > k:
            mydict[s[L]] = mydict.get(s[L]) - 1
            if mydict.get(s[L]) == 0:
                del mydict[s[L]]
            L += 1

    return len_max




