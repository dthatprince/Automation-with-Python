# define file path
fileName = 'inputFile.txt'

# read file
f = open(fileName,'r')

output1 = "PassFile.txt"
output2 = "FailFile.txt"

passFile = open(output1,'w')
failFile = open(output2, 'w')

# to print every line
for line in f:
    line_split = line.split()
    if line_split[2] == "P":
        passFile.write(line)
    else:
        failFile.write(line)

passFile.close()
failFile.close()
