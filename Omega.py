__author__ = 'vdata'

import numpy


class Omega:
    def __init__(self):

        self.chars = [ #Input Nodes
            'a', 'b', '?', 'c', 'd', 'e', '.','f', 'g', 'h', 'i', 'j', '\'', 'k', 'l', 'm',
            'n', 'o', ',', 'p', 'q', 'r', '!','s', 't', 'v', 'u', 'w', 'x', 'y', ' ', 'z',
                          #Changed
        ]  # List of characters are represent the omega network nodes, each 2 adjacent characters are one node
        # the first one is the upper value and the second character is the bottom value of the node.

    def R_shifting(self, value):
        return value[-1] + value[:-1]

    def L_shifting(self, value):
        return value[1:] + value[0]

    def ToBinStr_5(self, number):
        return '{0:05b}'.format(int(number))

    def ToBinStr_4(self, number):
        return '{0:04b}'.format(int(number))

    def logical_xor(self, InputStage, OutputStage):
        XOR = ''
        for i in range(len(InputStage)):
            if InputStage[i] == OutputStage[i]:
                XOR += '0'
            else:
                XOR += '1'
        return XOR

    def FindCoverChars(self, SecChar):

        SecChar = SecChar.lower()

        InputStageCharPos = OutputStageCharPos = self.chars.index(SecChar)
        BinInputStageCharPos = self.ToBinStr_5(InputStageCharPos)
        BinOutputStageCharPos = self.ToBinStr_5(OutputStageCharPos)

        print("Bin Input: " + BinOutputStageCharPos + "  " + "Bin Output: " + BinOutputStageCharPos + "\n")
        print("To Omega Network. \n")
        BinInputStageCharPos = self.R_shifting(BinInputStageCharPos)
        for StageCounter in range(2):
           BinInputStageCharPos = self.R_shifting(BinInputStageCharPos)
           BinOutputStageCharPos = self.L_shifting(BinOutputStageCharPos)

           #BinInputStageCharPos = BinInputStageCharPos[:-1] + str(numpy.random.randint(0, 2))
           #BinOutputStageCharPos = BinOutputStageCharPos[:-1] + str(numpy.random.randint(0, 2))  #randomizing the Least significant bit for Both Input stage and output stage


           print("Bin Input: " + BinInputStageCharPos + "  " + "Bin Output: " + BinOutputStageCharPos + "\n")
        #BinInputStageCharPos = BinInputStageCharPos[:-1] + str(numpy.random.randint(0, 2))
        if(self.chars[int(BinOutputStageCharPos[:-1] + "1", 2)].isalpha() == True and self.chars[int(BinOutputStageCharPos[:-1] + "0", 2)].isalpha() == True):  #if both of the node values are alphabetical characters, choose randomly

                 BinOutputStageCharPos = BinOutputStageCharPos[:-1] + str(numpy.random.randint(0, 2))

        elif(self.chars[int(BinOutputStageCharPos[:-1] + "0", 2)].isalpha() == False): #if the first value of the node is a non-alphabetical characters, choose the second one.

                 BinOutputStageCharPos = BinOutputStageCharPos[:-1] + "1"

        elif(self.chars[int(BinOutputStageCharPos[:-1] + "1", 2)].isalpha() == False): #if the second value of the node is a non-alphabetical characters, choose the first one.

                 BinOutputStageCharPos = BinOutputStageCharPos[:-1] + "0"

        print("Bin Input: " + BinInputStageCharPos + "  " + "Bin Output: " + BinOutputStageCharPos + "\n")
        InputStageChar = self.chars[int(BinInputStageCharPos, 2)]
        OutputStageChar = self.chars[int(BinOutputStageCharPos, 2)]  # Find the 2 covering characters by return new 2 chars based on the new

        return InputStageChar, OutputStageChar

    def FindSecChar(self, InputStageChar, OutputStageChar):
        print("Extracting: \n")
        BinInputStageChar = self.ToBinStr_5(self.chars.index(InputStageChar))
        BinOutputStageChar = self.ToBinStr_5(self.chars.index(OutputStageChar))
        RoutingStr = self.logical_xor(BinInputStageChar,
                                      BinOutputStageChar)
        print("Bin Input: " + BinInputStageChar + "  " + "Bin Output: " + BinOutputStageChar + "\n")

        # BinOutputStageChar = self.L_shifting(BinOutputStageChar)

        for StageCounter in range(3):
            #StageCounter += 3
            print("Bin Input: " + BinInputStageChar + "  " + "Bin Output: " + BinOutputStageChar + "\n")
            BinInputStageChar = self.L_shifting(BinInputStageChar)
            BinInputStageChar = BinInputStageChar[:-1] + BinOutputStageChar[StageCounter]
            print("Bin Input: " + BinInputStageChar + "  " + "Bin Output: " + BinOutputStageChar + "\n")
            print("-------------------- \n")
        return self.chars[int(BinInputStageChar, 2)]





