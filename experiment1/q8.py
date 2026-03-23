import sys

print('size of integer = ', sys.getsizeof(100), "bytes")
print('size of float = ', sys.getsizeof(10.5), "bytes")
print('size of string = ', sys.getsizeof("Hello"), "bytes")
print('size of set = ', sys.getsizeof({1, 2, 3}), "bytes")
print('size of tuple = ', sys.getsizeof((1, 2, 3)), "bytes")
print('size of dictionary = ', sys.getsizeof({"a": 1, "b": 2}), "bytes")
