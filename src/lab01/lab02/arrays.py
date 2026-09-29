def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if not nums: raise ValueError("Список пуст")
    min_val = max_val = nums[0]

    for num in nums[1:]:
        if num < min_val: min_val = num
        elif num > max_val: max_val = num

    return min_val, max_val
# print(min_max([3, -1, 5, 5, 0])) 
# print(min_max([42]))
# print(min_max([-5, -2, -9]))
# print(min_max([]))
# print(min_max([1.5, 2, 2.0, -3.1]))     


def unique_sorted(nums: list[float | int]) -> list[float | int]:
    return sorted(set(nums))
# print(unique_sorted([3, 1, 2, 1, 3]))       
# print(unique_sorted([]))                
# print(unique_sorted([-1, -1, 0, 2, 2]))   
# print(unique_sorted([1.0, 1, 2.5, 2.5, 0])) 

def flatten(mat: list[list | tuple]) -> list:
    for i in mat:
        if i.__class__ != list and i.__class__ != tuple :
            return 'TypeError:строка/элемент не является списком/кортежем'
    big_list = []
    for stroka in mat:
        for element in stroka:
           big_list.append(element)
    return big_list
# print(flatten([[1, 2], [3, 4]]))       
# print(flatten([[1, 2], (3, 4, 5)]))   
# print(flatten([[1], [], [2, 3]]))    
# print(flatten([[1, 2], "ab"]))   

