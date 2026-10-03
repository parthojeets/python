import os
# Specify the directory you want to list
directory_path = 'c:\\Users\\Alex\\Documents\\VS code\\python\\Chapter 1'
# list all files and directories in the specified directory
contents = os.listdir(directory_path)
# Print the contents
for item in contents:
    print(item)
