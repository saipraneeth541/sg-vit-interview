string="aaabbbbccccca"

res=""
count=1
for i in range(1,len(string)):
    if string[i]==string[i-1]:
        count+=1
    else:
        res+=string[i-1]+str(count)
        count=1
res+=string[i]+str(count)
print(res)
