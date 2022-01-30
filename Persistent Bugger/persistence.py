def persistence(n):
    count = 0
    while True:
        if n < 10:
            break
        digit_multiples = 1
        for i in str(n):
            digit_multiples *= int(i)
        n = digit_multiples         
        count += 1
    return count