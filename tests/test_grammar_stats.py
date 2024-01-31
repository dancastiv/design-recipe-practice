import pytest
from lib.grammar_stats import *

# if the text to be checked for grammar is empty, raise exception

def test_empty_text():
    empty_text = GrammarStats()
    with pytest.raises(Exception) as e:
        empty_text.check('')
    error = str(e.value)
    assert error == 'Please provide text to analyse.'

# given a text beginning with a capital letter and ending with an appropriate punctuation mark, return True. False otherwise.

def test_check_proper_grammar():
    grammar = GrammarStats()
    assert grammar.check('This is a grammatically correct sentence!') == True
    assert grammar.check('this is not a grammatically correct sentence (lol)') == False

# return percentage of checked texts that are grammatically correct
    
def test_percentage_good():
    percentage = GrammarStats()
    percentage.check('This is a grammatically correct sentence!')
    percentage.check('this is not a grammatically correct sentence')
    assert percentage.percentage_good() == 50