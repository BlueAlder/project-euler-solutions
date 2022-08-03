#!/usr/bin/env python3

import math

# Challenge 10

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

def main():
  upper_bound = 2000000

  primes = set()
  i = 2
  while True:
    if isPrime(i):
      primes.add(i)
    i += 1
    if i >= upper_bound:
      break
  print(sum(primes))


def isPrime(number):
  if number % 2 == 0 and number != 2:
    return False

  upper_bound = math.sqrt(number)
  upper_bound = math.ceil(upper_bound) + 1
  for i in range(3, upper_bound, 2):
    if number % i == 0:
      return False
  return True

if __name__ == "__main__":
  main()

