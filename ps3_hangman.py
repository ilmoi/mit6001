# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...

    for c in secretWord:
        if c not in lettersGuessed:
            return False
    else:
        return True

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    s = ''
    for c in secretWord:
        if c in lettersGuessed:
            s+=c
        else:
            s+='_ '
    
    return s

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    s = ''
    for c in alphabet:
        if c not in lettersGuessed:
            s+=c
            
    return s

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
    # FILL IN YOUR CODE HERE...
    
    lettersGuessed = ''
    mistakesMade = 0
            
    while isWordGuessed(secretWord, lettersGuessed) == False and mistakesMade < 8:
        g = input('pls type a letter: ').lower()
        while g not in getAvailableLetters(lettersGuessed):
            print('again, stupid bitch')
            g = input('pls type a letter: ').lower()
        old = getGuessedWord(secretWord, lettersGuessed)
        lettersGuessed +=g
        new = getGuessedWord(secretWord, lettersGuessed)
        if new != old:
            print('good work: ' + str(new))
            print('tries left:' +str(8-mistakesMade))
        else:
            print('fucking loser')
            mistakesMade +=1
            print('tries left:' +str(8-mistakesMade))    
    
    if mistakesMade == 9:
        print('you lost')
    else:
        print('you won')


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
print(secretWord)
hangman(secretWord)


# my first original attempt
#    # FILL IN YOUR CODE HERE...
#
#    #show the length
#    print('There are: ' + str(len(secretWord)) + ' letters')
#    
#    # prep alphabet dictionary
#    alphabet = 'abcdefghijklmnopqrstuvwxyz'
#    alphabet_d = {}
#    for c in alphabet: alphabet_d[c] = False
#
#    secretList = [i for i in secretWord] #turning into list coz easier to iterate over
#    displayList = ['_' for i in secretWord]
#
#    guesses = 8
#    while '_' in displayList and guesses > 0:
#        start_count = displayList.count('_')
#        
#        # get user input            
#        print('your choices of letters are: ' + str([i for i in alphabet_d if alphabet_d[i] == False]))
#        g = input('enter a letter: ')
#        while alphabet_d[g] == True:
#            print('you already tried that one stupid bitch')
#            g = input('enter a letter: ')
#    
#        # test user input   
#        for i,c in enumerate(secretList):
#            if g == c:
#                displayList[i] = g
#        
#        end_count = displayList.count('_')
#        if end_count == start_count:
#            guesses -=1
#
#        # mark the letter as done in alphabet  
#        alphabet_d[g] = True
#
#        print(displayList)
#        print('guesses left: ' +str(guesses))
#        
#    if '_' in displayList:
#        print('you failed stupid bitch')
#    else:
#        print('victory! '+ str(displayList))
