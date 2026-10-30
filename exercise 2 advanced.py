a = 5
b = 10.1
c = 7.1

a += 3
b *= 2
c %= 4

result = a**2 + b**2 + c**2
print(result)

#Question 2

x = int(input("enter a number:"))
y = int(input("enter a number:"))
z = int(input("enter a number:"))

is_even = x % 2 == 0 
is_positive = y > 0 
is_in_range = 10 <= z <=50

final_condition = is_even and is_positive and is_in_range

print(final_condition)

#Question 3

score = float(input("enter your base score"))
score = score + 5 - 10
score = max(0, min(100, score))
if score >= 90: 
  grade = "A"
elif score >= 80:
  grade = "B"
elif score >= 70:
  grade = "C"
elif score >= 60:
  grade = "D"
else:
  grade = "F"
  print(f"final score: {score}, grade: {grade}")
  
#Question 4

num1 = float(input("enter the first number:"))
num2 = float(input("enter the seconf number:"))
operation = input("enter operation (+, - , *, /, %, **):"). strip()

try:
  if operation == "+":
    result = num1 + num2
  elif operation == "-":
    result = num1 - num2
  elif operation == "*":
    result = num1 * num2
  elif operation == "/":
    result = num1 / num2
  elif operation == "%":
    result = num1 % num2
  elif operation == "**":
    result = num1 ** num2
  else:
    result = "invalid operation selected."

    print("result:", result)

except ZeroDivisionError:
  print("error: division or modulus by zero is not allowed.")
  


 





