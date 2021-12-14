# exercise-05 Fibonacci sequence for first 50 terms

# Write the code that:
# 1. Calculates and prints the first 50 terms of the fibonacci sequence.
# 2. Print each term and number as follows:
#      term: 0 / number: 0
#      term: 1 / number: 1
#      term: 2 / number: 1
#      term: 3 / number: 2
#      term: 4 / number: 3
#      term: 5 / number: 5
#      etc.

# Hint: The next number is found by adding the two numbers before it

def fibo(n):
  first_num = 0
  second_num = 1

  print(first_num)
  print(second_num)

  for num in range(2,n):
    third_num = first_num + second_num
    first_num = second_num
    second_num = third_num
    print(third_num)

fibo(50)
