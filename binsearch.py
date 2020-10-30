
l = [] 

def insert_num(element):

    mid = len(l) // 2
    low = 0
    high = len(l) - 1

    while len(l) > 0 and l[mid] != element and low <= high:
        if element > l[mid]:
            low = mid + 1 
        else:
            high = mid - 1
        mid = (low + high) // 2
    l.insert(low, element)

    return l


def num_from_list(nums):
    while len(nums) != 0:
        yield nums.pop()
        
n = num_from_list([3, 1, 8, 4, -1, 11, 6])

for num in n:
    insert_num(num)

    print(l)
 
 


