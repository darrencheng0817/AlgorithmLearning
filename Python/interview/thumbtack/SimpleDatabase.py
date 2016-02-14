'''
Created on 2016年2月10日
A simple in-memory Database, following command are supported
    SET name value – Set the variable name to the value value. Neither variable names nor values will contain spaces.
    GET name – Print out the value of the variable name, or NULL if that variable is not set.
    UNSET name – Unset the variable name, making it just like that variable was never set.
    NUMEQUALTO value – Print out the number of variables that are currently set to value. If no variables equal that value, print 0.
    END – Exit the program. The program will always receive this as its last command.
    BEGIN – Open a new transaction block. Transaction blocks can be nested; a BEGIN can be issued inside of an existing block.
    ROLLBACK – Undo all of the commands issued in the most recent transaction block, and close the block. Print nothing if successful, or print NO TRANSACTION if no transaction is in progress.
    COMMIT – Close all open transaction blocks, permanently applying the changes made in them. Print nothing if successful, or print NO TRANSACTION if no transaction is in progress.
Performance:
    All commands besides ROLLBACK run in O(1) time
    
@author: Darren
'''
import sys

class CommandError(Exception):
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return repr("Error command: "+self.message)

class ENDCommand(Exception):
    def __init__(self):
        self.message = "Reached the end of command."
    def __str__(self):
        return repr(self.message)
    
NOTRANSACTION_STRING="NO TRANSACTION"
NULLRESULT_STRING="NULL"

class SimpleDatabase(object):
    def __init__(self):
        self.__commands={"BEGIN": (self.__process_begin,0),
                         "END":(self.__process_end,0),
                         "ROLLBACK":(self.__process_rollback,0),
                         "COMMIT":(self.__process_commit,0),
                         "SET":(self.__process_set,2),
                         "UNSET":(self.__process_unset,1),
                         "GET":(self.__process_get,1),
                         "NUMEQUALTO":(self.__process_numequalto,1)
                         }
        self.__data={}
        self.__count={}
        self.__data_diffs=[{}]
        self.__count_diffs=[{}]
        self.print_flag=True
    
    def clear_data(self):
        self.__data={}
        self.__count={}
        self.__data_diffs=[{}]
        self.__count_diffs=[{}]
        
    def __process_begin(self,*arguments):
        self.__data_diffs.append({})
        self.__count_diffs.append({})
        
    def __process_rollback(self,*arguments):
        if not self.__data_diffs or not self.__data_diffs[-1]:
            self.__count_diffs.pop()
            self.__data_diffs.pop()
            if not self.__count_diffs or not self.__data_diffs:
                self.__count_diffs=[{}]
                self.__data_diffs=[{}]
            return NOTRANSACTION_STRING
        else:
            data_diff=self.__data_diffs[-1]
            count_diff=self.__count_diffs[-1]
            for key in data_diff:
                if data_diff[key]==None:
                    self.__data.pop(key)
                else:
                    self.__data[key]=data_diff[key]
            for key in count_diff:
                if count_diff[key]==None:
                    self.__count.pop(key)
                else:
                    self.__count[key]=count_diff[key]
            self.__count_diffs.pop()
            self.__data_diffs.pop()
            if not self.__count_diffs or not self.__data_diffs:
                self.__count_diffs=[{}]
                self.__data_diffs=[{}]
                
    def __commit_check(self):
        for d in self.__data_diffs:
            if d:
                return True
        return False
    
    def __process_commit(self,*arguments):
        if not self.__commit_check():
            self.__data_diffs=[{}]
            self.__count_diffs=[{}]
            return NOTRANSACTION_STRING
        self.__data_diffs=[{}]
        self.__count_diffs=[{}]
    
    def __process_set(self,*arguments):
        key,value=arguments
        data_diff=self.__data_diffs[-1]
        count_diff=self.__count_diffs[-1]
        if key not in self.__data:
            #new data added
            if key not in data_diff:
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
                if count_diff[origin_value]==None:
                    count_diff.pop(origin_value)
        if value not in self.__count:
            self.__count[value]=0
            if value not in count_diff:
                count_diff[value]=None
        else:
            if value not in count_diff:
                count_diff[value]=self.__count[value]
        self.__count[value]+=1
        self.__data[key]=value
        
    def __process_get(self,*arguments):
        key=arguments[0]
        if key not in self.__data:
            return NULLRESULT_STRING
        else:
            return self.__data[key]
    
    def __process_unset(self,*arguments):
        key=arguments[0]
        if key in self.__data:
            data_diff=self.__data_diffs[-1]
            count_diff=self.__count_diffs[-1]
            value=self.__data[key]
            if key not in data_diff:
                data_diff[key]=value
            elif data_diff[key]==None:
                data_diff.pop(key)
            if value not in count_diff:
                count_diff[value]=self.__count[value]
            self.__data.pop(key)
            self.__count[value]-=1
            if self.__count[value]==0:
                self.__count.pop(value)
                if count_diff[value]==None:
                    count_diff.pop(value)
    
    def __process_numequalto(self,*arguments):
        key=arguments[0]
        if key not in self.__count:
            return "0"
        else:
            return str(self.__count[key])
    
    def __process_end(self,*arguments):
        raise ENDCommand()
        
    def process_command(self,command):    
        command_list=command.strip().split(" ")
        command_key=command_list[0]
        arguments=command_list[1:]
        if command_key not in self.__commands:
            raise CommandError("Command not supported!")
        else:
            func,arguments_num=self.__commands[command_key]
            if len(arguments)!=arguments_num:
                raise CommandError("Error arguments!")
            else: 
                try:
                    return func(*command_list[1:])
                except KeyError:
                    print("Sorry, some error happened!")
                    exit()
                    
    def run_from_command(self):
        while True:
            command=input().strip()
            try:
                result=self.process_command(command)
                if result:
                    print(result)
            except CommandError as e:
                print(e)
            except ENDCommand as e:
                break
                
    def run_from_file(self,file_name):
        results=[] #for test and other purpose
        try:
            with open(file_name,"r") as file:
                while True:
                    try:
                        command=file.readline().strip()
                        result=self.process_command(command)
                        if result:
                            if self.print_flag:
                                print(result)
                            results.append(str(result))
                    except CommandError as e:
                        print(e)
                    except ENDCommand as e:
                        file.close()
                        break
                    except EOFError:
                        file.close()
                        break
        except FileNotFoundError as e:
            print("No such file: "+file_name)
        except PermissionError as e:
            print("Permission denied: "+file_name)
        return results       
     
if __name__ == '__main__':
    simpleDatabase=SimpleDatabase()
    if len(sys.argv)==1:
        simpleDatabase.run_from_command()
    elif len(sys.argv)==2:
        simpleDatabase.run_from_file(sys.argv[1])
    else:
        print('''Too many arguments
        Usage:
            python3 SimpleDatabase.py : for command line mode
            python3 SimpleDatabase.py file_name : load commands from file
        ''')