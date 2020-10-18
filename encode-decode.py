#ask user for messege
messege = input("Please input the messege: ").strip()

#Ask user for key
key = int(input("Please input the key provided: ").strip())

newMessege = []

#Go through each character of the messege
for letter in messege:
#if adding the key makes the value more than 122, go back to 32
    while (ord(letter) + key) > 122 :
        key = key - 90
    #convert each character to the correct ascii value and add the key
    newMessege.append(chr(ord(letter) + key))
print(''.join(newMessege))
