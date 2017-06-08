import random

HANGMANPICS = ['''

  +---+
  |   |
      |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()

def getRandomWord():
    index = random.randint(0, len( words ))
    word = words[ index ]
    return word

def guessLetter():
    while( True ):
        print('Guess a letter: ' )
        guess = input()
        guess = guess.lower()
        # Only single characters allowed
        if ( len( guess ) > 1 ):
            print( 'Enter a single letter' )
        # No numbers allowed
        elif( guess in '1234567890' ):
            print( 'Enter a letter not number' )
        # Not already a wrong guesses
        elif( guess in wrongGuesses ):
            print( 'Letter is wrong but already guessed' )
        # Not already in correct guesses
        elif( guess in correctGuesses ):
            print( 'Letter is correct but already guessed' )
        elif( guess in 'abcdefghijklmnopqrstuvwxyz' ):
            break
        else:
            print( 'No idea what that character was but enter only a letter' )
    return guess

def displayBoard():
    print( HANGMANPICS[0] )

    print( 'Missed Letters', end=' ')

    for letter in secretWord:
        if ( letter in correctGuesses ):
            print( letter, end=' ' )
        else:
            print( '_', end=' ' )
    print()
    print( 'Incorrect letters: ' + wrongGuesses )

# Generate random word
secretWord = getRandomWord()
wrongGuesses = ''
correctGuesses = ''
print ( secretWord )

def takeGuess():
    print('takeGuess')

def takeGuess( aGuess ):
    print('takeGuess' + aGuess)
    
# Loop until the user has guessed word or run out of lives
while( True ):
    
    # Display current state
    displayBoard()

    # Get user guess
    guess = guessLetter()
    print( guess )

    # Check guess is in word
    if ( guess in secretWord ):
        # Already guessed
        if ( guess in correctGuesses ):
            print('Letter already correctly guessed')
        else:
            print('Letter is in the word')
            correctGuesses = correctGuesses + guess
    else:
        # Already guessed?
        if ( guess in wrongGuesses ):
            print('Letter already incorrectly guessed')
        else:
            print('Letter is not in the word')
            wrongGuesses = wrongGuesses + guess

    if ( len( wrongGuesses ) >= 7 ):
        print( 'Too many guesses. Word was ' + secretWord )
        break
