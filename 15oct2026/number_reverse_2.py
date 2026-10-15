num=int(input("enter the number:"))
rev=0
while(num>0):
    last_value=num%10
    num=num//10
    rev=(rev*10)+last_value
print(rev)