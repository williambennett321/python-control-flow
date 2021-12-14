# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a: 
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equalateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle

length_a = int(input("Enter the first length of the triangle: ")) 
length_b = int(input("Enter the second length of the triangle: "))
length_c = int(input("Enter the third length of the triangle: "))

if length_a == length_b and length_a == length_c:
  print(f"A triangle with sides of {length_a}, {length_b}, {length_c} is a equalateral triangle")
if length_a != length_b and length_a != length_c:
  print(f"A triangle with sides of {length_a}, {length_b}, {length_c} is a scalene triangle ")
if length_a == length_b and length_a != length_c:
  print(f"A triangle with sides of {length_a}, {length_b}, {length_c} is a isosceles triangle")
