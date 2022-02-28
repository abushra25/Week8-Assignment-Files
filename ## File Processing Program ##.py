## File Processing Program ##
## Created by Ahmed Bushra ##
## for CIS245-304j, 02/26/22 ##

import os ## Module import to create/remove & fetch contents of directory/files ##

## Prompting user for name of directory to save file & file name ##

directory_path = input("Please enter the directory path:")
file_name= input("Please enter the name of the file:")

## Checking if directory exists or a new one will be created | Sources -> https://www.geeksforgeeks.org/create-a-directory-in-python/, https://www.geeksforgeeks.org/python-check-if-a-file-or-directory-exists-2/, https://stackoverflow.com/questions/25675352/how-to-check-to-see-if-a-folder-contains-files-using-python-3##
if not os.path.isdir(directory_path):
    os.makedirs(directory_path) ## This would sometimes work as just 'makedir' and then other times it would compile and run but throw an error and asked me if I wanted to correct it to 'makedirs'. Is that typical? ##

file_path= directory_path + file_name ## Appending user input of file_name. file_path will be used later to pull file and its contents ##

## User prompt for name, address, phone, & write data as comma separated values ##
user_file= open(file_path, 'a') ## Was receiving a Errno 2 filenotfound error before utilizing "a" fo append mode | Sources -> https://www.w3schools.com/python/ref_func_open.asp & https://stackoverflow.com/questions/22282760/filenotfounderror-errno-2-no-such-file-or-directory ##

user_name= input("Please enter your name: ")
user_file.write (user_name + ',') ## Got a TextIOWrapper error and learned I needed to use "+" so the comma was not passed through as an argument! ##

address=input("Please enter your address: ")
user_file.write (address + ',')

phone_number=input("Please enter your phone number: ")
user_file.write (phone_number + ',')

user_file.close()

## Reading the created file and contents + display to user ##
user_file1 = open(file_path)
output = user_file1.readlines()
print("Your created file contains the following data: \n", output)
user_file1.close()