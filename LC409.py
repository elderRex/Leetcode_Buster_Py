
def longestPalindrome(s):
    """
    :type s: str
    :rtype: int
    """
    mydict = {}
    for ch in s:
        if mydict.has_key(ch):
            mydict[ch] = mydict.get(ch) + 1
        else:
            mydict[ch] = 1
    has_one = False
    lencnt = 0
    print mydict
    for k,v in mydict.items():
        if v%2 == 1:
            has_one = True
            if v > 1:
                lencnt += v-1
        elif v%2 == 0:
            lencnt += v
    lencnt = lencnt + 1 if has_one else lencnt
    return lencnt

s = "civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"

print longestPalindrome(s)