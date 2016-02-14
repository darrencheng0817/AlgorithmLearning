'''
Created on 2016年2月10日

@author: Darren
'''
from SimpleDatabase import SimpleDatabase
import os
import unittest
from random import random

class Test(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)
        self.testClass=SimpleDatabase()
        self.testClass.print_flag=False
        
    def test_invalid_input(self):
        pass
    
    def test_robust(self):
        for _ in range(100):
            N=10000
            commands_d={"BEGIN":0,"END":0,"ROLLBACK":0,"COMMIT":0,"SET":2,"UNSET":1,"GET":1,"NUMEQUALTO":1}
            commands=["BEGIN","ROLLBACK","COMMIT","SET","UNSET","GET","NUMEQUALTO","END"]
            for _ in range(N):
                command=commands[int(random()*(len(commands)-1))]
                if command=="NUMEQUALTO":#special case
                    value=int(random()*100)
                    command+=" "+str(value) 
                elif commands_d[command]==1:
                    key=chr(ord("A")+int(random()*26))
                    command+=" "+str(key) 
                elif commands_d[command]==2:
                    key=chr(ord("A")+int(random()*26))
                    value=int(random()*100)
                    command+=" "+str(key) +" "+str(value)
                self.testClass.process_command(command)
            command=commands[-1]
            with self.assertRaises(Exception):
                self.testClass.process_command(command)  
            self.testClass.clear_data()
            
#     def test_robust(self):
#         file_name="test3.in"
#         for _ in range(10000):
#             N=100
#             self.generator_test_case(N, file_name)
#             self.testClass.run_from_file(file_name)
#             self.testClass.clear_data()
        
    def generator_test_case(self,N,file_name):
        commands_d={"BEGIN":0,"END":0,"ROLLBACK":0,"COMMIT":0,"SET":2,"UNSET":1,"GET":1,"NUMEQUALTO":1}
        commands=["BEGIN","ROLLBACK","COMMIT","SET","UNSET","GET","NUMEQUALTO","END"]
        with open(file_name,"w") as file:
            for _ in range(N):
                command=commands[int(random()*(len(commands)-1))]
                if command=="NUMEQUALTO":
                    value=int(random()*100)
                    file.write(" ".join([command,str(value)])+"\n")
                elif commands_d[command]==1:
                    key=chr(ord("A")+int(random()*26))
                    file.write(" ".join([command,key])+"\n")
                elif commands_d[command]==2:
                    key=chr(ord("A")+int(random()*26))
                    value=int(random()*100)
                    file.write(" ".join([command,key,str(value)])+"\n")
                else:
                    file.write(" ".join([command])+"\n")
            file.write(commands[-1])
        
    def load_result(self,file_name):
        try:
            file=open(file_name, "r")
            res=list(map(lambda x:x.strip("\n"),file.readlines()))
        except Exception as e:
            print("Error reading file: "+file_name)
        return res   
     
    def test_valid_input(self):
        path="DBTestData/valid"
        tests=[x for x in os.listdir(path) if os.path.splitext(x)[1]=='.in']
        for test in tests:
            actual_result=self.testClass.run_from_file(path+'/'+test)
            result_file_name=path+'/'+test[:-3]+'.out'
            expected_result=self.load_result(result_file_name)
            self.assertEqual(actual_result, expected_result, "Failed with input: "+test)
            self.testClass.clear_data()

if __name__ == "__main__":
    unittest.main()

        