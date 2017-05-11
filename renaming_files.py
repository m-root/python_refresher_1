import os

def rename_files():
    #1.) Getting file names from a folder
    file_name_list = os.listdir(r"C:\oop\prank")
    #print(file_list)
    saved_path = os.getcwd()
    print("Current working directory is " + saved_path)
    print(file_name_list)
    # os.getcwd()
    os.chdir(r"C:\oop\prank")
    #2. For Each file name rename files
    for file_name in file_name_list:
        print("Old Name - " + file_name)
        print("New Name: " + file_name.translate(None, "123456789"))
        os.rename(file_name, file_name.translate(None, "123456789"))
    os.chdir(saved_path)

rename_files()

