def estimate_reading_time(text):
    if text == '':
        return 'Please provide a text.' 
    word_count = len(text.split())
    if word_count < 200:
        return 'Estimated reading time: less than a minute.'
    if word_count >= 200:
        time = word_count / 200
        hours = round(time//60)
        minutes = round(time%60)
        if hours == 1:
            hour_string = str(hours) + ' hour'
        else:
            hour_string = str(hours) + ' hours'

        if minutes == 1:
            minute_string = str(minutes) + ' minute'
        else:
            minute_string = str(minutes) + ' minutes'
        if hours < 1:
            return f'Estimated reading time: {minute_string}.'
        else:
            return f'Estimated reading time: {hour_string} and {minute_string}.'
    

    



