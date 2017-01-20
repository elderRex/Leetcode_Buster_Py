def wordsTyping(self, sentence, rows, cols):
    """
    :type sentence: List[str]
    :type rows: int
    :type cols: int
    :rtype: int
    """
    '''

    append all words together
    eg.
    I had apple pie
    -----
         |
          -----
               |
                ----
    -
     |
      -----
           |==>>invalid


    row 4 col 5

    '''
    s = ' '.join(sentence) + ' '
    start, l = 0, len(s)
    for i in xrange(rows):
        start += cols

        '''
        add free space cols
        '''

        while s[start % l] != ' ':  # if current position in word does not point to space, move back the ptr
            start -= 1

        start += 1  # add the space behind

    return start / l