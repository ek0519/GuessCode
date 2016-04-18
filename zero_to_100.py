# -*- coding='utf-8' -*-
import random
# 隨機挑出一個數字 0-100
ans = random.randint(0,99)
lindex = 0
rindex = 100

def input_number():
    n = input('請輸入一個數\n')
    number_or_not = n
    if number_or_not.isnumeric():
        return n
    else:
        print('輸入含非數字，請重新輸入')
        i = 'c'
        while (i.isnumeric()==False):
            n = input('請輸入一個數\n')
            i = n
            if (i.isnumeric()==False):
                print('輸入含非數字，請重新輸入')
        return n
# 請輸入一個數
guess = int(input_number())
n=1
while (ans != guess):
        if ans > guess:
            if guess <= lindex:
                print('等小於 %d,請重新輸入' % lindex)
            else:
                lindex = guess
        elif ans < guess:
            if guess >= rindex:
                print('等大於 %d,請重新輸入'% rindex)
            else:
                rindex = guess      
        print("終極密碼 %d 到 %d" % (lindex, rindex))
        n += 1
        guess = int(input_number())
print('Bingo!您猜的數字為 %d,總共猜了 %d 次' % (guess, n))
