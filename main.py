import random
from replit import clear 
from hangman_art import stages, logo
from hangman_words import word_list

print(logo)
chosen_word = random.choice(word_list)
lives = 6

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = ["_" for _ in range(len(chosen_word))]
#Displey blanks
print(display)

game_on = True
guesses_letters = ''

while game_on:
    
    guess = input("Guess a letter: \n").lower()
    clear()
    #Printing ifromation if letter has alredy chosen
    if guess in guesses_letters:
        print(f"Letter {guess} has already chosen")
    
    #Check guessed letter
    for ID_letter in range(len(chosen_word)):

        if chosen_word[ID_letter] == guess:
            display[ID_letter] = guess
    
    #Adding gueses leetter to string with the letters
    guesses_letters += guess
            
    #Check if user is wrong.
    if guess not in chosen_word:
        print(f'Letter "{guess}" is not in the word.')
        lives -= 1
        if lives == 0:
            game_on = False
            print('GAME OVER')
    
    #Check if user has got all letters.            
    elif '_' not in display:
        game_on = False
        print('YOU WIN')
            
    #Join all the elements in the list and turn it into a String.        
    print(f"{' '.join(display)}")   
    
    print(stages[lives])
    
        
print(display)
