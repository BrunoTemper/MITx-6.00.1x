def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.

    text: string
    returns: 0 <= int < 26


    PSEUDO CODE:
    Create a dictionary called scores
    In a loop from 0 to 26:
        Use applyShift to decrypted the encrypted text using the loop index
        Split the encrypted text into a list
        For reach word in the list:
            If isWord() is true, increment score by one
        Add score to the score dictionary with key of index
    After going through the loop, return the dictionary key with the highest score value
    """
    scores = {}
    
    for i in range(26):
        score = 0
        decrypted = applyShift(text, i)
        decrypted.split(' ')
        for w in decrypted:
            if (isWord(wordList, w)):
                score += 1
        scores[i] = score

    return max(scores, key=scores.get)

def decryptStory():
    """
    Using the methods you created in this problem set,
    decrypt the story given by the function getStoryString().
    Once you decrypt the message, be sure to include as a comment
    your decryption of the story.

    returns: string - story in plain text
    """
    ### TODO
