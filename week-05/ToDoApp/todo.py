import sys
from sys import argv
import csv

class ToDoApp():
    def __init__(self):
        try:
            self.open_csv()
        except FileNotFoundError:
            pass

    def cmdLine_arg(self):
        print('Python Todo application\n')
        print('=======================')
        print('Command line arguments:')
        print(' -l   Lists all the tasks')
        print(' -a   Adds a new task')
        print(' -r   Removes an task')
        print(' -c   Completes an task')


    def open_csv(self):
        with open('todo.csv', newline='') as f:
            self.f = list(csv.reader(f, delimiter=';'))
        return self.f

    def list_all_tasks(self):
        try:
            if len(self.f) == 0:
                print('No todos for today! :)')
            number = 0
            output = ''
            for line in self.f: #self
                number += 1
                output += (str(number) + ' - ' + str(line[0 ]) + '\n')
            return output
        except FileNotFoundError:
            return 'File not found'

    def add_new_task(self):
        try:
            f = open('todo.csv','a')
            if len(sys.argv) == 2:
                 print('Unable to remove: No index is provided')
            else:
                f.write(sys.argv[2] + '\n')
        except FileNotFoundError:
            return 'File not found'

    def remove_task(self):
        file = open('todo.csv')
        f = file.readlines()
        file.close()

        if len(sys.argv) == 2:
             print('Unable to remove: No index is provided')
        elif(int(argv[2])) > len(f):
             print('Unable to remove: Index is out of bound')
        elif (type(sys.argv[2])) == str:
            try:
                int(sys.argv[2])
                file = open('todo.csv')
                remove_list = file.readlines()
                remove_list = remove_list[:(int(sys.argv[2]))-1] + remove_list[(int(sys.argv[2])):]
                file.close()
                remove_output = ''
                file = open('todo.csv', 'w')
                for item in remove_list:
                    remove_output += item
                file.write(remove_output)
                file.close()
            except:
                print('Index is not a number')

    def complete_a_task(self):
        print('This will be the Complete function')

    def main(self):
        if len(sys.argv) == 1:
            self.cmdLine_arg()
        elif len(sys.argv) > 1:
           if (sys.argv[1]) == '-l':
               print(self.list_all_tasks())
           if (sys.argv[1]) == '-a':
               self.add_new_task()
           if (sys.argv[1]) == '-r':
               self.remove_task()
           if (sys.argv[1]) == '-c':
               self.complete_a_task()
           cmd_args = ['-l','-a','-r','-c']
           if (sys.argv[1]) not in cmd_args:
               print('Unsupported argument \n')
               self.cmdLine_arg()

todoapp = ToDoApp()
todoapp.main()
