from itertools import permutations

def get_pins(observed):
    result = []
    instead_dict = {
        "1": ["2", "4"],
        "2": ["1", "3", "5"],
        "3": ["2", "6"],
        "4": ["1", "5", "7"],
        "5": ["2", "4", "6", "8"],
        "6": ["3", "5", "9"],
        "7": ["4", "8"],
        "8": ["5", "7", "9", "0"],
        "9": ["6", "8"],
        "0": ["8"]
    }
    
    my_dict = dict()
    res = []
    
    first = permutate(observed)
    
    for i in first:
        if len(first) == 1:
            for x in instead_dict[i]:
                res.append(x)
                res.append(i)
        elif len(first) == 2:
            nums = []
            nums.append(i)
            for x in i:
                for l in range(len(instead_dict[x])):
                    nums.append(i[0] + instead_dict[x][l])
                    nums.append(instead_dict[x][l] + i[1])
                    nums.append(instead_dict[x][l] + instead_dict[x][l])
                    if l == 0:
                        nums.append(instead_dict[i[0]][l] + instead_dict[i[1]][l+1])
                        nums.append(instead_dict[i[1]][l] + instead_dict[i[0]][l+1])
                        nums.append(instead_dict[i[0]][l+1] + instead_dict[i[1]][l])
                        nums.append(instead_dict[i[1]][l+1] + instead_dict[i[0]][l])
                    else:
                        nums.append(instead_dict[i[0]][l-1] + instead_dict[i[1]][l])
                        nums.append(instead_dict[i[1]][l-1] + instead_dict[i[0]][l])
                        nums.append(instead_dict[i[0]][l] + instead_dict[i[1]][l-1])
                        nums.append(instead_dict[i[1]][l] + instead_dict[i[0]][l-1])
            res = list(set(nums))
            if observed[0] != observed[1]:
                for i in res:
                    if i[0] == i[1]:
                        res.remove(i)
            for i in res:
                if i[0] not in instead_dict[observed[0]]:
                    res.remove(i)
                elif i[1] not in instead_dict[observed[1]]:
                    res.remove(i)
            return res
    return list(set(res))
        
        
def permutate(object):
    first = []
    for i in list(permutations(object)):
        first.append("".join(list(i)))
    return first