fp = open("mynames.txt", "r")

names = fp.readlines() 

# for name in names:
#     # fp.write(name)
#     fp.write(name + "\n")

# fp.writelines(names)
# AbhijitSagarManish



fp.close()

names = [name.strip() for name in names]
print(f"Names read are: {names}")

# for name in names:
#     name = name.strip()
#     print(f"The name is: {name} and he is student of this batch.")
