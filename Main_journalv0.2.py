#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Journal: Munged by @uk_grl
import datetime
import os,sys
import base64

version="0.2 alpha"
filename=(str(datetime.date.today())+".log") # File format for journal entries.
CurrTime=str(datetime.datetime.now().time())
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def main_menu():
    menuOptions = {1:"New entry(n)",2:"Read(r)",3:"Quit"}
    clear_Screen()
    print("\n\t~~~~~~~~~~ Journal - Version:",version,"~~~~~~~~~~~~\n")
    for opt in menuOptions:
        print(opt,menuOptions[opt])
    choice=int(input("Choose 1-3: "))
    strChoice=choice
    if strChoice == 1:
        new_entry()
    elif strChoice == 2:
        file_ops("",'r')
    else:
        print("Exiting")
        exit()

def clear_Screen():
    #Clear screen depending on OS type
    if os.name == 'nt':
        os.system('cls')  # For Windows
    else:
        os.system('clear')  # For Linux/OS X


def base64_encode(temptext):
    text_byte=temptext.encode('ascii')
    base64_bytes = base64.b64encode(text_byte)
    base64_text = base64_bytes.decode('ascii')
    return base64_text

#Needs completing.
def base64_decode(temptext):
    text_byte=temptext.encode('ascii')
    base64_bytes = base64.b64encode(text_byte)
    base64_text = base64_bytes.decode('ascii')
    return base64_text


def new_entry():
    temptext=str(input("Type entry here:"))
    text = base64_encode(temptext)
    file_ops(text,'a')

def file_ops(text,op_type):
    print("\nFilename:",filename)
    if op_type == 'a':
        f = open(filename,op_type)
        f.write('\n' + CurrTime + ',' + text + '\n')
        filesize=os.path.getsize(filename)
        print("File size:",filesize,"bytes")
        f.close()
    else:
         try:
            f = open(filename, "r")
            print("\nTodays entries:", f.read())
         except FileNotFoundError:
            print("File not accessible or does not exist")
            #Need to keep the loop open until a quit.

# Command line options
if len(sys.argv) == 1:
    main_menu()
    exit()
elif sys.argv[1] =='-r':
    file_ops("", "r")
    exit()
elif sys.argv[1] =='-h' or sys.argv[1] =='--help':
    clear_Screen()
    print("\n~~~ Journal by @UK_GRL ~~~")
    print("Simple journal program that takes input, encodes it (Base64 atm) and then writes it to a file.")
    print("\nOptions:")
    print("-n : New or Additional entry")
    print("-r : Read current days journal")
    print("-h : Print this text... duh")
    print("Thats it...\n")
    exit()
elif sys.argv[1] =='-n':
    new_entry()
    exit()

