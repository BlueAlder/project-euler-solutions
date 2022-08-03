#!/usr/bin/env python3

import math

# Challenge 7

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
# that the 6th prime is 13.

# What is the 10 001st prime number?

def main():
  prime_index = 10001
  # prime_index = 6
  primes_found = 0

  num_to_check = 2
  while True:
    if isPrime(num_to_check):
      primes_found += 1
      if primes_found == prime_index:
        break
    # Adding 2 here because no prime is even
    num_to_check += 1

  print(num_to_check)


def isPrime(number):
  upper_bound = math.sqrt(number)
  upper_bound = math.ceil(number)

  if number == 2:
    return True

  for i in range(2, upper_bound):
    if number % i == 0:
      return False

  return True

if __name__ == "__main__":
  main()

