
def binary_search(arr, low, high, num):
    if high < low:
        return -1

    mid = (high+low) // 2
    if arr[mid] == num:
        return mid
    elif arr[mid] > num:
        return binary_search(arr, low, mid-1, num)
    else:
        return binary_search(arr, mid+1, high, num)



arr = input("Input your array: ")
arr = list(arr.replace(' ', ''))
arr = [int(element) for element in arr]

num = input("Input your number: ")
num = int(num.strip())

result = binary_search(arr, 0, len(arr) - 1, num)
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")


"""
compara(string1, string2)
    return 0 egale
    return -1 daca string 1 > string2
    return 1 altfel

def func1():
    return 1
"""
#def = definitie"""
"""
def func2():
    val = func1()
    if val == 1:
        return "ceva"

    elif val == 9:
        return 1
"""