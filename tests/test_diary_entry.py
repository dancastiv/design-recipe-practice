from lib.diary_entry import *
from sample_texts import *

# test that given a title and contents it returns them in "Title: This is the content" format
def test_format_entry():
    diary_entry = DiaryEntry('Title', 'This is the content.')
    formatted_entry = diary_entry.format()
    assert formatted_entry == 'Title: This is the content.'

# check that given a diary entry it returns the word count
def test_count_words():
    diary_entry = DiaryEntry('Herbert West: Reanimator', herbert_west)
    word_count = diary_entry.count_words()
    assert word_count == 11902


# test that given a specific wpm it'll return the estimate reading time in minutes

def test_reading_time():
    diary_entry = DiaryEntry('Herbert West: Reanimator', herbert_west)
    reading_time = diary_entry.reading_time(200)
    assert reading_time == 60

    diary_entry = DiaryEntry('The Raven', the_raven)
    reading_time = diary_entry.reading_time(150)
    assert reading_time == 7

# test that given a wpm and an amount of minutes, return the chunk that will be read in that amount of time
# if called again, check it returns the next chunk
    
# def test_reading_chunk():
#     diary_entry = DiaryEntry('Lorem', lorem)
#     chunk = diary_entry.reading_chunk(200, 2)
#     assert chunk == lorem_2_min_chunk