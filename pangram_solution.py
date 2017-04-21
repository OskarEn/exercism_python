def IsPanagram(phrase):
    phrase = phrase.lower()
    #if string.count(char) >= 26:
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in phrase:
            return False
        return True

#print(IsPanagram("The quick red fox jumps over the lazy dog"))