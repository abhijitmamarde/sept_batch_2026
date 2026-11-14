import os
import shutil

print("The current working dir is:")
print(os.getcwd())


file_name = "sample.txt"
print(f"Deleting file {file_name}")

try:
    os.remove(f"{file_name}")
except FileNotFoundError:
    print(f"File {file_name} not found, hence could not delete!")
else:
    print(f"{file_name} deleted!")


# if it is empty
# os.rmdir("abc")

# this also removes everything under the dir specified
# shutil.rmtree("abc")