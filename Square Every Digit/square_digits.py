def square_digits(num):
    string = ""
    for i in str(num):
        current_num = int(i) ** 2
        string += str(current_num)
        
    return int(string)