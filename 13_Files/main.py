# 13) FILES :
# 13A) Opening files (TASK: Open the text.txt file)

# '.' : Current Directory opened in the text editor
# '..' : Parent Directory of the Current Directory opened in the text editor

my_file = open("./13_Files/text.txt")
print(my_file)

# 13B) Opening modes :

# 13B1) "r" - Read - Default value. Opens a file for reading, error if the file does not exist

# TASK: Repeat the above the task with specifying the mode :
my_file = open("./13_Files/text.txt", "r") # default
print(my_file)

# 13B2) "x" - Create - Creates the specified file, returns an error if the file exists
# my_file = open("./13_Files/text.txt", "x") # ERROR!, cz already exists

# TASK: Open/Create and Open a non-existing file :
my_file = open("./13_Files/text2.txt", "x") # Creates empty text2.txt
print(my_file)

# 13C) Opening type :
# "t" - Text - Default value. Text mode
# TASK: Repeat the above the task with specifying the mode or/and type :
my_file = open("./13_Files/text2.txt", "rt") # default
print(my_file)

# "b" - Binary - Binary mode (ex: images)

# TASK: Create a duplicate image file using the binary type

src_img = open("./Images/OverView.png", "rb")
other_file = open("./13_Files/duplicate.png", "wb") 
other_file.write(src_img.read()) # Creates a duplicates to OverView.png in the Images folder over here in the 13_Files folder, with the name duplicate.png

# 13D) Reading Files :
# 13D1) read() method : (And its arguments)
my_file = open("./13_Files/text.txt", "rt")

my_str = my_file.read() # reads all characters
print(my_str)

my_str = my_file.read(5) # reads first 5 characters
print(my_str)

# 13D2) readline() and readlines() methods :
my_str = my_file.readline() # reads first 1 line
print(my_str)

my_str = my_file.readlines() # reads all lines
print(my_str) # list

my_str = my_file.readlines(2) # reads first 2 lines
print(my_str) # list

# 13D3) Looping through an opened file :
for line in my_file.readlines(): # here, 'line' is a string
    print(line)

# NOTE:
# 1) Closing files: The close() method
# TASK: Close the opened files :
my_file.close() # It is always a good programming habit to close all the opened files for data-privacy, avoid data-leaks etc

'''
2) The following modes will be discussed in the coming videos :
- "a", "w" modes, writing into files using write(), writelines()
- readable(), writable() and file-permissions(and some bash)
- Deleting files and folders
'''
