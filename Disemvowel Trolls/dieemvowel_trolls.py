def disemvowel(string_):
    new_string = ""
    for i in string_:
        if i not in "aeiouAEIOU":
            new_string+=i
            
    return new_string