import math
import os
import random
import re
import sys

# Complete the 'reverseArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY a as parameter.


def reverseArray(a):
    return a[::-1]

if __name__ == '__main__':
    arr_count = int(input("Enter number of elements: ").strip()) 
    arr = list(map(int, input("Enter space-separated integers: ").rstrip().split()))  
    res = reverseArray(arr)
    print("Reversed array:", ' '.join(map(str, res)))