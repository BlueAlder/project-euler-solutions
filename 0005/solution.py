#!/usr/bin/env python3

# 2520 is the smallest number that can be divided by each of the numbers
# from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all
# of the numbers from 1 to 20?

# very slow solution but it works
def main():
  divisible_bound = 20

  current_num = 1
  while True:
    if multiplesUpTo(current_num, divisible_bound):
      break
    current_num += 1
  print(current_num)


def multiplesUpTo(number, multiplesUpperBound):
  for i in range(1, multiplesUpperBound + 1):
      if number % i != 0:
        return False
  return True


if __name__ == '__main__':
  main()
