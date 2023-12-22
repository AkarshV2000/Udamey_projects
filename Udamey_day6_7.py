# Day 6 was basically about while loop, nothing much interesting
# Day 7 is a project c/d "Hangman Game"
import random
print("**HANGMAN GAME**")
stages = [
'''_ _ _ _ _ _ _

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''',
'''_ _ _ _ _ _ _

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''',
'''_ _ _ _ _ _ _

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''',
'''_ _ _ _ _ _ _

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
'''_ _ _ _ _ _ _

  +---+
  |   |
  O   |
  |   |
      |
      |
=========''',
'''_ _ _ _ _ _ _

  +---+
  |   |
  O   |
      |
      |
      |
=========''',
]
    
end_of_game = False
random_words = [
    "banana", "elephant", "courage", "keyboard", "sunflower",
    "mountain", "whisper", "umbrella", "fireplace", "rainbow"
]

chosen_word = random.choice(random_words)
# print(chosen_word)
lives = 6
display = []

for i in range(len(chosen_word)):
    display+= "_"
print(f" Choosen word contains this many letters: {display}")



while not end_of_game:
    guess = input(" Guess a letter: ").lower()
    
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        lives -=1
        if lives == 0:
            end_of_game = True
            print("**You Loose**")
        print(stages[lives])

    print(display)
    if "_" not in display:
        end_of_game = True
        print("You Win")

        