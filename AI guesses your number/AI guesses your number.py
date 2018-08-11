#Computer Guesses your Number

print('Let me try and guess your number')
maxNumber = int(input('Please set the range from 1 and : '))

minNumber = 1

input('Think of a number between %s and %s then press ENTER' % (minNumber, maxNumber))

while True:

   
    guess = (minNumber + maxNumber) // 2

  
    correctGuess = input('Is %s your number? (yes/higher/lower): ' % guess)
    
    if correctGuess == 'yes':
        print('I guessed the right number!')
        break
    elif minNumber == maxNumber:
        print('You are trying to trick me')
        break
    elif correctGuess == 'higher':
        minNumber = guess + 1
    elif correctGuess == 'lower':
        maxNumber = guess - 1
    else:
        print('We do not recoginze what you entered. Try again!')
    


