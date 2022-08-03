#!/usr/bin/env python3

# Challenge 6

# Find the difference between the sum of the squares of the first one hundred
# natural numbers and the square of the sum.



def main():
  upper_bound = 100
  solution = squareOfSum(upper_bound) - sumOfSquares(upper_bound)
  print(solution)


def sumOfSquares(max):
  sum = 0

  for i in range(1, max + 1):
    sum += i * i
  return sum

def squareOfSum(max):
  sum = 0
  for i in range(1, max + 1):
    sum += i
  return sum * sum


if __name__ == "__main__":
  main()

