def alphanumeric(password):
    
    if password == "": # check if password is an empty string
        return False
    
    for i in password:
        if i.isspace() or i == '_': # check if character is a space or an underscore
            return False
        elif not i.isupper(): # check if character isnt an uppercase
            if not i.islower(): # check if character isnt a lowercase
                if not i.isdigit(): # check if isnt character isnt a digit
                    return False
    return True