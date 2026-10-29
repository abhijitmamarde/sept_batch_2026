i = 11
while i <= 10:
    print(i) 
    i = i + 1
else:
    print("Done 1")

for i in range(1, 11):
    print(i)
else:
    print("Done 1")

l1 = [1, 2, 3, 4, 5]
for i in l1:
    print(i)
else:
    print("Done 1")

f = open("somefile.txt", "w")
for i in range(1, 6):
    f.write(f"{i}\n")
else:
    f.close()
    print("All numbers data is written...")
