arr = input().split('-')
res = 0
for i in arr[0].split('+'):
    res+=int(i)
for i in arr[1:]:
    for j in i.split('+'):
        res -= int(j)
print(res)