def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers, and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    ### TODO 
    import string
    lowerWords = string.ascii_lowercase
    upperWords = string.ascii_uppercase  
    chiList = []
    chiLower = buildOne(lowerWords,shift)
    chiUpper = buildOne(upperWords,shift)
    chiList = chiUpper + chiLower   
    wordStr = upperWords + lowerWords
    chiDic = {}
    
    for i in wordStr:
        chiDic[i] = chiList[wordStr.index(i)]
    
    return chiDic

    

    
def buildOne(wordsList,shift):
    chiWords = []
    changeWord = ''

    
    for i in wordsList:

        if wordsList.index(i)+shift < len(wordsList):
            changeWord = wordsList[wordsList.index(i)+shift]
        else:
            newIndex = wordsList.index(i)+shift-len(wordsList)
            changeWord = wordsList[newIndex]

        chiWords.append(changeWord)
    return chiWords