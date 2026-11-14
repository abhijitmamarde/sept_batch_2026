import os

print("The current working dir is:")
print(os.getcwd())

print("Files in Project path:\n")
files = os.listdir("/Volumes/Abhi1TB/pwork/sept_batch_2026")
for index, file in enumerate(files, start=1):
    print(index, file)

print("\n" + ("-"*210) + "\n")

print("Files in current working directory:\n")
print(os.listdir("."))

print("\n" + ("-"*210) + "\n")


print("Changing to another directory...")
os.chdir("/Volumes/Abhi1TB/pwork/sept_batch_2026/day_17")

print("Now, The current working dir is:")
print(os.getcwd())

print("Files in current working directory:\n")
print(os.listdir("."))

print("\n" + ("-"*210) + "\n")
