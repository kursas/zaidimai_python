#Hint: Create a List of secret words and randomly pick a word.
# Now represent each word as _ and give user chances to guess the
# word if the user guesses the word right then replace _ with the word.
import time
import random
name = input("What is your name? ")
print ("Hello, " + name, "Time to play hangman!")
time.sleep(1)
print ("Start guessing...\n")
time.sleep(0.5)
## A List Of Secret Words
words = ['python','programming','treasure','creative','medium','horror']
word = random.choice(words)
guesses = ''
turns = 5
while turns > 0:         
    failed = 0             
    for char in word:      
        if char in guesses:    
            print (char,end="")    
        else:
            print ("_",end=""),     
            failed += 1    
    if failed == 0:        
        print ("\nYou won") 
        break              
    guess = input("\nguess a character:") 
    guesses += guess                    
    if guess not in word:  
        turns -= 1        
        print("\nWrong")    
        print("\nYou have", + turns, 'more guesses') 
        if turns == 0:           
            print ("\nYou Lose") 
#output
What is your name? andrius
Hello, andrius Time to play hangman!
Start guessing...

______
guess a character:100

Wrong

You have 4 more guesses
______
guess a character:10

Wrong

You have 3 more guesses
______
guess a character:action

Wrong

You have 2 more guesses
__t_on
guess a character:althon

Wrong

You have 1 more guesses
__thon
guess a character:python
python
You won

Process finished with exit code 0
