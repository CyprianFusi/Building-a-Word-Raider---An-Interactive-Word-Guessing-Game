# Building-a-Word-Raider---An-Interactive-Word-Guessing-Game
Applying recursive function call, Separation of Concerns Principle and functional programming in building a word guessing game.

## The Rules
* Prompt the player to guess a **n-letter word**
* Provide some feedback as to whether the letters within their guess are in the word to guess
* If the player guesses the **correct letter in the correct position**, that letter will be filled in on the console
* If they guess a correct letter that belongs in the word, but it is **in the wrong position**, that letter will be added to a list of **misplaced letters, and an underscore will be shown in that position** on the console
* If they guess a **letter that does not belong in the word**, that letter will be added to a **list of incorrect letters, and an underscore will be shown** in that position on the console. 
* The user will have a **maximum of 5 attempts** to guess the word.

Helper functions and the game logic are implemented in the module `app_function.py`
