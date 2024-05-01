# def linear_search(arr, x):
#     for i in range(len(arr)):
#         if arr[i] == x:
#             return i
#     return -1


# runs only if file is run as script, not as import
# if __name__ == '__main__':
#     data = [1,2,3,4,5,6,7,8]
#     result = linear_search(data,14)
#     print(result)

def bubble_sort_count3(arr):
    n = len(arr)
    count_n=0
    for i in range(n):
        for j in range(0, n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            print(i,j, arr)
            count_n+=1
    return count_n

if __name__ == "__main__":
  data = [10, 9, 88, 7, 62, 5, 43]
  print(bubble_sort_count3(data))