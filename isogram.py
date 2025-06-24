def is_isogram(string):
    string = string.lower()
    letters = (word for word in string if string.isalpha())
    if len(set(letters)) == len(letters):
        return True
