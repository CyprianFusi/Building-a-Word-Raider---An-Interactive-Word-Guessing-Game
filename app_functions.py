# Helper function to load word bank

def load_words():
    word_bank = []
    with open('words.txt') as open_file:
        for word in open_file.readlines():
            word_bank.append(word.strip().lower())
    return word_bank

#------------------------------------------------
# Helper function to restart game

def restart_game():
    ans = input('\nDo you wish to start a new game?(Y/N): ').strip().lower()
    if ans == 'n':
        return False
    else:
        return True
    
#--------------------------------------------------
# Helper function to set game variables

def welcome():
    import random
    NAME_OF_GAME = 'MR & MRS WORD'
    print(f'\nWelcome to {NAME_OF_GAME}!\nAn Interactive Word-Guessing Game\n')
    word_bank = load_words()
    correct_word = random.choice(word_bank)

    misplaced_letters = []
    incorrect_letters = []
    max_attempts = 5
    remaining_attempts = max_attempts

    print(f'The word to guess has {len(correct_word)} letters')
    print(f'You have a maximum of {max_attempts} attempts to guess the word...')
    return correct_word, misplaced_letters, incorrect_letters, max_attempts, remaining_attempts

#------------------------------------------------
# Helper function to track game progress

def track_game(misplaced_letters, incorrect_letters, remaining_attempts):
    print(f'\n\nMisplaced Letters: {list(set(misplaced_letters))}')
    print(f'Incorrect letters: {list(set(incorrect_letters))}')
    print(f'\nYou have {remaining_attempts} attempts remaining...')
    
#-----------------------------------------------
# Helper functions to print failure, invalid entry and winning messages

def fail_msg(user_guess, correct_word):
    print('\n\nYou did not win \U0001F620!')
    print(f'\nYour guess: {user_guess}\nThe correct word: {correct_word}\n')
    
#-----------------------------------------------

def invalid_entry(user_guess, remaining_attempts):
    print(f'\nThe entered word ({user_guess}) is invalid! Try again...')
    print(f'\nYou have {remaining_attempts} attempts remaining...')
    
#----------------------------------------------

def congrats_you_won(user_guess, correct_word):
    print(f'\nYou won \U0001F60A \U0001F3C6!!')
    print(f'\nYour guess: {user_guess}\nThe correct word: {correct_word}')
    
#--------------------------------------------
# The Game Logic

def word_guessing_game():
    '''
    MR & MRS WORD is an interactive word-guessing game.
    
    The Rules:
    Prompt the player to guess a n-letter word
    Provide some feedback as to whether the letters within their guess are in the word to guess
    If the player guesses the correct letter in the correct position, that letter will be filled in on the console
    If they guess a correct letter that belongs in the word, but it is in the wrong position, that letter will be added to 
    a list of misplaced letters, and an underscore will be shown in that position on the console
    If they guess a letter that does not belong in the word, that letter will be added to a list of incorrect letters, 
    and an underscore will be shown in that position on the console.
    The user will have a maximum of 5 attempts to guess the word.
        '''
    correct_word, misplaced_letters, incorrect_letters, max_attempts, remaining_attempts = welcome()

    playing = True
    while playing:
        user_guess = input(f'Guess a {len(correct_word)}-letter word: ').strip().lower()
        print()
        if (user_guess.isalpha()) and (len(user_guess) == len(correct_word)):
            if user_guess == correct_word:
                congrats_you_won(user_guess, correct_word)
                
                if restart_game():
                    word_guessing_game()
                else:
                    print('\nGoodbye \U0001F44B and thanks for playing...')
                    break
                break
                    
            else:        
                for correct_letter, guess_letter in zip(correct_word, user_guess):
                    if correct_letter == guess_letter:
                        print(guess_letter, end = '')

                    elif (correct_letter != guess_letter) and (guess_letter in correct_word):
                        misplaced_letters.append(guess_letter)
                        print('_', end = '')
                    else:
                        incorrect_letters.append(guess_letter)
                        print('_', end = '')
                remaining_attempts -= 1

                if (remaining_attempts == 0) and (user_guess != correct_word):
                    fail_msg(user_guess, correct_word)
                    
                    if restart_game():
                        word_guessing_game()
                    else:
                        print('\nGoodbye \U0001F44B and thanks for playing...')
                        break
                    break
            track_game(misplaced_letters, incorrect_letters, remaining_attempts)

        else:
            invalid_entry(user_guess, remaining_attempts)
            continue