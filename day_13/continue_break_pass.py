# pass - keyword which means NO-OP No Operation
# used in places where by syntax we need to put some statement but we dont have any yet

def f1():
    pass
    
print("This is start of program...")
f1()
print("This is end of program...")

# ==============
# continue and break
# both are used within the loop 
# continue is used for continuing (bypoass the rest of the block of code) with next iteration in the loop
# break is for breaking out from the runing loop to the first statement outside the loop


# break

i = 1
while i <= 100:
    print(f"i is: {i}")
    if i == 3:
        break
    i = i + 1
    print(f"i is incremented to: {i}")

print("Outside the while loop")


for i in range(1, 100):
    if i == 5:
        break
    print(f"I is: {i}")

print("Outside the for loop")

# continue

for i in range(1, 101):
    if i < 95:
        continue
    print(f"i is: {i}")

# as good as doing below operation
# for i in range(95, 101):
#     print(f"i is: {i}")
