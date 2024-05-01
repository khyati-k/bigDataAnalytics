def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1


# runs only if file is run as script, not as import
if __name__ == '__main__':
    data = [1,2,3,4,5,6,7,8]
    result = linear_search(data,14)
    print(result)

