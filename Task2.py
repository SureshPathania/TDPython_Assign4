#Task 2 of Assignment 4 - Write and Append Data to a File
import io

file_name = "output.txt"
try:
    text = input("Enter text to write to the file: ")
    with open(file_name,"wt") as fh:        #opening file in write mode
        fh.write(text + "\n")
    print(f"Data successfully written to the file \'{file_name}\'.\n")

    text = input("Enter additional text to append to the file: ")
    with open("output.txt","at") as fh:       #opening file in append mode
        fh.write(text + "\n")
    print(f"Data successfully appended to the file \'{file_name}\'.\n")

    with open(file_name,"rt") as fh:   #opening file for reading purpose
        print(f"Final content of the file \'{file_name}\':")
        while line := fh.readline():
            print(f"{line}",end="")
    print()

except FileNotFoundError:       #handling error if file not exists
    print(f"Error: The file \'{file_name}\' was not found.")
    exit()

except io.UnsupportedOperation as e:    #handling error if unable to read file
    print(f"Error: File \'{file_name}\' cannot be opened.")
    exit()

finally:
    print("Bye!!!")

#end of program