from lib.diary import *
from lib.diary_entry import *
from sample_texts import *
import pytest


# test when user adds 2 entries to diary, they can return a list of diary entries 
def test_add_and_return_diary_entries():
    diary = Diary()
    diary_entry1 = DiaryEntry("This is a title", "This is an entry.")
    diary_entry2 = DiaryEntry("This is also a title", "This is my second entry.")
    diary.add(diary_entry1)
    diary.add(diary_entry2)
    assert diary.all() == [diary_entry1, diary_entry2]

# test that if user adds 2 entries to diary and requests the total word count they receive it
def test_diary_word_count():
    diary = Diary()
    diary_entry1 = DiaryEntry("This is a title", "This is an entry.")
    diary_entry2 = DiaryEntry("This is also a title", "This is my second entry.")
    diary.add(diary_entry1)
    diary.add(diary_entry2)
    assert diary.count_words() == 18

def test_diary_word_count_long():
    diary = Diary()
    diary_entry1 = DiaryEntry("This is a title", "This is an entry.")
    diary_entry2 = DiaryEntry("Herbert West: Reanimator", herbert_west)
    diary.add(diary_entry1)
    diary.add(diary_entry2)
    assert diary.count_words() == 11910

# if the user adds entries to diary and and requests the reading time given a specified wpm they'll receive it
def test_diary_reading_time():
    diary = Diary()
    diary_entry1 = DiaryEntry("This is a title", "This is an entry.")
    diary_entry2 = DiaryEntry("This is also a title", "This is my second entry.")
    diary.add(diary_entry1)
    diary.add(diary_entry2)
    assert diary.reading_time(9) == 2

def test_diary_reading_time_long():
    diary = Diary()
    diary_entry1 = DiaryEntry("This is a title", "This is an entry.")
    diary_entry2 = DiaryEntry("Herbert West: Reanimator", herbert_west)
    diary.add(diary_entry1)
    diary.add(diary_entry2)
    assert diary.reading_time(200) == 60

# if user tries to request total word count from an empty diary, exception is raised
def test_empty_diary_word_count():
    diary = Diary()
    with pytest.raises(Exception) as e:
        diary.count_words()
    error = str(e.value)
    assert error == 'Diary is empty. Please add entries.'

# if user triesto request total reading time from an empty diary, exception is raised
def test_empty_diary_reading_time():
    diary = Diary()
    with pytest.raises(Exception) as e:
        diary.reading_time(200)
    error = str(e.value)
    assert error == 'Diary is empty. Please add entries.'

# if user tries to provide 0 as the wpm for the reading time, raise exception
def test_0_wpm_reading_time():
    diary = Diary()
    diary_entry1 = DiaryEntry("This is a title", "This is an entry.")
    diary_entry2 = DiaryEntry("Herbert West: Reanimator", herbert_west)
    diary.add(diary_entry1)
    diary.add(diary_entry2)
    with pytest.raises(Exception) as e:
        diary.reading_time(0)
    error = str(e.value)
    assert error == 'WPM cannot be 0. Please provide a new WPM.'

# given a specific wpm and minutes available, user will recieve the best entry for the given reading time
def test_find_entry_for_reading_time():
    diary = Diary()
    diary_entry1 = DiaryEntry("This is a title", "This is an entry.")
    diary_entry2 = DiaryEntry("Herbert West: Reanimator", herbert_west)
    diary_entry3 = DiaryEntry("The Raven", the_raven)
    diary.add(diary_entry1)
    diary.add(diary_entry2)
    diary.add(diary_entry3)
    entry_to_read = diary.find_best_entry_for_reading_time(150, 10)
    assert entry_to_read == diary_entry3

# if the user provides a 0 for the wpm or the minutes while finding the best entry for reading time, raise exception
def test_find_entry_with_0_wpm():
    diary = Diary()
    diary_entry1 = DiaryEntry("This is a title", "This is an entry.")
    diary_entry2 = DiaryEntry("Herbert West: Reanimator", herbert_west)
    diary_entry3 = DiaryEntry("The Raven", the_raven)
    diary.add(diary_entry1)
    diary.add(diary_entry2)
    diary.add(diary_entry3)
    with pytest.raises(Exception) as e:
        diary.find_best_entry_for_reading_time(0, 10)
    error = str(e.value)
    assert error == 'The WPM or the minutes available cannot be 0. Please provide new values.'

def test_find_entry_with_0_minutes():
    diary = Diary()
    diary_entry1 = DiaryEntry("This is a title", "This is an entry.")
    diary_entry2 = DiaryEntry("Herbert West: Reanimator", herbert_west)
    diary_entry3 = DiaryEntry("The Raven", the_raven)
    diary.add(diary_entry1)
    diary.add(diary_entry2)
    diary.add(diary_entry3)
    with pytest.raises(Exception) as e:
        diary.find_best_entry_for_reading_time(200, 0)
    error = str(e.value)
    assert error == 'The WPM or the minutes available cannot be 0. Please provide new values.'