def is_valid_IP(strng):
    is_true = True
    if strng == " " or strng == "":
        return False
    elif strng.count(".") == 3:
        listn = strng.split(".")
        for i in listn:
            if len(listn) == 4:
                if len([x for x in i if x.isalpha()]) > 0 or " " in i or i == "":
                    is_true = False
                    break
                elif i.startswith("0") and i != "0":
                    is_true = False
                    break
                elif 0 <= int(i) <= 255 and i.isnumeric():
                    is_true = True
                else:
                    is_true = False
                    break
            else:
                is_true = False
                break
    else:
        return False
    
    return is_true

# complete ✔