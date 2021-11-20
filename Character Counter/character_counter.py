def validate_word(word):
    string = word.lower()
    for i in string:
        if string.count(i) != string.count(string[0]):
            return False
    return True
    
    
        
    
    
    