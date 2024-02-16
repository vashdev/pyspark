class Solution:
    def countLetters(self, s: str) -> int:

            lseq=""
            seq=""
            for i in range(1, len(s)):
                if s[i] == s[i - 1]:
                    seq+=s[i]
                else:
                    print(s[i] ,s[i - 1],len(lseq) ,len(seq))
                    if len(lseq) < len(seq):
                        lseq=seq
                        seq=""
            if lseq =="":
                lseq=seq


            return lseq,len(lseq)





if __name__ == '__main__':
    print(' ')
    s=Solution()
    print(s.countLetters('yyyyyaaaaaaaaaacc'))
    #print(s.countLetters('aaaaaaaa'))

        



        