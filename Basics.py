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

Bs6/

for i in range(1,11): 
  print(i)  //dùng for để chạy vòng lặp từ 1 đến 10

i=0 
while(i<10): 
  i+=1 
  print(i) //dùng while để chạy vòng lặp từ 1 đến 10

Bs7/

aNum = int(input("Enter a number: "))
for i in range (1,aNum+1):
  print(f"{aNum}x{i}=",aNum * i) // in phép nhân tổng quát từ 1 tới số bất kì

aNum = int(input("Enter a number: "))
for i in range(1, 11): 
    print(f"{aNum} x {i} = {aNum * i}") //in phép nhân cụ thể là từ 1 tới 10 với số bất kì


print(f"Multiplication Table of {aNum}")
for i in range(1, 11):
    print(f"{aNum} x {i:2} = {aNum * i:3}") //ép kiểu để chỉnh các kích thước của các biến trong bảng phép nhân


















