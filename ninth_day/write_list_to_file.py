names = [
    "Abhijit",
    "Sagar",
    "Manish",
]

fp = open("mynames.txt", "w")

# for name in names:
#     # fp.write(name)
#     fp.write(name + "\n")

# fp.writelines(names)
# AbhijitSagarManish

fp.writelines(
    [name + "\n" for name in names]
)

fp.close()
