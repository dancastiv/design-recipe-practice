# File: lib/diary.py

class Diary:
    def __init__(self):
        self.all_diary_entries = []

    def add(self, entry):
        self.all_diary_entries.append(entry)

    def all(self):
        return self.all_diary_entries

    def count_words(self):
        if len(self.all_diary_entries) == 0:
            raise Exception('Diary is empty. Please add entries.')
        total_words = 0
        for entry in self.all_diary_entries:
            total_words += entry.count_words()
        return total_words

    def reading_time(self, wpm):
        if wpm == 0:
            raise Exception('WPM cannot be 0. Please provide a new WPM.')
        if len(self.all_diary_entries) == 0:
            raise Exception('Diary is empty. Please add entries.')
        total_words = self.count_words()
        return round(total_words / wpm)

    def find_best_entry_for_reading_time(self, wpm, minutes):
        if len(self.all_diary_entries) == 0:
            raise Exception('Diary is empty. Please add entries.')
        if wpm == 0 or minutes == 0:
            raise Exception('The WPM or the minutes available cannot be 0. Please provide new values.')
        readable_entries = []
        total_words = wpm * minutes
        for entry in self.all_diary_entries:
            if entry.count_words() < total_words:
                readable_entries.append(entry)
        readable_entries.sort(key=lambda entry: entry.count_words()) 
        return readable_entries[-1]