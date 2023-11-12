import random
word_list = ['banana', 'apple', 'avocado', 'watermelon','grapes']
print(word_list)
word = random.choice(word_list)
print(word)
guess = input('Enter a single letter: ')

'''
Usually, when taking input from users, it is best to validate that the input makes sense.
For example, we may want to ensure that only a single letter is entered and that only alphabetical characters are 
provided by the user.
To do this, create conditional checks that must be passed before the input can be accepted.
Step 1:
Create an if statement that checks if the length of the input is equal to 1 and the input is alphabetical.
Step 2:
In the body of the if statement, print a message that says "Good guess!".
Step 3:
Create an else block that prints "Oops! That is not a valid input." if the preceding conditions are not met.
'''
if len(guess) == 1 and guess.isalpha():
    print('Good guess!')
else: 
    print('Oops! That is not a valid input.')

