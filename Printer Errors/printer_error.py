def printer_error(s):
    alpha = "abcdefghijklm"
    counter = 0
    for i in s:
        if i not in alpha:
            counter+=1
    return str(counter) + "/" + str(len(s))