names = ["ABC PQR", "QWE RTS", "OOP OUY"]

def create_pass(name):
    return name[::-1].lower().replace(" ", "") + "@1234"

passwd1 = create_pass(names[0])
print(passwd1)

# passwd2 = names[1][::-1].lower() + "@1234"
# print(passwd2)

# passwd3 = names[2][::-1].lower() + "@1234"
# print(passwd3)

passwd2 = create_pass(names[1])
print(passwd2)

passwd3 = create_pass(names[2])
print(passwd3)

# 

def greet():
    print("Hey User!")
    print("Hope you have a great day so far!")

    for i in range(1, 11):
        print(f"Hey how are you... calling for {i} time...")

    return 1

r = greet()
print(f"Return is {r}")

greet()
