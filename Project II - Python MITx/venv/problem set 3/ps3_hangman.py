# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

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
    for l in lettersGuessed:
        if l in secretWord:
            secretWord = secretWord.replace(l,"")
    if secretWord == "":
        return True
    else:
        return False


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    w = secretWord
    for l in secretWord:
        if l not in lettersGuessed:
            w = w.replace(l , "_ ")
    return w

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    available = string.ascii_lowercase
    for l in lettersGuessed:
        available = available.replace(l, "")
    return available
    

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
    print('Welcome to the game Hangman! \n'
          "I am thinking of a word that is " + str(len(secretWord)) +" letters long")
    guesses = []
    availableLetters = getAvailableLetters(guesses)
    mistakes = 0
    print("-----------")
    guess = input("You have "+str(8-mistakes) +" guesses left \n"
                  "Available Letters: "+str(availableLetters)+" \n"
                    "Please guess a letter: ")
    while not isWordGuessed(secretWord, guesses) and mistakes < 7:
        if not guess in availableLetters:
            print("Oops! You've already guessed that letter: "+ getGuessedWord(secretWord, guesses))
        else:
            guesses.append(guess)
            if not guess in secretWord:
                print("Oops! That letter is not in my word: "+ getGuessedWord(secretWord, guesses))
                mistakes += 1
            else:
                print("Good guess: " + getGuessedWord(secretWord, guesses))
        print("-----------")
        if isWordGuessed(secretWord, guesses):
            break
        availableLetters = getAvailableLetters(guesses)
        guess = input("You have " + str(8 - mistakes) + " guesses left \n"
                                                         "Available Letters: " + str(availableLetters) + "\n"
                                   "Please guess a letter: ")
    guesses.append(guess)
    if  guess not in secretWord:
        print("Oops! That letter is not in my word: " + getGuessedWord(secretWord, guesses) + "\n"
            "----------- \n"
                  "Sorry, you ran out of guesses. The word was " + secretWord)
    if isWordGuessed(secretWord, guesses):
        print("Congratulations, you won!")




# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = 'zzz'
hangman(secretWord)
def bob(s):
    n = 0
    while s.find('bob') != -1:
        n += 1
        if s[s.index('bob'):s.index('bob')+5] == 'bobob':
            n += 1
            s = s.replace('bo', "", 1)
        else:
            s = s.replace('bob', "", 1)
        print("Number of times bob occurs is: " + str(n))
    