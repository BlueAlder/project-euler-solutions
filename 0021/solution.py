#!/usr/bin/env python3

# Challenge 21

# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
# Evaluate the sum of all the amicable numbers under 10000.

import math

stored_divisor_sum = {
  1: 0
}

def main():
  UPPER_BOUND = 10000

  amicable_numbers = set()

  for num in range(2, UPPER_BOUND):
    am1 = get_divisor_sum(num)
    am2 = get_divisor_sum(am1)

    if (num == am2 and num != am1):
      amicable_numbers.add(am1)
      amicable_numbers.add(am2)
  
  # print(stored_divisor_sum)
  print(amicable_numbers)
  print(sum(amicable_numbers))

def get_divisor_sum(num):
  if num in stored_divisor_sum:
    return stored_divisor_sum[num]
  
  total = sum(find_devisors(num))
  stored_divisor_sum[num] = total
  return total


def find_devisors(num):
  bound = math.sqrt(num)
  bound = math.ceil(bound) + 1
  
  divisors = set()
  for i in range(1, bound):
    if num % i == 0:
      divisors.add(i)
      if i != 1:
        divisors.add(int(num / i))
  return divisors

if __name__ == "__main__":
  main()

