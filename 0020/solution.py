#!/usr/bin/env python3

# Challenge 20
# Find the sum of the digits in the number 100!

import math

def main():
  val = math.factorial(100)
  str_num = str(val)

  total = 0
  for digit in str_num:
    total += int(digit)
  
  print(total)

if __name__ == "__main__":
  main()

