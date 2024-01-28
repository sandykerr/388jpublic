def hello_world():
   return 'Hello, World!'

def sum_unique(l):
    unique = list(set(l))
    sum = 0
    for i in unique: 
        sum += i
    return sum

def palindrome(x):
    x = str(x)
    if(x == x[::-1]): return True
    return False       

#error on for loop :P
def sum_multiples(num):
    sum = 0
    for i in range(0..num-1):
        if i % 3 == 0 or i % 5 == 0: sum += i
    return sum

#erroring weirdly
def num_func_mapper(nums, funs):
    return [f(nums) for f in funs]

def height_sort(names, heights):
    heights, names = (list(i) for i in zip(*sorted(zip(heights, names)))) #create list of tuples, sort by height, return list of heights
    return names[::-1]
 
def custom_sort(lst):
    return sorted(lst, key=lambda i: (1 - (i & 1), i))
