
# 📘 Hangman Game Challenge

## 🎯 Objective

Create the classic Hangman word-guessing game where players guess letters to reveal a hidden word before running out of attempts. You'll practice string manipulation, loops, conditionals, and working with lists in Python.

## 📝 Tasks

### 🛠️ Set Up the Game Structure

#### Description
Start by creating the foundation of your game. You'll set up a word list, initialize game variables, and display the initial game state to the player.

#### Requirements
Completed program should:

- Have a predefined list of at least 5 words to guess from
- Randomly select one word at the start of each game
- Initialize variables to track incorrect guesses remaining (suggest 6 attempts)
- Display the hidden word in underscore format (e.g., `_ _ _ _ _ _`)

### 🛠️ Implement Guess Handling

#### Description
Build the core gameplay loop that accepts player guesses, validates them, and updates the game state based on correct or incorrect guesses.

#### Requirements
Completed program should:

- Accept single letter guesses from the player
- Check if the guessed letter is in the word
- Update the display to show correctly guessed letters
- Display list of incorrect guesses made so far
- Provide feedback when a guess is already made

### 🛠️ Add Win/Lose Logic

#### Description
Complete the game by adding win and lose conditions with appropriate messages and replay functionality.

#### Requirements
Completed program should:

- End the game when the player guesses the word (display win message)
- End the game when incorrect guesses reach zero (display lose message and reveal the word)
- Show the final word and game result clearly
- Ask if the player wants to play again
