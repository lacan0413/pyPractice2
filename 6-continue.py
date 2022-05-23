n=0
for x in [0,1,2,3]:
    if x%2==0: #x是偶數
        continue #偶數非0直接進到下個迴圈
    print(x)
    n+=1
print("最後的n:", n)