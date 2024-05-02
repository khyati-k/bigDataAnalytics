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

# def bubble_sort_count3(arr):
#     n = len(arr)
#     count_n=0
#     for i in range(n):
#         for j in range(0, n-1-i):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#             print(i,j, arr)
#             count_n+=1
#     return count_n

# if __name__ == "__main__":
#   data = [10, 9, 88, 7, 62, 5, 43]
#   print(bubble_sort_count3(data))
import time
from itertools import permutations

# def all_permutations(elements):
#     return list(permutations(elements))

# if __name__ == "__main__":
#   elements=[1,2,3,4,5,6,7,8,9,10,11]  
#   # Start the timer
#   start = time.time()
#   result = all_permutations(elements)
#   # End the timer
#   end = time.time()
  
#   print(f'Total time to run (seconds):',round(end-start,4))

# def count_pass(file_path):
#   # Provide your Python script here
#   count = 0
#   with open("session1/solutions/rockyou.txt", 'r',encoding='ISO-8859-1') as file:
#     for line in file:
#       count += 1
#     return count

# ## Use the following main
# if __name__ == "__main__":
#   print(count_pass('rockyou.txt'))

# def search_password(file_path, target_password):
#   # Provide your solution here
#   start = time.time()
#   with open(file_path, 'r',encoding='ISO-8859-1') as file:
#         for line in file:
#             if ''.join(line.splitlines()) == target_password:
#               end = time.time()
#               print(f'Total time:', round(end- start, 4))
#               return True
#   return False


# if __name__ == "__main__":
#     file_path = input("Enter the path to the password file: ")
#     target_password = input("Enter the password to search for: ")
#     found = search_password(file_path, target_password)
#     if found:
#         print("Password found.")
#     else:
#         print("Password not found.")

#9
# def check_duplicates1(file_path):
#   	# Provide your solution here
#     with open(file_path, 'r', encoding = 'ISO-8859-1') as file:
#         words = []
#         for line in file:
#           if len(words) < 25:
#             words.append(''.join(line.splitlines()))

#         for i in range(len(words)):
#            for j in range(len(words)):
#               if words[i] == words[j]:
#                  return True
              
# if __name__ == "__main__":
#     file_path = "session1/solutions/rockyou.txt"
#     print(check_duplicates1(file_path))

#11
def check_duplicates2(file_path):
  # Provide your solution here
  with open(file_path, 'r', encoding = 'ISO-8859-1') as file:
    words = []
    for line in file:
      if len(words) < 25:
        words.append(''.join(line.splitlines()))

  wordsSet = set()
  for i in range(len(words)):
      for j in range(len(words)):
        if words[i] == words[j]:
            wordsSet.add(words[j])
  print(wordsSet)

if __name__ == "__main__":
  file_path = "session1/solutions/rockyou.txt"
  check_duplicates2(file_path)
          
          
