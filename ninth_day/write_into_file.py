# open
# filename
# open mode: r - read, w - write, a - append

name = "Sagar"
fp = open("myname.txt", "w")
fp.write(name)

# always close the file as soon as 
# file operation is done
fp.close()

