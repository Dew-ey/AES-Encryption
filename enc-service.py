import pyAesCrypt
import string
import random

def encrypt(key,source):
    output=source+".enc"
    pyAesCrypt.encryptFile(source,output,key)
    return output

def decrypt(key,source):
    dfile = source.split(".")
    output = dfile[0]+"dec."+dfile[1]
    pyAesCrypt.decryptFile(source,output,key)
    return

def fenc(key,source):
    return encrypt(key,source)

def toString(s):
    # initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in s:
        str1 += ele

    # return string
    return str1

def keygen():
    # Getting password length
    length = 8

    print('''Password Will Be Len 8''')

    characterList = ""

    # Getting character set for password

    characterList += string.ascii_letters

        
    # Adding digits to possible characters
    characterList += string.digits

    characterList += string.punctuation

    password = []

    for i in range(length):
        # Picking a random character from our 
        # character list
        randomchar = random.choice(characterList)
        # appending a random character to password
        password.append(randomchar)

    # printing password as a string
    print("The random key is " + "".join(password))
    return(toString(password))

# Temp key will be in the file
# in production model user will supply the file and nesscary password to decrypt after account verification
# right now test cases are built in
def main():
    print("\n**********************\n")
    oper = input("Please state if you wish to decrypt or encrypt a file (E for encrypt), (D for Decrypt): ")
    if oper == "E": 
        # Request for user key first 
        # use given test cases
        source = input("Give the name of the file you wish to encrypt (Must be in the same directory): ")
        print("File selected is: "+ source)
        print("Please generate a key to implement: ")
        key = keygen()
        print("Encrpyting")
        f = fenc(key,source)
        print(f)
    
    if oper == "D":
        source = input("Give the name of file to decrypt (Do not add the .enc just give filename): ")
        key = input("Please insert the files key: ")
        f = source + ".enc"
        decrypt(key,f)

main() 