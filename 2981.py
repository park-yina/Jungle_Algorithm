import sys
a=input()
b=input()
temp_a=str(a[::-1])
temp_b=str(b[::-1])
print(min(temp_a,temp_b))