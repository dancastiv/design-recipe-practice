class DiaryEntry:
    def __init__(self, title, contents):
        self._title = title
        self._contents = contents
        self._read_contents = 0

    def format(self):
        return f'{self._title}: {self._contents}'
    
    def count_words(self):
        return len(DiaryEntry.format(self).split())

    def reading_time(self, wpm):
        time = DiaryEntry.count_words(self) / wpm
        return round(time)

    def reading_chunk(self, wpm, minutes):
        chunk_length = wpm * minutes
        full_text = DiaryEntry.format(self)
        full_text_listed = full_text.split()
        chunk = ' '.join(full_text_listed[self._read_contents:self._read_contents+chunk_length+1])
        self._read_contents += chunk_length +1
        if self._read_contents > len(full_text_listed):
            self._read_contents = 0
        return chunk