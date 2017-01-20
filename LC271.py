def encode(self, strs):
    """Encodes a list of strings to a single string.

    :type strs: List[str]
    :rtype: str
    """
    res = ''
    for ch in strs:
        x = chr(ord(ch) + 1) % 255
        res += x

    return res



def decode(self, s):
    """Decodes a single string to a list of strings.

    :type s: str
    :rtype: List[str]
    """
    ans = ''
    for ch in s:
        if ord(ch) == 0:
            x = chr(255)
        elif ord(ch) == 255:
            x = chr(0)
        else:
            x = chr(ord(ch)-1)
        ans += x

    return ans