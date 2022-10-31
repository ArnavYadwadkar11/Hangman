import random

print('HANGMAN')
name = input('What is your name? ')
print('Good Luck!', name, "enjoy the game!")
words = ['rainbow', 'computer', 'science', 'programming', 'python', 'mathematics', 'player', 'condition', 'reverse', 'water', 'board', 'garden', 'football', 'gaming', 'tennis', 'fire', 'ice', 'thor', 'birthday', 'captain', 'tolerate']
word = random.choice(words)
print(name, ', guess the missing characters of the word')

guesses = ''
turns = 10

while turns > 0:
    failed = 0

    for letter in word:
        if letter in guesses:
            print(letter)
        else:
            print('_')
            failed = failed + 1

    if failed == 0:
        print(f'Congratulations {name}, you win!!!')
        print('The word is ', word)
        break

    guess = input('Guess a letter: ')
    guesses = guesses + guess

    if guess not in word:
        turns = turns - 1
        print('Wrong!')
        print(f'You have {turns} turns remaining')

        if turns == 0:
            print('GAME OVER!! Better luck next time')
            print(f'The word was {word}')