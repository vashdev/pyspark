
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#Open brackets must be closed by the same type of brackets.
#Open brackets must be closed in the correct order.
#Every close bracket has a corresponding open bracket of the same type.
#Input: s = "()[]{}" Input: s = "()[]{}" "{{()}} "


def matchp(s):
    # valids=["(","[","{"]
    # validclose=[")","]","}"]
    # rtn=False
    # for index, c in enumerate(s):
    #     # if its open char then get its index from valid
    #     if c in valids:
    #         ind=valids.index(c)
    #         # get closing paranthesis for that element from validclose
    #         if (  len(s) > index + 1):
    #             if(validclose[ind] == s[index + 1]):
    #                rtn=True
    #             else:
    #               rtn=False

    # since we should do positional test lets do stack  and test whats at top of stack as soon as we see  closing then we pop that of if closing is as expected
    # in end stack should be empty
    myStack = []


    for  c in s :
        if c in ["(","[","{"]:
            myStack.append(c)

        print(f"stack is {myStack} ")
        if c in "]":
            if(myStack.pop() == "["):
                pass

        if c in ")":
           if (myStack.pop() == "("):
             pass
        if c in "}":
            if (myStack.pop() == "{"):
                 pass
    if(myStack ==[]) :
        return True
    else:
        return False










if __name__ == '__main__':
    #print(matchp("(){}[]"))
    #print(matchp("()[{}]"))
    print(matchp("(]"))