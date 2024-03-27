print("Enter the operation you want to do")
print("==>1.ADD")
print("==>2.SUBSTRACT")
print("==>3.MULTIPLY")
print("==>4.DIVIDE")
print("==>5.MODLUS")
print("==>6.POWER")
choice=int(input("Enter your choice:"))
num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
if choice==1:
    sum=num1+num2
    print("Result=",sum)
elif choice==2:
    sum=num1-num2
    print("Result=",sum)
elif choice==3:
    sum=num1*num2
    print("Result=",sum)
elif choice==4:
    sum=num1/num2
    print("Result=",sum)
elif choice==5:
    sum=num1%num2
    print("Result=",sum)
elif choice==6:
    i = 1
    power = 1
    while i<=num2:
        power =power*num1
        i=i+1
    print("Result=",power)
else:
    print("Enter valid choice")

