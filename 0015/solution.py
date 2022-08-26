#!/usr/bin/env python3

# Challenge 15

# Starting in the top left corner of a 2×2 grid, 
# and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

# How many such routes are there through a 20×20 grid?



# How many such routes are there through a 20×20 grid?

# This follows a pascals triangle pattern since each node in the triangle is
# the sum of the previous nodes, so we need to expand this to be a 20 X 20 triangle.

# The below shows the solution for a 2 x 2 rectangle with the top of the triangle being 
# the top left of the square.

###
#            1           n = 0
#          1   1         n = 1
#        1   2   1       n = 2
#      X   3   3   X     n = 3
#    X   X   6   X   X   n = 4
#  X   X   X   X   X   X

# In a grid of k * k squares there are (k + 1) * (k + 1) nodes meaning we need to traverse
# pascals triangle (2k + 1) layers however since the triangle is indexed at 0 our number is
# located on layer n = 2k. 

# Since n is an even number the number of numbers on that layer is odd, the number we are looking for is the middle number
# therefore we are looking for kth number of the 2kth row. To solve this problem.

def main():
  GRID_SIZE = 20
  
  desired_layer = GRID_SIZE * 2
  layer_index = 0
  layer = [1]
  while layer_index < desired_layer:
    layer_index += 1

    new_layer = []
    for i in range(layer_index + 1):
      # Edges of triangle
      if (i == 0 or i == layer_index):
        new_layer.append(1)
      else: 
        new_layer.append(layer[i - 1] + layer[i])
    layer = new_layer
  
  print(layer[GRID_SIZE])



if __name__ == "__main__":
  main()

