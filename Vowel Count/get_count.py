def get_count(sentence):
    count = 0
    for i in sentence:
        if i in "aeiouAEIOU":
            count+=1
    return count