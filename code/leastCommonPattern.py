
#["flower","flow","flight"]  -->fl
def lcp(l):
    # take 1st one as prefix
    prefix=l[0]
    for index, value in enumerate(l):
        # compare it with rest of the words  to see if thaat word exists as substring if not
        while(value.rfind(prefix,0) !=0 ):
            #then remove last letter and redo lookup # and try again untill u find a prefix
            prefix=prefix[0:len(prefix)-1]
        print(f"prefix= {prefix} ")
    return prefix








if __name__ == '__main__':
    print(lcp(["flower","flow","flight"] ))