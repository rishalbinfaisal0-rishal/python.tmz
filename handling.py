# file handling
# exception handling 

# file1 = open("hello.txt","r")
# print(file1.read())
# file1.close()


# file2 = open("bye.txt","w")
# file2.write("i am a rider.....")
# file2.close()

# file3 = open("demo.txt","a")
# for i in range(1,100):
#     file3.write(f"am legendery !!!!!! times{i}!!!!!\n")
# file3.close()

# with open("hello.txt","r") as f:
#     print(f.read())

import os 

# os . mkdir("django")
# os.rename("bye.txt","byeeeeee.txt")
file_path = "C:\\Users\\HP\\OneDrive\\Documents\\New folder (2)"
os.remove(file_path)
# print(file_path)
if os.path.eixsts(file_path):
    if os.path.isdir(file_path):
        print("folder")
    elif os.path.isfile(file_path):
        print("its a file")