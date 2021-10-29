import hashlib

flag = 0

Type = input("What type of hash would you like to decrypt?(md5, sha1, sha224, sha256, sha384, sha512): ")

Hash = input("Enter the hashed password: ")

Wordlist = input("Enter directory of the password file: ")


try:
    Passwords = open(Wordlist, "r")
except:
    print("File not found")
    exit()



if Type == "md5":
    for password in Passwords:
        encoded_word = password.encode("utf-8")
        decode = hashlib.md5(encoded_word.strip()).hexdigest()

        print(password)
        print(decode)
        print(Hash)

        if decode == Hash:
            print("Password Found!")
            print("The password is: " + password)
            flag = 1
            break

if Type == "sha1":
    for password in Passwords:
        encoded_word = password.encode("utf-8")
        decode = hashlib.sha1(encoded_word.strip()).hexdigest()

        print(password)
        print(decode)
        print(Hash)

        if decode == Hash:
            print("Password Found!")
            print("The password is: " + password)
            flag = 1
            break

if Type == "sha224":
    for password in Passwords:
        encoded_word = password.encode("utf-8")
        decode = hashlib.sha224(encoded_word.strip()).hexdigest()

        print(password)
        print(decode)
        print(Hash)

        if decode == Hash:
            print("Password Found!")
            print("The password is: " + password)
            flag = 1
            break

if Type == "sha256":
    for password in Passwords:
        encoded_word = password.encode("utf-8")
        decode = hashlib.sha256(encoded_word.strip()).hexdigest()

        print(password)
        print(decode)
        print(Hash)

        if decode == Hash:
            print("Password Found!")
            print("The password is: " + password)
            flag = 1
            break

if Type == "sha384":
    for password in Passwords:
        encoded_word = password.encode("utf-8")
        decode = hashlib.sha384(encoded_word.strip()).hexdigest()

        print(password)
        print(decode)
        print(Hash)

        if decode == Hash:
            print("Password Found!")
            print("The password is: " + password)
            flag = 1
            break

if Type == "sha512":
    for password in Passwords:
        encoded_word = password.encode("utf-8")
        decode = hashlib.sha512(encoded_word.strip()).hexdigest()

        print(password)
        print(decode)
        print(Hash)

        if decode == Hash:
            print("Password Found!")
            print("The password is: " + password)
            flag = 1
            break

else:
    print("Invalid Type")
    exit()

if flag == 0:
    print("Password not found in file :(")
    exit()