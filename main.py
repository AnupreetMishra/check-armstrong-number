
num = int(input("Enter the number:"))


n1=num%10
temp=num//10
n2=temp%10
n3=temp//10

print(n1,n2,n3)

new_num=(n1**3)+(n2**3)+(n3**3)
if new_num==num:
  print("given number is armstrong number")

else:
  print("given number is not a armstrong number")

