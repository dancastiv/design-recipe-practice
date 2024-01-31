class DiaryEntry:
    def __init__(self, title, contents):
        self._title = title
        self._contents = contents

    def format(self):
        return f'{self._title}: {self._contents}'
    
    def count_words(self):
        return len(DiaryEntry.format(self).split())

    def reading_time(self, wpm):
        time = DiaryEntry.count_words(self) / wpm
        return round(time)

    def reading_chunk(self, wpm, minutes):
        # Parameters
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   string: a chunk of the contents that the user could read in the
        #           given number of minutes
        #
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that should restart from the beginning.
        
        chunk_length = wpm * minutes
        self.full_text = DiaryEntry.format(self)
        full_text_listed = self.full_text.split()
        return ' '.join(full_text_listed[:chunk_length+1])