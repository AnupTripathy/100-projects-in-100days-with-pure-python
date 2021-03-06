# BMI Calculator
# The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):
# Warning you should convert the result to a whole number.
#
# Example Input
# weight = 80
# height = 1.75
# Example Output
# 80 รท (1.75 x 1.75) = 26.122448979591837
#
# 26
# e.g. When you hit run, this is what should happen:
#
# https://cdn.fs.teachablecdn.com/wmjVjddeSmGj0QVtOUrE
#
# Hint
# Check the data type of the inputs.
# Try to use the exponent operator in your code.
# Remember BODMAS.
# Remember to convert your result to a whole number (int).
# Test Your Code
# Before checking the solution, try copy-pasting your code into this repl:


# ๐จ Don't change the code below ๐
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# ๐จ Don't change the code above ๐

#Write your code below this line ๐

bmi = int(weight) / (float(height) * float(height))
print(bmi)