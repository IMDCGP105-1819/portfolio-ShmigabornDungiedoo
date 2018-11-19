# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
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



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    secret_word= list(secret_word)
    guess=[]
    for c in secret_word:
        if c in letters_guessed:
            guess.append(c)
    if len(guess)==len(secret_word):
        return 1
    else:
        return 0



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    secret_word= list(secret_word)
    print(letters_guessed)
    guess=[]
    for c in secret_word:
        if c in letters_guessed:
            guess.append(c)
        elif c not in letters_guessed:
            guess.append("_ ")
    guess="".join(guess)
    return guess



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    import string
    alphabet=string.ascii_lowercase
    alphabet=list(alphabet)
    for c in alphabet:
        if c in letters_guessed:
            alphabet.remove(c)
    return alphabet



def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    secret_word=list(secret_word)
    length=len(secret_word)
    consonants=["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s" ,"t", "v", "x", "z"]
    vowels=["a", "e", "i", "o", "u"]
    guesses_remaining=6
    warnings_remaining=3
    print("The word contains ", length, " letters.")
    letters_guessed=[]
    isguessed=0
    alphabet=string.ascii_lowercase
    alphabet=list(alphabet)
    alphaorig=string.ascii_lowercase
    alphaorig=list(alphaorig)
    twoguess=[]
    victory =0
    while isguessed==0:
        print("\n")
        print("-------")
        print("\n")
        
        if victory ==1:
            isguessed==1
            print("You win.")
            unique=len(list(set(secret_word)))
            score=guesses_remaining*unique
            print("Your score is ", score)
            break

        print("Warnings left: ", warnings_remaining)
        print("Guesses left: ", guesses_remaining)
        twoguess=[]
        oneguess=input("Please guess a letter: ")
        oneguess=oneguess.lower()
        twoguess.append(oneguess)
        letters_guessed.extend(twoguess)
        guess=get_guessed_word(secret_word, letters_guessed)
        alphabet=get_available_letters(letters_guessed)
        victory=is_word_guessed (secret_word, letters_guessed)
        print("My word: ", guess)



        if len(twoguess)>1:
            print(twoguess)
            print("Please input 1 letter at a time")
            warnings_remaining=warnings_remaining-1
            letters_guessed.pop()


        for c in twoguess:
            letters_guessed.pop()
            if c in letters_guessed:
                warnings_remaining= warnings_remaining-1
                letters_guessed.extend(twoguess)
            else:
                letters_guessed.extend(twoguess)

        for c in twoguess:
            if c not in secret_word:
                for k in twoguess:
                    if k in vowels:
                        guesses_remaining=guesses_remaining-2
                        print("Wrong, you lose 2 guesses")
                    elif k in consonants:
                        guesses_remaining=guesses_remaining-1
                        print("Wrong, you lose a guess")
        for c in twoguess:
            if c not in alphaorig:
                warnings_remaining=warnings_remaining-1
                print("Such input is not allowed, you lose 1 warning point")

        if warnings_remaining<=0:
            guesses_remaining=guesses_remaining-1
            print("You are out of warnings. You lose one guess")

        if guesses_remaining<=0:
            print("You are out of guesses. The word was ", secret_word, ".")
            isguessed=1



        print("Letters guessed ", letters_guessed)
        print("Letters left ", alphabet)
        print("\n")
        print("-------")
        print("\n")




secret_word = choose_word(wordlist)
hangman (secret_word)
