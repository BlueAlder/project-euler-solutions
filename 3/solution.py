#!/usr/bin/env python3

import math

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

def main():
  number_to_factor = 600851475143

  # Naive approach, cause sack
  # Only need to search for sqrt(n) factors
  # Anything higher will just find compliment factors
  # If we find only 1 and n, then number is a prime
  # might try out some recursion

  values = findPrimeFactors(number_to_factor)

  print(max(values))


def findPrimeFactors(number):
  upper_bound = math.sqrt(number)
  upper_bound = math.ceil(upper_bound)

  primeFactors = set()
  for i in range (1, upper_bound):
    if number % i == 0:
      # We have found a factor
      if i == 1:
        primeFactors.add(i)
        continue


      subPrimes = findPrimeFactors(i)
      if len(subPrimes) == 1:
        primeFactors.add(i)

      compliment_i = int(number / i)
      subPrimes = findPrimeFactors(compliment_i)
      if len(subPrimes) == 1:
        primeFactors.add(compliment_i)

  return primeFactors


if __name__ == '__main__':
  main()
