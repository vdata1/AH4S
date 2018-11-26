__author__ = 'vdata'
from Omega import *
import time

class Embedding(Omega):
    def __init__(self):
        Omega.__init__(self)
        self.Key = ""
        self.Covermssg = ""
        self.FinalCover = ""

    def GenCoverMsg(self, SecretMsg):
        FirstChar = SecondChar = ""
        DictFile = open("Dict.txt",'r') #Open File Contains English words.
        OutPut = open("Output","w")
        counter = 0
        for counter in range(len(SecretMsg)):
            print(SecretMsg[counter]+"\n")
            if SecretMsg[counter] not in self.chars and SecretMsg[counter].isalpha() == False:

                self.Covermssg += SecretMsg[counter] + " "
            else:
                FirstChar, SecondChar = self.FindCoverChars(SecretMsg[counter].lower())
                print (FirstChar + "     " + SecondChar)

                if FirstChar.isalpha() is False:

                    FirstChar = self.chars[int((self.ToBinStr_5(self.chars.index(FirstChar))[:-1] + "1"), 2)]
                    self.Key += "1"
                    print("Correcting first Char: " + FirstChar + "    " + SecondChar)

                else:
                    self.Key += "0"

                if SecondChar.isalpha() is False:
                    SecondChar = self.chars[int((self.ToBinStr_5(self.chars.index(SecondChar))[:-1] + "1"), 2)]
                    self.Key += "1"
                    print("Correcting Second Char: " + FirstChar + "    " + SecondChar)

                else:
                    self.Key += "0"

                if(SecretMsg[counter].isupper() == True):
                    self.Key += "1"
                else:
                    self.Key += "0"
                for word in DictFile:
                        if FirstChar.lower() in word and SecondChar.lower()in word and len(word)<=15:
                            self.ind = self.ToBinStr_4(word.index(FirstChar.lower()))
                            self.Key = self.Key + self.ind
                            self.Covermssg +=word[:-1] +' ' # ''.join([self.Covermssg ,' ',word])
                            self.ind = self.ToBinStr_4(word.index(SecondChar.lower()))
                            self.Key = self.Key + self.ind
                            print (word[-1])
                            break
                if(counter != len(SecretMsg) - 1 and SecretMsg[counter+1] == " "): #End Of the Secret word...
                    self.Key += "1"
                elif(counter != len(SecretMsg) - 1 and SecretMsg[counter+1] != " "):
                    self.Key += "0"

                OutPut.write(self.Covermssg)
        self.Key += "1"
        print("Cover Mssg: " + self.Covermssg + "\n")
        print("Key: " + self.Key + "\n")
    def Hide_Key(self): #White-Space Steganography

        counter = 0
        ChCounter = 0
        #Dict = open("Dict.txt")
        while True:
            if counter == len(self.Key):
                break
            elif ChCounter == len(self.Covermssg)-1:
                self.Covermssg+=self.Covermssg
                '''
                counter = 0
                Cover = ""
                for line in Dict:
                    if counter <= len(self.Covermssg):
                        Cover+= line[-1]
                        break
                    counter+=1
                self.Covermssg+=Cover
                '''
            else:
                if self.Key[counter] == '1' and self.Covermssg[ChCounter] == ' ':
                         self.FinalCover += self.Covermssg[ChCounter]+' '
                         counter += 1
                         ChCounter += 1
                elif self.Key[counter] == '0' and self.Covermssg[ChCounter] == ' ':
                        self.FinalCover += self.Covermssg[ChCounter]
                        counter += 1
                        ChCounter += 1
                else:
                    self.FinalCover += self.Covermssg[ChCounter]
                    ChCounter += 1
        print (self.FinalCover)
        #return self.FinalCover
    def Embed(self, SecretMsg):
        Timer = time.time()
        self.GenCoverMsg(SecretMsg)
        self.Hide_Key()
        self.KeyErrorControl()
        OutPut = open("Output","a")
        OutPut.writelines(self.FinalCover)

        print "Timer : "+ str(time.time() - Timer )
        return self.FinalCover

    def KeyErrorControl(self):
        KeySum  = 0
        for digit in self.Key:
            if digit == "1":
                KeySum += 1
        self.FinalCover += str(KeySum)
        print("One's Counter :" + str(KeySum))

#Bug Descovered, in case of the twin_secret characters are not in chars, the output will be ignored,,,,
#in case of end of world too ;
#review gen_covermsg method;!!
#####Done ,
####### Embedding Process Is DONE,,,





#We Need more 2 Flags, The first one is for the omega node postion for the first char,
# the second one is for the omega node possition for the second one, maybe will fix the problem
