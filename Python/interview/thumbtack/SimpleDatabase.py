'''
Created on 2016年2月10日

@author: Darren
'''
import sys

class CommandError(Exception):
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return repr("Erron command: "+self.message)

class SimpleDatabase(object):
    def __init__(self):
        self.__commands={"BEGIN":self.__process_begin,"END":self.__process_end,\
                       "ROLLBACK":self.__process_rollback,"COMMIT":self.__process_commit,\
                       "SET":self.__process_set,"UNSET":self.__process_unset,"GET":self.__process_get,\
                       "NUMEQUALTO":self.__process_numequalto}
        self.__data={}
        self.__count={}
        self.__data_diffs=[{}]
        self.__count_diffs=[{}]
    
    def __process_begin(self,*arguments):
        self.__data_diffs.append({})
        self.__count_diffs.append({})
        
    def __process_rollback(self,*arguments):
        if len(arguments)!=0:
            raise CommandError("Error arguments!")
        if not self.__data_diffs or not self.__data_diffs[-1]:
            print("NO TRANSACTION")
            return
        else:
            data_diff=self.__data_diffs[-1]
            count_diff=self.__count_diffs[-1]
            for key in data_diff:
                if not data_diff[key]:
                    self.__data.pop(key)
                else:
                    self.__data[key]=data_diff[key]
            for key in count_diff:
                if not count_diff[key]:
                    self.__count.pop(key)
                else:
                    self.__count[key]=count_diff[key]
            self.__count_diffs.pop()
            self.__data_diffs.pop()
    
    def __process_commit(self,*arguments):
        if len(arguments)!=0:
            raise CommandError("Error arguments!")
        if not self.__data_diffs or not self.__data_diffs[-1]:
            print("NO TRANSACTION")
            return
        self.__data_diffs=[{}]
        self.__count_diffs=[{}]
    
    def __process_set(self,*arguments):
        if len(arguments)!=2:
            raise CommandError("Error arguments!")
        key,value=arguments
        data_diff=self.__data_diffs[-1]
        count_diff=self.__count_diffs[-1]
        if key not in self.__data:
            #new data added
            data_diff[key]=None
        else:
            #change a existed data
            if key not in data_diff:
                data_diff[key]=self.__data[key]
            origin_value=self.__data[key]
            if origin_value not in count_diff:
                count_diff[origin_value]=self.__count[origin_value]
            self.__count[origin_value]-=1
            if self.__count[origin_value]==0:
                self.__count.pop(origin_value)
                if not count_diff[origin_value]:
                    count_diff.pop(origin_value)
        if value not in self.__count:
            self.__count[value]=0
            count_diff[value]=None
        else:
            if value not in count_diff:
                count_diff[value]=self.__count[value]
        self.__count[value]+=1
        
        self.__data[key]=value
        
    def __process_get(self,*arguments):
        if len(arguments)!=1:
            raise CommandError("Error arguments!")
        key=arguments[0]
        if key not in self.__data:
            print("NULL")
        else:
            print(self.__data[key])
    
    def __process_unset(self,*arguments):
        if len(arguments)!=1:
            raise CommandError("Error arguments!")
        key=arguments[0]
        if key in self.__data:
            data_diff=self.__data_diffs[-1]
            count_diff=self.__count_diffs[-1]
            value=self.__data[key]
            if key not in data_diff:
                data_diff[key]=value
            if value not in count_diff:
                count_diff[value]=self.__count[value]
            self.__data.pop(key)
            self.__count[value]-=1
            if self.__count[value]==0:
                self.__count.pop(value)
                if not count_diff[value]:
                    count_diff.pop(value)
    
    def __process_numequalto(self,*arguments):
        if len(arguments)!=1:
            raise CommandError("Error arguments!")
        key=arguments[0]
        if key not in self.__count:
            print("NULL")
        else:
            print(self.__count[key]) 
    
    def __process_end(self,*arguments):
        if len(arguments)!=0:
            raise CommandError("Error arguments!")
        else:
            exit()
        
    def __process_command(self,command):    
        command_list=command.strip().split(" ")
        if command_list[0] not in self.__commands:
            raise CommandError("Command not supported!")
        else:
            self.__commands[command_list[0]](*command_list[1:])
    
    def run_from_command(self):
        while True:
            command=input().strip()
            try:
                self.__process_command(command)
            except CommandError as e:
                print(e)
                
    def run_from_file(self,file_name):
        try:
            file=open(file_name,"r")
            while True:
                try:
                    command=file.readline().strip()
                    self.__process_command(command)
                except CommandError as e:
                    print(e)
                except EOFError:
                    break
        except FileNotFoundError as e:
            print("No such file: "+file_name)
        except PermissionError as e:
            print("Permission denied: "+file_name)
        finally:
            file.close()
                
if __name__ == '__main__':
    simpleDatabase=SimpleDatabase()
    simpleDatabase.run_from_file("DBCommand.txt")
    if len(sys.argv)==1:
        simpleDatabase.run_from_command()
    elif len(sys.argv)==2:
        simpleDatabase.run_from_file(sys.argv[1])
    else:
        print("Too many arguments")