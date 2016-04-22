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

#words that the computer is going to randomly choose from
words_list = 'apple four office trial clinic computer desktop message fun funny'.split()

#define a function to split the above string into words and choose one one randomly and return it
def splitGetRandomWord (word):
	wordNumber = random.randint(0, len(word)-1)
	return word[wordNumber]

#define a fuction to compare user's gueeses to the letters in the secretword
def displayHangmanBoard (HANGMANPICS, rightguess, wrongguess, secretword):
	print HANGMANPICS[len(wrongguess)]
	
	#displays the worng guesses user has made
	print 'Wrong Letters: '
	for letter in wrongguess:
		print letter, 

	blanks = '_' * len(secretword)

	#replaces the blanks with correct guesses
	for x in range (len(secretword)):
		if secretword[x] in rightguess:
			blanks = blanks[:x] + secretword[x] + blanks[x+1:]

	print '\n'
	#shows the secretword with spaces in between each letter
	for letter in blanks:
		print letter, 

#define a function for the user to enter her guesses and also checks the guess is one letter
def getUserGuess (guessed):
	while True:
		print '\n\nGuess a letter: '
		guess = raw_input().lower()
		if len(guess) != 1:
			print 'Please enter only one letter.'
		elif guess in guessed:
			print 'You have already guessed this letter.'
		elif guess not in 'abcdefghijklmnopqrstuvwxyz':
			print 'Enter only letters from A-Z.'
		else:
			return guess

#define a function to offer user the option to play again after winning or losing the game
def playAgain ():
	print 'Do you want to Play again? (yes or no)'
	#function return True only if the answer is yes
	return raw_input().lower().startswith('y') 	

print 'H A N G M A N'
rightguess = ''
wrongguess = ''
secretword = splitGetRandomWord(words_list)
gameIsDone = False

while True:
	displayHangmanBoard (HANGMANPICS, rightguess, wrongguess, secretword)

	#player types in a letter
	guess = getUserGuess(wrongguess + rightguess)

	if guess in secretword:
		rightguess = rightguess + guess

		#check whether the players has won
		foundItAll = True
		for i in range (len(secretword)):
			if secretword[i] not in rightguess:
				foundItAll = False
				break
		if foundItAll:
			print 'You won! The secret word is ' + secretword + '.'
			gameIsDone = True

	else:
		wrongguess = wrongguess + guess

		#check whether the player has run out of guesses
		if len(wrongguess) == len(HANGMANPICS) - 1:
			displayHangmanBoard (HANGMANPICS, rightguess, wrongguess, secretword)
			print 'You have run out of guesses.'
			gameIsDone = True

	if gameIsDone:
		if playAgain():
			wrongguess = ''
			rightguess = ''
			gameIsDone = False
			secretword = splitGetRandomWord(words_list)
		else:
			break






