__author__ = 'VData'

from Omega import *

'''install pyQt Module'''
class Extracting(Omega):
    def __init__(self):

        Omega.__init__(self)
        self.key = ""
        self.SecretMsg = ""
        self.FinalSecretMsg = ""
        self.KeyErroCheck = 0
        self.SecretMsgSplit = ""
    def Extract_Key(self, SecretMsg):
        self.SecretMsgSplit = SecretMsg.split(" ")
        CheckSum = 0
        counter = 0
        while counter <= len(self.SecretMsgSplit)-2:
           if self.SecretMsgSplit[counter] == '':
               self.key += "1"
               CheckSum += 1
           elif self.SecretMsgSplit[counter] != '' and self.SecretMsgSplit[counter+1] != '':
               self.key += "0"
           counter += 1
        print "KEy Val: "+self.key

        if CheckSum == int(self.SecretMsgSplit[-1]):
            print "No Error"
        else:
            print "The Transmitted/Memorized Message Has Been Modidiyed, Please Resend it Again..."
        return self.key
    def Extract_Secret_Chars(self):
        SecChars = ""
        Key_Array_Counter = 0
        Key_Array = ""
        Cover_Characters_Array = []
        #10 digits for each secret character,,,
        #the First one for the case, the next 4 digits are for the first cover cover character,,
        #the next 4 digits are for the second cover character,..
        #the final digits to determine if it's at the end of the secret word.
        counter = 0
        ListCounter = 0
        KeySplit = []
        print(self.chars)
        while counter < len(self.key):
                KeySplit.insert(ListCounter, self.key[counter:counter+12])
                ListCounter += 1
                counter += 12

        KeyCounter = 0
        ItemCounter = 0
        print(len(self.SecretMsgSplit))
        while KeyCounter <= len(KeySplit)-1:
            print "KeyCounter = "+ str(KeyCounter)
            print "ItemCounter = " + str(ItemCounter)
            item = self.SecretMsgSplit[ItemCounter]
            KeyItem  = KeySplit[KeyCounter]
            print(item + "\n \n")

            if item not in self.chars and item != '' and len(item) == 1:

                self.FinalSecretMsg += item
                ItemCounter += 1

            elif item == '':

                ItemCounter += 1

            else:
                print "Item: " + item

                KeyCounter += 1
                ItemCounter += 1
                self.First_Cover_Char = item[int(str(KeyItem[3:7]), 2)]
                self.Second_Cover_Char = item[int(str(KeyItem[7:11]), 2)]


                if KeyItem[0] == '1':
                    self.First_Cover_Char = self.chars[int((self.ToBinStr_5(self.chars.index(self.First_Cover_Char))[:-1] + "0"), 2)]
                else: pass

                if KeyItem[1] == '1':
                    self.Second_Cover_Char = self.chars[int((self.ToBinStr_5(self.chars.index(self.Second_Cover_Char))[:-1] + "0"), 2)]
                else: pass
                print "First Char: " +  self.First_Cover_Char + "   " + "Second Char: " + self.Second_Cover_Char

                self.Sec_Char = self.FindSecChar(self.First_Cover_Char, self.Second_Cover_Char)

                print "Sec Char: " + self.Sec_Char

                if KeyItem[2] == '1':
                    self.Sec_Char = self.Sec_Char.upper()

                self.FinalSecretMsg += self.Sec_Char #To Generate the Secret Msg

                if KeyItem[-1] == '1':
                    self.FinalSecretMsg += " "

        print "$$$$$$$$$$$$"
        print (self.FinalSecretMsg)
        return self.FinalSecretMsg
       # return self.FinalSecretMsg
    def ExtractSecMsg(self, CoverMsg):
        self.Extract_Key(CoverMsg)
        SecMsg = self.Extract_Secret_Chars()
        return SecMsg
       # return self.FinalSecretMsg
