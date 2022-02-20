# This is a header for the application
# You should read this header and insert your name and your date below as part of the peer review
# This is a typical part of any program
# Author: Phillip Dec
# Creation Date: 12 February 2022
# Below is a simple program with 10 issues (some are syntax errors and some are logic errors.  You need to identify the issues and correct them.

import random
import time

def displayIntro():
	print('''You are in a land full of dragons. In front of you,
	you see two caves. In one cave, the dragon is friendly
	and will share his treasure with you. The other dragon
	is greedy and hungry, and will eat you on sight.''')

 #I don't believe you need this second print command
	print()

def chooseCave():
    cave = ''
	while cave != '1' and cave != '2':
		print('Which cave will you go into? (1 or 2)')
		cave = input()
#Corrected variable to match, cave instead of caves
	return cave

def checkCave(cave):
	print('You approach the cave...')
	#sleep for 2 seconds
	time.sleep(2)
	print('It is dark and spooky...')
	#sleep for 2 seconds
#changed the value to match the note from 3 to 2
	time.sleep(2)
	print('A large dragon jumps out in front of you! He opens his jaws and...')
	print()
	#sleep for 2 seconds
	time.sleep(2)
	friendlyCave = random.randint(1, 2)
#Changed the line to reflect what would happen on a roll of 1 instead
	if friendlyCave == 1:
		print('Gives you his treasure!')
	else:
	#added the parentheses
		print('Gobbles you down in one bite!')

#Corrected parameter to True instead of 'yes' to create a loop
playAgain = True

#corrected the loop parameter, took off the parts that came after playAgain
while playAgain:
	displayIntro()
#Changed cavenumber to choosecave to call on the function defined above
	chooseCave()
	checkCave()
    
	print('Do you want to play again? (yes or no)')
	playAgain = input()
	#changed the "" to '' around no
	if playAgain == 'no':
    # Set a paramater to end loop by setting it to = false on 'no'
		playAgain = False
	#Incorrect spelling, changed "planing" to playing
		print("Thanks for playing")

