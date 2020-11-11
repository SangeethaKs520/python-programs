num =int(input("enter a number"))
sum=0
prod=1
while(num>0):
    dig=num%10
    if(dig==0):
        dig=1
        prod=prod*dig
        dig=0
    else:
        prod=prod*dig
    sum=sum+dig
    num=num//10
print("sum and product of digits is",sum,prod)
