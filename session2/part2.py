def linearSearch(arr, search):
   for element in arr:
       if element == search:
           return True
   return False

def search_key_index(arr, search):
    count = 0
    found = -1
    for element in arr:
       if element == search:
           found = count
           break
       count += 1
    return found

# import pprint

def freq(arr):
    freq = {}
    for element in arr:
        freq[element] = 0
    for element in arr:
        freq[element] += 1
    return freq

if __name__ == '__main__':

    import pprint

    alist = [-10,-5,0, 0, 0,4,9]
    # print(search_key_index(alist,0))
    # print(search_key_index(alist,114))
    pprint.pprint(freq(alist))