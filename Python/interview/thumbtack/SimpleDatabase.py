'''
Created on 2016年2月10日
A simple in-memory Database, following command are supported
    SET name value – Set the variable name to the value value. Neither variable names nor values will contain spaces.
    GET name – Print out the value of the variable name, or NULL if that variable is not set.
    UNSET name – Unset the variable name, making it just like that variable was never set.
    NUMEQUALTO value – Print out the number of variables that are currently set to value. If no variables equal that value, print 0.
    END – Exit the program. The program will always receive this as its last command.
    BEGIN – Open a new transaction_log block. transaction_log blocks can be nested; a BEGIN can be issued inside of an existing block.
    ROLLBACK – Undo all of the commands issued in the most recent transaction_log block, and close the block. Print nothing if successful, or print NO transaction_log if no transaction_log is in progress.
    COMMIT – Close all open transaction_log blocks, permanently applying the changes made in them. Print nothing if successful, or print NO transaction_log if no transaction_log is in progress.
Performance:
    All commands besides ROLLBACK run in O(1) time
For transaction recovery, write-through techniques are used.  

@author: Darren
'''
import sys
import traceback
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
    
NO_TRANSACTION_STRING="NO TRANSACTION"
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
        self.__transaction_logs=[{}]
        self.print_flag=True
    
    def clear_data(self):
        self.__data={}
        self.__count={}
        self.__transaction_logs=[{}]
        
    def __process_begin(self,*arguments):
        self.__transaction_logs.append({})
        
    def __process_rollback(self,*arguments):
        if not self.__transaction_logs or not self.__transaction_logs[-1]:
            self.__transaction_logs.pop()
            if not self.__transaction_logs:
                self.__transaction_logs=[{}]
            return NO_TRANSACTION_STRING
        else:
            transaction_log=self.__transaction_logs[-1]
            for key in transaction_log:
                if key in self.__data:
                    new_value=self.__data[key]
                    self.__count[new_value]-=1
                    if self.__count[new_value]==0:
                        self.__count.pop(new_value)
                if transaction_log[key]==None:
                    self.__data.pop(key)                
                else:
                    original_value=transaction_log[key]
                    if original_value not in self.__count:
                        self.__count[original_value]=0
                    self.__count[original_value]+=1
                    self.__data[key]=transaction_log[key]
            self.__transaction_logs.pop()
            if not self.__transaction_logs:
                self.__transaction_logs=[{}]
                
    def __commit_check(self):
        for d in self.__transaction_logs:
            if d:
                return True
        return False
    
    def __process_commit(self,*arguments):
        if not self.__commit_check():
            self.__transaction_logs=[{}]
            return NO_TRANSACTION_STRING
        else:
            self.__transaction_logs=[{}]
    
    def __process_set(self,*arguments):
        key,value=arguments
        transaction_log=self.__transaction_logs[-1]
        if key not in self.__data:
            #new data added
            if key not in transaction_log:
                transaction_log[key]=None
        else:
            #change a existed data
            if key not in transaction_log:
                transaction_log[key]=self.__data[key]
            origin_value=self.__data[key]
            self.__count[origin_value]-=1
            if self.__count[origin_value]==0:
                self.__count.pop(origin_value)
        if value not in self.__count:
            self.__count[value]=0
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
            transaction_log=self.__transaction_logs[-1]
            value=self.__data[key]
            if key not in transaction_log:
                transaction_log[key]=value
            elif transaction_log[key]==None:
                transaction_log.pop(key)
            self.__data.pop(key)
            self.__count[value]-=1
            if self.__count[value]==0:
                self.__count.pop(value)
    
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
                    print(traceback.print_exc())
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