___author__ = 'Jason Maderski'
__date__ = '11/15/2015'

import re

inputFile1List = []
inputFile2List = []

inputFile1 = "inputFile1.txt"
inputFile2 = "inputFile2.txt"

class FindDuplicates:

    duplicatesCounted = 0

    # Check to see if inputed item is on inputed List
    def isItemOnList(self, item, inputList):
        if item in inputList:
            return True
        else:
            return False

    # Converts file1 to a List
    def file1ToList(self):
        try:
            inputFile = open(inputFile1, "r")
            for line in inputFile:
                line = re.sub('[\n]', '', line)
                inputFile1List.append(line)
            inputFile.close()
        except Exception, e:
            print e

    # Converts file2 to a List
    def file2ToList(self):
        try:
            inputFile = open(inputFile2, "r")
            for line in inputFile:
                line = re.sub('[\n]', '', line)
                inputFile2List.append(line)
            inputFile.close()
        except Exception, e:
            print e

    # Compares List1 and List2, prints out items on both Lists in the console
    def compareLists(self):

        self.file1ToList()
        # print inputFile1List
        self.file2ToList()
        # print inputFile2List

        i = 0
        while i < len(inputFile2List):
            if self.isItemOnList(inputFile1List[i], inputFile2List):
                print inputFile1List[i]
            i += 1

fd = FindDuplicates()
fd.compareLists()