# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 13:04:30 2021

@author: 20315914
"""
from functools import *

class tag:
    def __init__(self,tagno,cableLength,cableSize,drumNo=1):
        self.tagn = tagno
        self.cableLengt = cableLength
        self.cableSiz = cableSize
        self.drumN = drumNo
    def display(self):
        print(self.tagn,self.cableLengt,self.cableSiz,self.drumN)
    
#firstTag = tag('k-1101A',980,'3Cx150',2)
#firstTag.display()
inputData = [1100,1111,1234,3300,4000,300,400,500,600,700,350,450,250,650,550,200,100,150,800,850,900,950,1200,50]
completed = True
maxLength = 1000
moreThanMax =list (filter(lambda x: x>maxLength, inputData))
lessThanMax =list (filter(lambda x: x<=maxLength, inputData))
finalDrums = []
intermediateDrums = []
# function to extract only extra length from lengths greater than max drum length
def flattenInput(length):
    extra = length-maxLength
    if extra > maxLength:
        flattenInput(extra)
    if extra<=maxLength:
        intermediateDrums.append(extra)
    intermediateDrums.append(maxLength)

for i in moreThanMax:
    flattenInput(i)
    
for i in intermediateDrums:
    if i < maxLength:
        lessThanMax.append(i)
    else:
        finalDrums.append(i)
#print (sorted(lessThanMax))
#print (sorted(intermediateDrums))
#print (sorted(finalDrums))

'''
def addToDrums(newArray):
        for i in newArray:
            if i < difference:
                currentDrum.append(i)
                newArray.remove(i)
                difference = maxLength - sum(currentDrum)
                addToDrums(newArray)
                break
        else:
            pass
'''
ignore = []
while (completed):
    currentLength = max(lessThanMax)
    lessThanMax.remove(currentLength)
    currentDrum=[currentLength]
    lessThanMax.sort(reverse=True)
    difference = maxLength - sum(currentDrum)
    
    #print(lessThanMax)
    for index,value in enumerate(lessThanMax):
        #print(value)
        if index not in ignore:
            if value <= difference and (value+sum(currentDrum))<=maxLength:
                currentDrum.append(value)
                lessThanMax.remove(value)

    finalDrums.append(currentDrum)
            
    #addToDrums(lessThanMax) 

    print(lessThanMax)
    #print('done')

    if len(lessThanMax) == 0:
        completed = False  






print(finalDrums)