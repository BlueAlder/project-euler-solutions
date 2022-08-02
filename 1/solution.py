#!/usr/bin/env python3

# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

def main():
  multiples = set()
  upper_bound = 1000

  # Find Multiples of 3
  for i in range(0, upper_bound, 3):
    multiples.add(i)

  # Find Multiples of 5
  for i in range(0, upper_bound, 5):
    multiples.add(i)

  sum = 0
  for num in multiples:
    sum += num
  print(sum)


if __name__ == '__main__':
  main()
