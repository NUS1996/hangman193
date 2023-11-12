import random 
'''
Step 1:
Create a list containing the names of your 5 favorite fruits.


Step 2:
Assign this list to a variable called word_list.


Step 3:
Print out the newly created list to the standard output (screen). 
'''

word_list = ['banana', 'avocado', 'apple', 'watermelon', 'grapes']
print(word_list)

'''
To accomplish this task, you will need to use the 'random' module.
The random module is one of Python's built-in modules.
It has a choice method which returns a random item from a given sequence.
'''
word = random.choice(word_list)
print(word)
guess = input('Enter a single letter: ')
'''
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

