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

print("換電腦猜你的啦")
ans=int(input("請輸入一個數字讓電腦猜"))
gs,gb,cn,cg=(1,100,0,0)
while cg!=ans:
    cg=np.random.randint(gs,gb+1)
    print(f"電腦猜了{cg}")
    if cg > ans:
        gb = cg
        cn+=1
    elif cg < ans :
        gs = cg
        cn+=1
    else:
        print(f"電腦猜{cg}，猜了{cn}次")

