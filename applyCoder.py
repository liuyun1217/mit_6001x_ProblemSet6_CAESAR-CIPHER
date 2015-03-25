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