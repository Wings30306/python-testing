def even_number_of_evens(numbers):
    if isinstance(numbers, list):
        evens = sum([1 for num in numbers if num % 2 == 0])
        return evens and evens % 2 == 0
    else:
        raise TypeError("A list was not passed into the function")


if __name__ == '__main__':
    print(even_number_of_evens([1, 2, 4]))
