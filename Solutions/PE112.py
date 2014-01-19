# Project Euler 112
# Bouncy Number
# Kai Kang

def getRelation(number, anotherNumber):
    if number == anotherNumber:
        return 0
    elif number < anotherNumber:
        return 1
    else:
        return 2

def isBouncy(number):
    # number should have at least three digits
    original_relation = getRelation(int(str(number)[0]),int(str(number)[1]))
    compare = int(str(number)[1])
    for char in str(number)[2:]:
        relation = getRelation(compare, int(char))
        if original_relation != 0 and relation != 0:
            if original_relation != relation:
                return True
        if original_relation == 0:
            original_relation = relation
        compare = int(char)
    return False



proportion = 0.9
current_number = 21780
current_bouncy_numbers = 0.9 * 21780

while proportion < 0.99:
    current_number += 1
    if isBouncy(current_number):
        current_bouncy_numbers += 1
        proportion = current_bouncy_numbers / float(current_number)
print current_number
