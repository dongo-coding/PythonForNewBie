Bs1/ 

name = input("Enter your name : ")
print(f"Hello, {name}") //ép kiểu để hiện tên mà người dùng nhập
print("Welcome to Python") //input Bs1

Enter your name : Do Ngo
Hello, Do Ngo
Welcome to Python   //Example output Bs1

Bs2/

name = input("Enter your name: ")
age = int(input ("Enter your age:"))
print(f"Hi {name}, you are {age} years old") //input Bs2 //ép kiểu để hiện tên, tuổi theo đúng như người dùng nhập

Enter your name: Do Ngo
Enter your age:19
Hi Do Ngo, you are 19 years old //Example output Bs2

Bs3/

fnum = int(input ("Enter your first number: "))
snum = int(input ("Enter your second number: "))
print("Sum of them: " , fnum + snum)
print("Difference of them: " , fnum - snum)
print("Production of them: " , fnum * snum)
print(f"Normal division of them: {fnum / snum:.2f} ") //ép kiểu số thực, làm tròn đến 2 chữ số thập phân, in ra phép chia bình thường
print("Integer division of them: " , fnum // snum) // in ra phép chia lấy phần nguyên 

//input Bs3

Enter your first number: 4
Enter your second number: 3
Sum of them:  7
Difference of them:  1
Production of them:  12
Normal division of them: 1.33 
Integer division of them:  1 //Example output Bs3

Bs4/

aNum = int(input("Enter any number: ")) 
if aNum%2==0: 
  print(f"{aNum} is even") 
else: print(f"{aNum} is odd") //input Bs4

Enter any number: 13
13 is odd  //Exanple output Bs4


Bs5/

aNum = int(input("Enter any number: "))
if aNum<0:
  print("The number is negative")
elif aNum>0:
  print("The number is positive")
elif aNum==0:
  print("The number is zero")
else:
  print("The number is not exist in any types") //input Bs5

Enter any number: -987654321
The number is negative       //Example output Bs5  











