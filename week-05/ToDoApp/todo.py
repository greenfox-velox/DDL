import sys
from sys import argv


class ToDoApp():
    def __init__(self):
        pass

    def cmdLine_arg(self):
        print('Python Todo application\n')
        print('=======================')
        print('Command line arguments:')
        print(' -l   Lists all the tasks')
        print(' -a   Adds a new task')
        print(' -r   Removes an task')
        print(' -c   Completes an task')

    def missing_file(self):
        try:
            file = open('todo.txt')
            file.close()
        except:
            file = open('todo.txt', a)
            file.close()


    def list_all_tasks(self):
        self.missing_file()
        try:
            file = open('todo.txt')
            f = file.readlines()
            file.close()
            if len(f) == 0:
                print('No todos for today! :)')
            number = 0
            output = ''
            for line in f:
                number += 1
                output += (str(number) + ' - ' + line)
            return output
        except FileNotFoundError:
            return 'File not found'

    def add_new_task(self):
        self.missing_file()
        if len(sys.argv) == 2:
             print('Unable to remove: No index is provided')
        else:
            try:
                file = open('todo.txt', 'a')
                file.write('[ ]' + sys.argv[2] + '\n')
                file.close()
            except FileNotFoundError:
                return 'File not found'

    def remove_task(self):
        self.missing_file()
        file = open('todo.txt')
        f = file.readlines()
        file.close()
        if len(sys.argv) == 2:
             print('Unable to remove: No index is provided')
        elif (type(sys.argv[2])) == str:
            try:
                if(int(argv[2])) > len(f):
                     print('Unable to remove: Index is out of bound')
                int(sys.argv[2])
                file = open('todo.txt')
                remove_list = file.readlines()
                remove_list = remove_list[:(int(sys.argv[2]))-1] + remove_list[(int(sys.argv[2])):]
                file.close()
                remove_output = ''
                file = open('todo.txt', 'w')
                for item in remove_list:
                    remove_output += item
                file.write(remove_output)
                file.close()
            except:
                print('Index is not a number')

    def complete_a_task(self):
        self.missing_file()
        try:
            f = open('todo.txt')
            text = f.readlines()
            text[int(sys.argv[2])-1] = text[int(sys.argv[2])-1].replace('[ ]', '[x]')
            f.close()
            f = open('todo.txt', 'w')
            for i in text:
                f.write(i)
            f.close()
        except IndexError:
            if len(sys.argv) == 2:
                print ('Unable to check: No index is provided')
            else:
                print('Unable to check: Index is out of bound')
        except ValueError:
            print ('Unable to check: Index is not a number')

    def main(self):
        self.missing_file()
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
