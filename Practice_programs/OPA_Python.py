# -*- coding: utf-8 -*-
"""
Created on Sat May 30 13:35:14 2020

@author: LENOVO
"""

class Professor():
    def __init__(self,profId, profName, subjectsDict):
        self.profId = profId
        self.profName = profName
        self.subjectsDict = subjectsDict
class University():
    def __init__(self, test):
        self.test = "tesint"
    def getTotalExperience(self,profList, profId):
        result = 0
        for item in profList:
            proFId=int(profId)
            if item.profId == proFId:
                for exp in item.subjectsDict.values():
                    result+=exp
        return result
    def selectSeniorProfessorBySubject(self,profList, subjectName):
        result= -9
        found = False
        obj=None
        for item in profList:
            if item.subjectsDict[subjectName.upper()]>= result:
                result = item.subjectsDict[subjectName.upper()]
                found = True
                obj = item
        if found == False:
            return 'None'
        else:
            return str(obj.profId)+" "+ obj.profName+" "+str(obj.subjectsDict)
if __name__ == "__main__":


    T = int(input().strip())
    
    profObjects=[]
    while T>0:
        profId = int(input())
        profName = input().strip()
        numSubjects = int(input().strip())
        subjectDict={}
        while numSubjects>0:
            subjectName = input().strip()
            exp = int(input().strip())
            subjectDict[subjectName.upper()] = exp
            numSubjects-=1
        obj = Professor(profId,profName,subjectDict)
        profObjects.append(obj)
        T-=1
    profSearch = input().strip()
    subjectSearch = input().strip()
    obj = University("tset")
    print(obj.getTotalExperience(profObjects,profSearch))
    print(obj.selectSeniorProfessorBySubject(profObjects, subjectSearch))