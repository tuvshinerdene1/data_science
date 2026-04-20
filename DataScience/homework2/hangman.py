# Problem Set 2, hangman.py
# Name:
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, "r")
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    inFile.close()
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    """
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for char in secret_word:
        if char not in letters_guessed:
            return False
    
    return True
            


def get_guessed_word(secret_word, letters_guessed):
    """
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    result = ""
    for char in secret_word:
        if char in letters_guessed:
            result += char
        else:
            result += '_ '
    return result


def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    letters = string.ascii_lowercase
    result = ""
    for char in letters:
        if char not in letters_guessed:
            result += char
    return result


def hangman(secret_word):
    """
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    tries_left = 6
    warnings_left = 3
    guessed_letters = []
    is_won = False

    print(f"the word has {len(secret_word)} letters")

    while tries_left > 0 :  

      print("*******************************")
      print(f"you have {tries_left} tries left")
      print(f"Available letters: {get_available_letters(guessed_letters)}")
      letter = input("Please guess a letter :")
      letter = letter.lower()

      if not validate_letter(letter):
          warnings_left = warn('invalid_input', warnings_left)
          if warnings_left > 0:
            print(f" you have {warnings_left} warnings left: {get_guessed_word(secret_word,guessed_letters )} ")
            
          else:
              tries_left = punish(tries_left, 1)
              print(f"{get_guessed_word(secret_word, guessed_letters)}")
      else:
          
          if letter in guessed_letters:
              warnings_left  = warn('duplicate', warnings_left)

              if warnings_left > 0:
                print(f"warning for now . warning left {warnings_left} : {get_guessed_word(secret_word, guessed_letters)}")
              else:
                  tries_left = punish(tries_left, 1)
                  print(f"{get_guessed_word(secret_word, guessed_letters)}")

          elif letter in secret_word:
            guessed_letters.append(letter)
            print(f"good guess: {get_guessed_word(secret_word, guessed_letters)}")
            if is_word_guessed(secret_word, guessed_letters):
                is_won = True
                break
          else:
              guessed_letters.append(letter)
              if letter in "aeiou":
                  tries_left = punish(tries_left, 3)
              else:
                  tries_left = punish(tries_left,1)
                  
              print(f"oops that letter is not in my word : {get_guessed_word(secret_word, guessed_letters)}")
    if is_won:
      print("Congratulations, you won!")
      score = tries_left * len(set(secret_word))
      print(f"Your total score for this game is: {score}")
    else:
      print(f"Sorry, you ran out of guesses. The word was {secret_word}.")

def warn(type, warnings_remaining):
    if type == 'invalid_input':
        print('invalid input')
    else:
        print('you already picked this letter')
    warnings_remaining -= 1
    if warnings_remaining > 0:
        print("warning for now")
    return warnings_remaining

def punish(tries_left, penalty_point):
    print(f'applying penalty: - {penalty_point} points')
    return tries_left - penalty_point

def validate_letter(letter):
    if letter == "*":
        return True
    elif len(letter) > 1 or letter not in string.ascii_lowercase:
        return False
    return True
      
              
          



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
# (hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------


def match_with_gaps(my_word, other_word):
    """
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise:
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    my_word = my_word.replace(" ", "")
    if len(my_word) != len(other_word):
        return False
    for x in range(len(my_word)):
        if(my_word[x]=="_"):
            continue
        else:
            if (my_word[x] != other_word[x]):
                return False
    return True
    


def show_possible_matches(my_word):
    """
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    result = " "
    for word in wordlist:
        if match_with_gaps(my_word, word):
            result += f" {word}"
    print(result)
            
    


def hangman_with_hints(secret_word):
    """
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word.

    Follows the other limitations detailed in the problem write-up.
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    tries_left = 6
    warnings_left = 3
    guessed_letters = []
    is_won = False

    print(f"the word has {len(secret_word)} letters")

    while tries_left > 0 :  

      print("*******************************")
      print(f"you have {tries_left} tries left")
      print(f"Available letters: {get_available_letters(guessed_letters)}")
      letter = input("Please guess a letter :")
      letter = letter.lower()

      if not validate_letter(letter):
          warnings_left = warn('invalid_input', warnings_left)
          if warnings_left > 0:
            print(f" you have {warnings_left} warnings left: {get_guessed_word(secret_word,guessed_letters )} ")
            
          else:
              tries_left = punish(tries_left, 1)
              print(f"{get_guessed_word(secret_word, guessed_letters)}")
      elif letter == "*":
        if(len(guessed_letters) >= 3):
          show_possible_matches(get_guessed_word(secret_word,guessed_letters ))
        else:
            print("At least 3 letters need to be guessed already.")
      else:
          
          if letter in guessed_letters:
              warnings_left  = warn('duplicate', warnings_left)

              if warnings_left > 0:
                print(f"warning for now . warning left {warnings_left} : {get_guessed_word(secret_word, guessed_letters)}")
              else:
                  tries_left = punish(tries_left, 1)
                  print(f"{get_guessed_word(secret_word, guessed_letters)}")

          elif letter in secret_word:
            guessed_letters.append(letter)
            print(f"good guess: {get_guessed_word(secret_word, guessed_letters)}")
            if is_word_guessed(secret_word, guessed_letters):
                is_won = True
                break
          else:
              guessed_letters.append(letter)
              if letter in "aeiou":
                  tries_left = punish(tries_left, 3)
              else:
                  tries_left = punish(tries_left,1)
                  
              print(f"oops that letter is not in my word : {get_guessed_word(secret_word, guessed_letters)}")
    if is_won:
      print("Congratulations, you won!")
      score = tries_left * len(set(secret_word))
      print(f"Your total score for this game is: {score}")
    else:
      print(f"Sorry, you ran out of guesses. The word was {secret_word}.")


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    secret_word = choose_word(wordlist)
    print(secret_word)
    hangman_with_hints(secret_word)

    ###############

    # To test part 3 re-comment out the above lines and
    # uncomment the following two lines.

    # secret_word = choose_word(wordlist)
    # hangman_with_hints(secret_word)
