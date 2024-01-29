from lib.proper_grammar import *
import pytest

#check for capitalization at the beginning of the text

def test_capitalization_present():
    capitalization = check_grammar('I am a sentence.')
    assert capitalization == True

# check for period at the end

def test_check_for_period():
    no_period = check_grammar('I guess I am not a sentence after all')
    assert no_period == False
    period = check_grammar('I am a sentence.')
    assert period == True

# check for any type of punctuation at the end
def test_check_for_punctuation():
    punctuation = check_grammar('I think I am a sentence?')
    assert punctuation == True
    punctuation = check_grammar('I am for sure a sentence!')
    assert punctuation == True

def test_empty_string():
    with pytest.raises(Exception) as e:
        check_grammar('')
    error = str(e.value)
    assert error == 'Please provide text to analyse.'