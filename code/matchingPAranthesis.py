
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#Open brackets must be closed by the same type of brackets.
#Open brackets must be closed in the correct order.
#Every close bracket has a corresponding open bracket of the same type.
#Input: s = "()[]{}" Input: s = "()[]{}" "{{()}} "


def matchp(s):
    myStack = []
    resp=False
    pairs = {
        '(': ')',
        '{': '}',
        '[': ']'
    }

    for  c in s :
        if c in ["(","[","{"]:
            myStack.append(c)
        elif len(myStack) == 0 or c != pairs[myStack.pop()]:
               return False

    return len(myStack) == 0

















if __name__ == '__main__':
    #print(matchp("(){}[]"))
    #print(matchp("()[{}]"))
    print(matchp("( [ ) ]"))