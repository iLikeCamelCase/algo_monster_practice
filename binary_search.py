from typing import List

def binary_search(target, array) -> int:
    left, right = 0, len(array)-1
    while left <= right:
        mid = left + right // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def find_boundary(arr: List[bool]) -> int:
    left, right = 0, len(arr)-1
    if len(arr) <= 1 or arr[0] == True:
        return 0
    elif arr[len(arr)-1] == False:
        return -1
    elif len(arr) == 2:
        return 1

    while left <= right:
        mid = left + right // 2
        if arr[mid] == True and arr[mid-1] == False:
            return mid
        elif arr[mid] == arr[mid+1] == False:
            left = mid
        else:
            right = mid
    return -1

if __name__ == '__main__':

    array = [False,False,True,True,True]

    print(find_boundary(array))