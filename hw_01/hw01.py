import random
import os
HANGMANPICS = ['''

  +---+
  |   |
  |
  |
  |
  |
=========''','''

  +---+
  |   |
  |   O
  |    
  |    
  |    
=========''','''

  +---+
  |   |
  |   O
  |   |
  |
  |
=========''','''

  +---+
  |   |
  |   O   
  |  /|   
  |    
  |    
=========''','''

  +---+
  |   |
  |   O   
  |  /|\  
  |    
  |    
=========''','''

  +---+
  |   |
  |   O   
  |  /|\  
  |  /    
  |    
=========''','''

  +---+
  |   |
  |   O   
  |  /|\  
  |  / \  
  |    
=========''']

def get_category():
    category = input("Выберите одну из трех категорий: 'Штаты США', 'Животные Австралии' или 'Школьные предметы': ")
    category = category.lower()
    category = category+'.txt'
    return category

def random_word(filename):
    with open(filename, encoding='utf-8') as f:
        words = []
        lines = f.readlines()
        for line in lines:
            if line.endswith('\n'):
                line = line[:-1]
            words += [line]
        return random.choice(words)

def displayBoard(HANGMANPICS, triesleft, missedletters, correctLetters,secretWord):
    print(HANGMANPICS[len(missedLetters)])
    print()

    triesleft = 6-len(missedletters)
    if triesleft > 4:
        triesleft = str(triesleft)
        print('Осталось '+triesleft+' попыток')
    elif triesleft == 1:
        triesleft = str(triesleft)
        print('Осталась '+triesleft+' попытка')
    else:
        triesleft = str(triesleft)
        print('Осталось '+triesleft+' попытки')
    
    print()

    print('Неправильные буквы: ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_'*len(secretWord)

    for i in  range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks:
        print(letter, end=' ')
    print()

def getGuess(alreadyGuessed):
    while True:
        guess = input('Введите букву: ')
        guess = guess.lower()
        if len(guess) != 1:
            print('Ваша буква:')
        elif guess in alreadyGuessed:
            print ('Вы уже пробовали эту букву. Выберите другую')
        elif guess not in 'ёйцукенгшщзхъфывапролджэячсмитьбю':
            print('Пожалуйста, введите букву кириллицы')
        else:
            return guess

def playAgain():
    print('Хотите попробовать еще раз? ("Да" или "Нет")')
    return input().lower().startswith('д')


print('В И С Е Л И Ц А')
category = input("Выберите одну из трех категорий: 'Штаты США', 'Животные Австралии' или 'Школьные предметы': ")
category = category.lower()
category = category+'.txt'
if os.path.isfile(category):
    triesleft = 6
    missedLetters = ''
    correctLetters = ''
    secretWord = random_word(category)
    gameIsDone = False
else:
    print('Такой категории нет! Выберите одну из существующих.')

while True:
    displayBoard(HANGMANPICS, triesleft, missedLetters, correctLetters, secretWord)
	
    guess = getGuess(missedLetters+correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Было загадано слово "'+secretWord+'"!')

            gameIsDone = True
    else:
        missedLetters = missedLetters+guess

        if len(missedLetters) == len(HANGMANPICS) - 1:
            displayBoard(HANGMANPICS, triesleft, missedLetters, correctLetters, secretWord)
            print('У вас не осталось попыток!\nЗагаданное слово: '+secretWord+'"')
            gameIsDone = True

    if gameIsDone:
        if playAgain():
            category = input("Выберите одну из трех категорий: 'Штаты США', 'Животные Австралии' или 'Школьные предметы': ")
            category = category.lower()
            category = category+'.txt'
            if os.path.isfile(category):
                missedLetters = ''
                correctLetters = ''
                secretWord = random_word(category)
                gameIsDone = False
            else:
                print('Такой категории нет! Выберите одну из существующих.')
        else:
            break
