# Define a secret number (this would be the number picked in the game)
 # Change this to test different cases

def guess(num: int) -> int:
    if num > secret_number:
        return -1
    elif num < secret_number:
        return 1
    else:
        return 0

def guessNumber(n):
    l = 0
    r = n
    while l <= r:
        m1 = l+(r-l)//3
        m2 = r-(r-l)//3
        if guess(m1) == 0:
            return m1
        if guess(m2) == 0:
            return m2
        if guess(m1)+guess(m2) == 0:
            l = m1+1
            r = m2-1
        elif guess(m1) == -1:
            r = m1-1
        else:
            l = m2+1

secret_number = 5
guessNumber(10)


