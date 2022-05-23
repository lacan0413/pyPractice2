n=input("輸入一個正整數: ")
n=int(n) #轉換輸入成數字
for i in range(n): # i 從 0 ~ n-1
    if i*i==n:
        print("整數平方根", i)
        break #不會跑else
else:
    print("沒有整數平方根")
