

def lemonadeChange(bills):
    count = {5: 0, 10: 10, 20: 0}
    for i in bills:
        if i == 5:
            count[i] += 1
        elif i == 10:
            count[10] += 1
            if not count[5]:
                return False
            count[5] -= 1
        else:
            count[20] += 1
            change = False
            if count[10] and count[5]:
                count[5] -= 1
                count[10] -= 1
                change = True
            elif count[5] > 2:
                count[5] -= 3
                change = True
            if not change:
                return False
    return True
lemonadeChange([5,5,5,10,5,5,10,20,20,20])