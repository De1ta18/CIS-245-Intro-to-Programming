import os.path

def name(): #function to ask user for name
    while True:
        try:
            user_name = str(input('Please enter your name: ').title())
            return user_name
        except ValueError:
            print("")

def address(): #function to ask user for address
    while True:
        try:
            user_address = input('Please enter your address: ')
            return user_address
        except Exception:
            print("")

def phn_num(): #function to ask user for phone number
    while True:
        try:
            user_num = int(input('Please enter your phone number (Without dashes): '))
            user_num = str(user_num)
            return user_num
        except ValueError:
            print("")

def main(): #main function
    while True:
        try:
            directory = input("Directory you want to save the file to: ") #asks user for directory
            isdir = os.path.isdir(directory) #checks directory exists
        
            while isdir is True: #if directory exists, continues to asking filename
                try:
                    file_name = input('Filename: ') #asks user for filename
                    write_file = open(os.path.join(directory, file_name), 'w') #opens and creates a file using user input
                    write_file.write(name() + ', ' + address() + ', ' + phn_num()) #writes user input for name, address, and phone number into user created file
                    write_file.close() #closes the previously created file
                    print("")
                    print("Here's what's in the file:")
                    read_file = open(os.path.join(directory, file_name), 'r') #opens previously created file in order to read it

                    for line in read_file: #reads each line in the file
                        print("")
                        print(line)
                    read_file.close()
                    break
                except ValueError:
                    print("")
            break
        except FileNotFoundError: #Error to tell user if the directory or file couldn't be found
            print("")
            print("Directory/File couldn't be found")
            print("")
main()