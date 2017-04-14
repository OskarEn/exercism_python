def IsIsogram(string):
    string = string.lower()
    for char in string:
        if string.count(char) > 1:
            return False
        else:
            return True

#print(IsIsogram("Lumberjack"))