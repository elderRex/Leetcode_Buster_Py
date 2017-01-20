import collections
def wordSquares(self, words):
    """
    :type words: List[str]
    :rtype: List[List[str]]
    """
    '''
    for each word
        add to square
        for each ch
            get matching result
    '''
    lenw = len(words[0])
    full_dict = collections.defaultdict(list)
    '''
    build dict with a: area ar:area are:area
    '''
    for word in words:
        for i in range(0,lenw):
            full_dict[word[:i]].append(word)

    '''
    build with one word
    '''
    squares = []
    def build(square):
        if len(square) == lenw:
            return squares.append(square)
        prefix = []
        for i in range(0,len(square)):
            prefix.append(square[i][len(square)])
        for word in full_dict[prefix]:
            build(square+[word])

    for word in words:
        build([word])

    return squares

