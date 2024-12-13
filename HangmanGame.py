import random
import hangman_stages
import word_file

lives = 6
choosen_word = random.choice(word_file.words)
print(choosen_word)
display = []
for i in range(len(choosen_word)):
    display +='_'
print(display)
game_over = False
while not game_over:
    gussed_letter = input("guess a letter")
    for position in range(len(choosen_word)):
        letter = choosen_word[position]
        if letter == gussed_letter:
            display[position] = gussed_letter
        print(display)
        if gussed_letter not in choosen_word:
            lives -=1
            if lives ==0:
                print("you lose")
        if '_' not in display:
            game_over = True
            print("you won")
        print(hangman_stages.stages[lives])
