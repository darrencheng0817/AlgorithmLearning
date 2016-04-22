'''
Created on 2016年3月1日

@author: Darren
'''
from math import log
import unittest

class TFIDFCalculator(object):
    def search(self,query,cropus):
        if not cropus:
            raise Exception("Empty cropus")
        totalDoc=len(cropus)
        wordsStatistic={}
        docStatistic={}
        for docName in cropus.keys():
            wordsList=cropus[docName]
            wordCount=0
            for word in wordsList:
                wordCount+=1
                if word not in wordsStatistic:
                    wordsStatistic[word]={}
                if docName not in wordsStatistic[word]:
                    wordsStatistic[word][docName]=0
                wordsStatistic[word][docName]+=1
            docStatistic[docName]=wordCount    
        maxTFIDF=0
        res=""
        print(docStatistic)
        print(wordsStatistic)
        for docName in cropus:
            TFIDFValue=0
            for queryWord in query:
                if docName not in wordsStatistic[queryWord]:
                    continue
                TF=wordsStatistic[queryWord][docName]/docStatistic[docName]
                IDF=log(totalDoc/len(wordsStatistic[queryWord]))
                TFIDFValue+=TF*IDF
            if TFIDFValue>maxTFIDF:
                maxTFIDF=TFIDFValue
                res=docName
            print(docName,TFIDFValue)
        return res 

class Test(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)
        self.testClass=TFIDFCalculator()
        
    def test_search(self):
        query=["interview","with", "thumbtack"]
        cropus={"doc1":["interview", "with", "thumbtack"],
                "doc2":["happy"],
                "doc3":["interview"]
                }
        expectedResult="doc1"
        actualReslut=self.testClass.search(query, cropus)
        self.assertEqual(expectedResult, actualReslut)
        
unittest.main()
        