fp = open("myname.txt", "r")
name = fp.read()

# always close the file as soon as 
# file operation is done
fp.close()

print(f"Name read from file is: {name}")
