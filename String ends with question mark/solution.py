def solution(string, ending):
    if ending != "":
        if ending in string:
            if ending[-1] == string[-1]:
                return True
    elif ending == "":
        return True
    return False
   