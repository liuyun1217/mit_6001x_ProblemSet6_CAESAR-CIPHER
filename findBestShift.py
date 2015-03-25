def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.

    text: string
    returns: 0 <= int < 26
    """
    ### TODO
    ##a = 0
    bestShift = [0]
    for n in range(0,26):   
        ##print n
        changeWord = applyShift(text, n)   
        wordSplit = changeWord.split(' ')
        ##print len(wordSplit)
        ##wordSplit = changeWord.split("'s")
        ##print len(wordSplit)
        for i in wordSplit:
            ##print i
            if  isWord(wordList, i):
                bestShift.append(n)##record all shift which can decode
            else:
                break
    
    
    return max(bestShift)
    
 
        
        
        
        
        
        



def isWord(wordList, word):
    """
    Determines if word is a valid word.

    wordList: list of words in the dictionary.
    word: a possible word.
    returns True if word is in wordList.

    Example:
    >>> isWord(wordList, 'bat') returns
    True
    >>> isWord(wordList, 'asdf') returns
    False
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\\:;'<>?,./\"")
    return word in wordList
    
    
    
    




def applyShift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. Lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.

    text: string to apply the shift to
    shift: amount to shift the text (0 <= int < 26)
    returns: text after being shifted by specified amount.
    """
    ### TODO.
    ### HINT: This is a wrapper function.
    return applyCoder(text, buildCoder(shift))
    
    
    
    
def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    ### TODO
    import string
    igoreList = string.punctuation+string.digits+" "
    
    newStrList = []
    for i in text:
        if i in igoreList:
            newStrList.append(i)
        else:
            newStrList.append(coder[i])
            
    newStr = ''
    newStr = ''.join(newStrList)           
    return newStr
    

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