import numpy as np
n=np.random.randint(1,101)
guess,small,big=(0,1,100)
while n!=guess:
    guess=int(input(f"從{small}到{big}猜個數字吧"))
    if guess > big or guess <small:
        print(f"超出範圍啦，從{small}到{big}猜個數字吧")
    else:
        if guess > n:
            print("太大囉！")
            big=guess
        elif guess < n :
            print("太小囉！")
            small=guess
        else:
            print("恭喜猜對啦！")
        

