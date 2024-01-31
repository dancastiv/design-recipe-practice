class GrammarStats:
    def __init__(self):
        self.total_counter = 0
        self.correct_counter = 0

    def check(self, text):
        if text == '':
            raise Exception('Please provide text to analyse.')
        self.total_counter += 1
        if text[0].isupper() and text[-1] in '.?!':
            self.correct_counter += 1
            return True
        else:
            return False

    def percentage_good(self):
        return (self.correct_counter / self.total_counter) * 100
