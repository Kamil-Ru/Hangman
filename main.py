#Step 1 
import random

word_list = ["aardvark", "baboon", "camel"]

# 1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')
display = ["_" for _ in range(len(chosen_word))]
print(display)

# 2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Guess a letter: \n").lower()


# 3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

for ID_letter in range(len(chosen_word)):
    
    if chosen_word[ID_letter] == guess:
        display[ID_letter] = guess
        print(True)
    else:
        print(False)
    
        

print(display)