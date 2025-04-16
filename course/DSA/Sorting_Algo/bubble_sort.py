def bubble_sort(arr):
  n = len(arr)
  flag = True
  while flag:
    flag = False
    for i in range(1, n):
      if arr[i-1] > arr[i]:
        flag = True
        arr[i-1], arr[i] = arr[i], arr[i-1]


if __name__ == "__main__":
  arr = [-5, 3, 2, 1, -3, -3, 7, 2, 2]
  bubble_sort(arr)
  print(arr
