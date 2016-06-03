import sys
from sys import argv


class ToDoApp():
    def __init__(self):
        pass

    def cmdLine_arg(self):
        print('Python Todo application\n', '=======================\n', 'Command line arguments:\n', ' -l   Lists all the tasks\n', ' -a   Adds a new task\n', ' -r   Removes an task\n', ' -c   Completes an task\n')

    def missing_file(self):
        try:
            file = open('todoapp.csv')
            file.close()
        except:
            file = open('todoapp.csv', a)
            file.close()

    def read_in_txt(self):
        file = open('todoapp.csv')
        f = file.readlines()
        file.close()
        return f

    def list_all_tasks(self):
        self.missing_file()
        f = self.read_in_txt()
        if len(f) == 0:
            print('No todos for today! :)')
        number, output = 0, ''
        for line in f:
            number += 1
            output += (str(number) + ' - ' + line)
        return output

    def add_new_task(self, task):
        self.missing_file()
        if len(sys.argv) == 2:
             print('Unable to remove: No index is provided')
        else:
            try:
                file = open('todoapp.csv', 'a')
                file.write(False, '[ ]' + task + '\n')
                file.close()
            except FileNotFoundError:
                return 'File not found'

    def remove_task(self):
        self.missing_file()
        f = self.read_in_txt()
        if len(sys.argv) == 2:
             print('Unable to remove: No index is provided')
        elif (type(sys.argv[2])) == str:
            try:
                if(int(argv[2])) > len(f):
                     print('Unable to remove: Index is out of bound')
                int(sys.argv[2])
                file = open('todoapp.csv')
                remove_list = file.readlines()
                remove_list = remove_list[:(int(sys.argv[2]))-1] + remove_list[(int(sys.argv[2])):]
                file.close()
                remove_output = ''
                file = open('todoapp.csv', 'w')
                for item in remove_list:
                    remove_output += item
                file.write(remove_output)
                file.close()
            except:
                print('Index is not a number')

    def complete_a_task(self):
        self.missing_file()
        try:
            f = open('todoapp.csv')
            text = f.readlines()
            item = text[int(sys.argv[2])-1]
            item = item.replace('[ ]', '[x]')
            f.close()
            f = open('todoapp.csv', 'w')
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
               self.add_new_task(sys.argv[2])
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
