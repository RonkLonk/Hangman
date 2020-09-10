from random_word import RandomWords
randWord = RandomWords()

def printCurrentStatus():
    print("You have", guessesLeft, "guesses left.")
    print("You have guessed:", guessedLetters)
    for letter in revealedLetters:
        print(letter, end=" ")
    print()
    print()

def getInput():
    letter = input("Guess a letter: ")
    return letter

guessesLeft = 10
computerWord = randWord.get_random_word()
guessedLetters = []
lettersList = computerWord.split()
revealedLetters = []
for i in range(len(computerWord)):
    revealedLetters.append("_")

def checkLetter(guess):
    if guess in lettersList:
        for i in range(len(lettersList)):
            if guess == lettersList[i]:
                revealedLetters[i] = guess
    guessedLetters.append(guess)

while True:
    guess = getInput()
    checkLetter(guess)
    printCurrentStatus()

