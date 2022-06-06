# Python program to explain os.mkdir() method

# importing os module
import os
from establish_server_connection import connection_test

dir_name = input('Enter MO or SO for directory name: ')
file_name = input('Enter file name: ')
dir_path = os.path.join("C:\\", "Users", 'milleri', 'Desktop', dir_name)
complete_path = os.path.join(dir_path, file_name + '.txt')

try:
    os.mkdir(dir_path)
    f = open(complete_path, "w")
    f.write("Woops! I have deleted the content!")
    f.close()
    print(f'Directory "{dir_name}" and file "{file_name}" Created ')
except FileExistsError:
    print(f'Directory {dir_name} already exist')


connection_test()
