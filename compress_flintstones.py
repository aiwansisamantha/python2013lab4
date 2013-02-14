# Filename: compress.py
# Description: compress an ASCII file

def compress(line):
    while len(line) > 0:
        # while there's stuff to compress in the line
        if len(line) > 1:
            # only check for repetition of there's more than one character in the line
            if line[0] == line[1]:
                char = line[0]
                # assign the character first
                n = 0
                while len(line) > 1 and line[0] == char:
                    # take away first occurrence
                    n = n + 1
                    line = line[1:]                    
                print(char + str(n))
            else:
                print(line[0])
                line = line[1:]
        else:
            print(line)
            break

try:
    infile = open("flintstones.txt", 'r')

    lines = infile.readlines()
    for line in lines[:-1]:
        compress(line)
        print("---")
    compress(lines[-1])
    infile.close()
except IOError:
    print("Error reading from flintstones.txt.")
