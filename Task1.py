#Task 1 of Assignment 4 - Read a File and Handle Errors
import io

file_name = "sample11.txt"
try:
    fh = open(file_name,"rt")   #opening file for reading purpose
    print("Reading file content:")

except FileNotFoundError:       #handling error if file not exists
    print(f"Error: The file \'{file_name}\' was not found.")
    exit()

except io.UnsupportedOperation as e:    #handling error if unable to read file
    print(f"Error: File \'{file_name}\' cannot be opened.")
    exit()

else:
    l_count = 0
    while line := fh.readline():
        l_count += 1
        print(f"Line {l_count}: {line}",end="")
    print()
    fh.close()

finally:
    print("Bye!!!")


#end of program
