
def run():
    # return capital indexes
    str="heLlO"
    print(  [i for i, char in enumerate(str) if char.isupper()] )
    # return mid letter
    if len(str) %2==0:
        return ""
    else :
        m= len(str) // 2
        m,str[m]

        # how many online
    statuses = {
        "Alice": "online",
        "Bob": "offline",
        "Eve": "online",
    }
    l=[]
    for k,v in statuses.items():
        if v =="online":
            l.append(k)
    #print(l)
    # double letters - hello -l
    s="hello"
    for i in range(1,len(s)):
        if s[i-1] == s[i]:
            print("double")
            #return True
    n=9
    if n % 3 ==0 :
        print(f" {n} dev by 3 " )
    l=[1,2,3,4]
    j="-".join(l)
    print(j.split("-"))


def palindrome(s):
    #return s==s[::-1]
    l=0
    r=len(s)-1
    res=False
    while l < r :
        if s[l] == s[r]:
            res=True
        else:
            res=False
        print(f" {l} {r} {s[l]} {s[r]}")
        l=l+1
        r=r-1
    return res
def consecutive_zeros(s):
    indexv=s.index('0')
    c=0
    longest=0
    if indexv:
        c=c+1
    for i in range(indexv+1,len(s)-1):
        if s[i] ==s[indexv]:
            c=c+1
        else:
            longest = c
            c = 0
    return c







# add_dots  test t.e.s.t
def add_dots(s):
        return '.'.join(s)
def is_anagram(s1,s2):
    return s1 ==s2[::-1]
def flatten( l1, l2 ):
    #[1,2] [3,4] [1234]
    l1.extend(l2)

def flatten(lst):
    flattened_list = []
    for sublist in lst:
        if isinstance(sublist, list):
            flattened_list.extend(flatten(sublist))
        else:
            flattened_list.append(sublist)
    return flattened_list
def largest_difference(l):
    maxv,minv=l[0],l[0]
    for e in l:
        maxv=max(maxv,e)
        minv=min(minv,e)
    return maxv-minv

if __name__ == '__main__':
    run()
    print(add_dots("test"))
    print(largest_difference([1,5,10,20]))
    print(f" palindrome test {palindrome('abba')}")
    print(f" langet 0  {consecutive_zeros('12000400005')  }" )
