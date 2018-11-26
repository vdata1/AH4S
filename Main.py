__author__ = 'vdata'

from Extracting import  *
from Embedding import  *
from Omega import  *
import time

def Main():


    chars = [
                 'a', 'b', ',', 'c', 'd', 'e', '!', 'f',
                 'g', 'h', 'i', 'j', '/', 'k', 'l', 'm',
                 'n', 'o', 'p', 'q', 'r', 's', '.', 't',
                 'u', '$', 'v', 'w', 'x', 'y', 'z', '?'
            ]

    omega = Omega()
    counter = 0
    i = 0
    SecChar = SecChar1 = ""
    EM = Embedding()
    SecretMssg = raw_input("Please Enter Your Secret Message: ")
    print("Message Length: "+ str(len(SecretMssg)))

    #EM.GenCoverMsg(SecretMssg)


    FinalCover = EM.Embed(SecretMssg)
    print "--------------------------- "
    print FinalCover
    print "Extracting Process: "
    CoverMsg = raw_input("Please Enter The Cover MSG: ")
    EX = Extracting()
    timer = time.time()
    EX.Extract_Key(CoverMsg)
    print "Timer : " + str(time.time() - timer)
    EX.Extract_Secret_Chars()


''' for i in range(len(chars)):
            SecChar = chars[i]

            print(SecChar + "\n")

            char1, char2  = omega.FindCoverChars(SecChar)

            print("Char1: " + char1 + "   " + "Char2: " + char2 + "\n")

            SecChar1 = omega.FindSecChar(char1, char2)
            print("Original Char: " + SecChar1)
            if SecChar == SecChar1:
                counter += 1
    print("Counter " + str(counter))
'''

if __name__ == "__main__":
    Main()