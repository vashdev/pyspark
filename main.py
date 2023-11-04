# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import collections
from functools import reduce
from itertools import groupby, accumulate

def addElements(alist):
    return list(accumulate(alist))

def findele(alist):
    print('itertoos magic')
    grouped_l=[[k, len(list(v))] for k, v in groupby(l)]
    store={}
    for item in grouped_l:
        if item[0] in store:
            store.update({item[0]:max(item[1],store.get(item[0]))})
        else:
            store.update({item[0]:item[1]})
            #get max value
            vals= store.values()
    return max(vals)




def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1);


def fib(n):
    if n < 0:
        return 'error'
    elif n < 2:
        return 1
    return fib(n - 1) + fib(n - 2)


def isPalindrome(string):
    # get iterators for fwd and backward traversal
    left, right = 0, len(string) - 1
    while right >= left:
        if not string[left] == string[right]:
            return False
        left += 1;
        right -= 1
        return True


def print_hi(name):
    # remove vowels
    s = "leetcodeisacommunityforcoders"
    _rtn = ""
    for x in s:
        if x not in ['a', 'e', 'i', 'o', 'u']:
            _rtn = _rtn + x;
    print(_rtn)
    nums = [1, 2, 3, 4]
    # [1,3,6,10] [1, 1+2, 1+2+3, 1+2+3+4].
    for i in range(1, len(nums)):
        nums[i] += nums[i - 1]
    # return long string form list with saperator
    l = [1, 2, 3]
    print('long string from list' + ','.join(map(str, l)))
    # use of underscore
    # if thers no use of i in for loop then just drop for then drop it and use _
    for _ in range(3):
        print('no i')
    # flip k,v to v,k  reverse
    teacher_subject = {'Ben': 'English', 'Maria': 'Math', 'Steve': 'Science'}
    subject_teacher = {y: x for x, y in teacher_subject.items()}

    # collections.Counter
    # This is useful when you want to count how many numbers of all elements in a list.
    arr_list = [1, 1, 1, 1, 2, 2, 2, 3, 3, 5, 5, 5, 7]
    c = collections.Counter(arr_list)
    print(c)
    print(type(c))
    print(c[1], c[6])
    # Creating an empty dictionary
    freq = {}
    for items in arr_list:
        freq[items] = arr_list.count(items)

    for key, value in freq.items():
        print("% d : % d" % (key, value))

    # Decorators -function
    def devide(first, second):
        print("The result is:", first / second)

    # decorator
    def swipe_decorator(func):
        def swipe(first, second):
            if first < second:
                first, second = second, first
            return func(first, second)

        return swipe

    devide = swipe_decorator(devide)
    devide(4, 16)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    print(factorial(3))
    print(fib(10))
    print(isPalindrome('racecar'))
    print(
        '__init__.py. is used as constructor in class and to identify individual dirs as packages ...then you import import Game.Sound.load as loadgame')
    l = [1, 5, 3, 3, 3, 2,1,1,1,1,1]  # 2

    print('find most recurring :successive '+str(findele(l)))
    print('add elements successive '+str( addElements(l)))
    print(' ')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
#Define a function named all_equal that takes a list and checks whether all elements in the list are the same.

#For example, calling all_equal([1, 1, 1]) should return True.


def all_equal(l):
    if len(l) == 0:
        return True

    return len(l) - len(set(l)) == len(l) - 1

print(reduce(lambda x, y : x + y,[1,2,3]),-3)
values=[34,6565,67,8]
for count, value in enumerate(values):
    print(count, value)