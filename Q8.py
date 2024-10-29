def bubble_sort(array):
  length = len(array)
  first_index = 0
  last_index = length - 1
  while first_index < last_index:
    for index in range(first_index, last_index):
      value1 = array[index]
      value2 = array[index + 1]
      if value1 > value2:
        array[index], array[index + 1] = value2, value1
    last_index -= 1

    for index in range(last_index, first_index, -1):
      value1 = array[index]
      value2 = array[index - 1]
      if value1 < value2:
        array[index], array[index - 1] = value2, value1
    first_index += 1

numbers = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
bubble_sort(numbers)
print(numbers)