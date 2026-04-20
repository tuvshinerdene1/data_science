import string

import pytest
from hangman import get_available_letters
from hangman import is_word_guessed
from hangman import get_guessed_word
from hangman import match_with_gaps

def test_is_word_guessed_1():
    assert is_word_guessed("apple", ['a','p','l','e']) == True

def test_is_word_guessed_2():
    assert is_word_guessed("apple", ['a','p','l']) == False

def test_get_guessed_word1():
    assert get_guessed_word("apple", ['a', 'p']) == "app_ _ "

def test_get_guessed_word2():
    assert get_guessed_word("apple", ['a', 'p', 'l', 'e']) == "apple"

def test_get_guessed_word3():
    assert get_guessed_word("apple", []) == "_ _ _ _ _ "
def test_basic_functionality():
    """Test a standard mix of guessed and unguessed letters."""
    guessed = ['a', 'b', 'c']
    result = get_available_letters(guessed)
    # Check that 'a', 'b', 'c' are gone and 'd' remains
    assert 'a' not in result
    assert 'd' in result
    assert len(result) == 23

def test_no_guesses():
    """If no letters are guessed, it should return the full alphabet."""
    assert get_available_letters([]) == string.ascii_lowercase

def test_all_guessed():
    """If every letter is guessed, it should return an empty string."""
    all_letters = list(string.ascii_lowercase)
    assert get_available_letters(all_letters) == ""

def test_match_1():
    assert match_with_gaps("a_ _ _ a", "abbba") == True

def test_match_2():
    assert match_with_gaps("a_ _ _ a", "abbbb") == False

def test_match_3():
    assert match_with_gaps("abbbc", "abbba") == False




