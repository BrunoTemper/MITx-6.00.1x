#   MITx 6.00
#   Problem Set 3 - Hangman
#
#   

import string
import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print str(len(wordlist)), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

wordlist = loadWords()

def listToString(list):
    '''
    list: list of characters guessed or letters available
    returns: string
    '''
    outString = ""
    for char in range(len(list)):
        outString+=str(list[char])
    return outString
    
def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for l in range(len(secretWord)):
        if (secretWord[l] not in lettersGuessed):
            return False
    return True

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    guessedSoFar = []
    for l in range(len(secretWord)):
        if (secretWord[l] in lettersGuessed):
            guessedSoFar.append(secretWord[l]+" ")
        else:
            guessedSoFar.append("_ ")

    return listToString(guessedSoFar)

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    letters = string.ascii_lowercase
    availableLetters = []

    for l in letters:
        if l in lettersGuessed:
            pass
        else:
            availableLetters.append(l)

    return listToString(availableLetters)

def printLine():
    print "-" * 13

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''

    lettersGuessed = []
    mistakesMade = 0
    attempts = 8
    availableLetters = []
    
    print "Welcome to the game, Hangman!"
    print "I am thinking of a word that is " + str(len(secretWord)) + " letters long."
    printLine()
    
    while (isWordGuessed(secretWord, lettersGuessed) != True):
        print "You have " + str(attempts) + " guesses left."
        print "Available letters: " + getAvailableLetters(lettersGuessed)
        guess = raw_input('Please guess a letter: ')
        guess = guess.lower()
        availableLetters = getAvailableLetters(lettersGuessed)
        
        if (guess in secretWord) and (guess not in lettersGuessed):
            lettersGuessed.append(guess)
            print "Good guess: " + getGuessedWord(secretWord, lettersGuessed)
        elif (attempts <= 1):
            print "Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed)
            printLine()
            print "Sorry, you ran out of guesses. The word was " + secretWord + "."
            break
        elif (guess in lettersGuessed):
            print "Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed)
        else:
            lettersGuessed.append(guess)
            print "Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed)
            attempts -= 1
        printLine()
        if (isWordGuessed(secretWord, lettersGuessed) == True):
            print "Congratulations, you won!"
            break
