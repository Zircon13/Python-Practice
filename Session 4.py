string=input("Enter Number:")
number=list(map(int, string.split()))
print(number)

string=input("Enter Number:")
number=list(map(int, string.split()))
tot=sum(number)
print(tot)

string=input("Enter Number:")
number=list(map(int, string.split()))
m=min(number)
n=max(number)
print(f"Max: {n}\nMin: {m}")

string=input("Enter Number:")
number=list(map(int, string.split()))
even=0
odd=0
for num in number:
    if num%2==0:
        even+=1
    else:
        odd+=1
print(f"number of even: {even}\nnumber of odd: {odd}")

string=input("Enter Number:")
number=list(map(int, string.split()))
rev=number[::-1]
print(rev)

string=input("Enter Number:")
number=list(map(int, string.split()))
scn=sorted(set(number), reverse=True)[1] if len(number)>1 else None
print(f"Second largest number: {scn}")

string=input("Enter Number:")
number=list(map(int, string.split()))
u=list(set(number))
print(f"numbers: {u}")