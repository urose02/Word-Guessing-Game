import random

animals = ['elephant', 'bear', 'cheetah', 'giraffe', 'wolf', 'tiger', 'penguin', 'rabbit',
           'lion', 'monkey', 'rhinoceros', 'sheep', 'zebra']
fruits = ['apple', 'orange', 'guava', 'lime', 'watermelon']
stationery = ['pencil', 'eraser', 'sharpner', 'envelope', 'paper']
words = animals + fruits + stationery

random_word = random.choice(words)
print('WORD GUESSING GAME')

if random_word in animals:
    print('Hint: It\'s an animal')
elif random_word in fruits:
    print('Hint: It\'s a fruit')
else:
    print('Hint: It\'s a stationery item')

user_guesses = ''
chances = 5

while chances > 0:
    wrong_guess = 0
    for ch in random_word:
        if ch in user_guesses:
            print(ch, end=' ')
        else:
            wrong_guess += 1
            print('_', end=' ')

    if wrong_guess == 0:
        print('\nCONGRATULATIONS! YOU WON THE GAME. THE WORD IS ', random_word)
        break

    guess = input('\nMake a guess: ')
    user_guesses += guess

    if guess not in random_word:
        chances -= 1
        print(f'WRONG, YOU HAVE {chances} more chances')

        if chances == 0:
            print('GAME OVER. YOU LOSE. THE WORD IS ', random_word)
