#Task 1
def fun():
    a = 1
    str = 'GeeksForGeeks'


def num_locals(fun):
    return fun.__code__.co_nlocals

print('Task 1:', num_locals(fun))

#Task 2
#Write a Python program to access a function inside a function (Tips: use function, which returns another function)'''

def func2(a, b):
    return a +b

def func3():
    return func2

print('Task 2: ', func3()(3,4))

#Task3

nums1 = [1, 2, 3, 4, 5]
nums2 = [1, -2, 3, -4, 5]


def square_nums(nums):
    return [num ** 2 for num in nums]


def remove_negatives(nums):
    return [num for num in nums if num > 0]


def choose_func(nums: list, func1=square_nums, func2=remove_negatives):
    count = True
    for num in nums:
        if num < 0:
            count = False
    if count:
        return func1(nums)
    else:
        return func2(nums)


assert choose_func(nums1, square_nums, remove_negatives) == [1, 4, 9, 16, 25]
assert choose_func(nums2, square_nums, remove_negatives) == [1, 3, 5]