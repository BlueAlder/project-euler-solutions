#!/usr/bin/env python3

# Challenge 16

# 215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

# What is the sum of the digits of the number 21000?

def main():
  num = pow(2, 1000)

  str_rep = str(num)
  total = 0
  for digit in str_rep:
    total += int(digit)
  
  print(total)


if __name__ == "__main__":
  main()

