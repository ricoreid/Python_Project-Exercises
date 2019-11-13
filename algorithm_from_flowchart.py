from random import shuffle
from random import random

array_list = int(random() * 50 + 1)
numbers = list(range(array_list))
shuffle(numbers)


def swap_function(a, b):
    global numbers
    temp = numbers[a]
    numbers[a] = numbers[b]
    numbers[b] = temp


def sort_numbers():
    global numbers
    N = len(numbers)
    iteration = 1

    print("Array values: ", numbers)

    while iteration < N:
        j = 0

        while j <= (N - 2):
            if numbers[j] > numbers[j+1]:
                swap_function(j, j+1)
            else:
                j = j + 1

        iteration = iteration + 1


print("Initial array: ", numbers)
sort_numbers()
print("Sorted array: ", numbers)
