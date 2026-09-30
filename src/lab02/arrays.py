#/////////////////////////////MIN_MAX///////////////////////////////////////////
def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:

#    if not nums:
#        raise ValueError("список пуст")

    min_val = max_val = nums[0]

    for num in nums[1:]:
        if num < min_val:
            min_val = num
        elif num > max_val:
            max_val = num

    return min_val, max_val
print("min_max")
print(f"[3, -1, 5, 5, 0]→{min_max([3,-1,5,5,0])}")
print(f"[42]→{min_max([42])}")
print(f"[-5, -2, -9]→{min_max([-5, -2, -9])}")
try:
    print(f"[]→{min_max([])}")
except ValueError:
    print("[]→ValueError:список пуст")
print(f"[1.5, 2, 2.0, -3.1]→{min_max([1.5, 2, 2.0, -3.1])}")

#/////////////////////////////UNIQUE_SORTED///////////////////////////////////////////

def unique_sorted(nums: list[float | int]) -> list[float | int]:
    return sorted(set(nums))

print("unique_sorted")
print(f"[3, 1, 2, 1, 3]→{unique_sorted([3, 1, 2, 1, 3])}")
print(f"[]→{unique_sorted([])}")
print(f"[-1, -1, 0, 2, 2]→{unique_sorted([-1, -1, 0, 2, 2])}")
print(f"[1.0, 1, 2.5, 2.5, 0]→{unique_sorted([1.0, 1, 2.5, 2.5, 0])}")



#////////////////////////////FLATTEN///////////////////////////////////////////

def flatten(mat: list[list | tuple]) -> list:
    for i in mat:
        if i.__class__ != list and i.__class__ != tuple :
            #raise ValueError("TypeError:строка/элемент не является списком/кортежем")
            return 'TypeError:строка/элемент не является списком/кортежем'
    big_list = []
    for stroka in mat:
        for element in stroka:
           big_list.append(element)
    return big_list

print("flatten")
print(f"[[1, 2], [3, 4]]→{flatten([[1, 2],[3,4]])}")
print(f"[[1, 2], (3, 4, 5)] →{flatten([[1, 2], (3, 4, 5)] )}")
print(f"[[1], [], [2, 3]]→{flatten([[1], [], [2, 3]])}")
print(f'[[1, 2], "ab"]→{flatten([[1, 2], "ab"])}')