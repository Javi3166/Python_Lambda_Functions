# Lambda functions: a small one-line anonymous function that defined without a name.
# format is: lambda arguments: expressions

print("\nThe format for doing a lambda function is typing \"lambda\" then following up with the arguments that will be "
      "passed to it, a colon(:), \nthen the one-line expression of the function to be evaluated.")
add10 = lambda x: x + 10
print(add10(5))

print("\nIt is possible to use multiple arguments with a lambda function.")
mult = lambda x,y: x * y
print(mult(2,7))

print("\nLambda functions are typically used when you need a simple function that is only used once in the code.\nOr it is "
      "used as an argument to higher order functions, meaning functions that take in other functions as arguments, "
      "such as sorted, map, filter, and reduce.")

print("\nIt is possible to use a lambda function as a key for the sorted function to change how it sorts.")
print("\nOriginal sorted:")
points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
points2D_sorted = sorted(points2D)
print(points2D)
print(points2D_sorted)

print("\nModified sorted:")
points2D_sorted = sorted(points2D, key=lambda x: x[1])
print(points2D)
print(points2D_sorted)

print("\nIt is possible to also sort in whatever manner is possible in one line including based on the addition of the "
      "elements in the tuple.")
points2D_sorted = sorted(points2D, key=lambda x: x[0] + x[1])
print(points2D)
print(points2D_sorted)

print("\nA map function transforms each element with a function. It has the format of map(function, sequence like a list).")
a = [1, 2, 3, 4, 5]
b = map(lambda x: x * 2, a)
print(b)
print(list(b))

print("\nIn this specific case, a list comprehension might be easier.")
c = [x * 2 for x in a]
print(c)

print("\nFilter function filters out the elements in a sequence that results in a TRUE in the specified function. "
      "\nThe syntax is filter(func, seq).")
a = [1, 2, 3, 4, 5, 6]
b = filter(lambda x: x % 2 == 0, a)
print(list(b))

print("\nList comprehension can also accomplish this case.")
c = [x for x in a if x % 2 == 0]
print(c)

print("\nReduce repeatedly applies the function until there is 1 value to return."
      "\nThe syntax is reduce(func, seq).")
from functools import reduce
b = reduce(lambda x, y: x * y, a)
print(b)