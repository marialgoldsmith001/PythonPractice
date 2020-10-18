initialInput = input("Press "e" to encode a messege, or "d" to decode a messege ").strip()

#TO ENCODE
if initialInput.lower() == "e" :
    #Ask user for messege and key
    messege = input("Please input the messege: ").strip()
    key = int(input("Please input the key provided: ").strip())

    encodedMessege = []

    #Go through each character of the messege and if ascii value is more than 122, go back to ascii #32
    for letter in messege:
        while (ord(letter) + key) > 122 :
            key = key - 90
        encodedMessege.append(chr(ord(letter) + key))

    print(''.join(encodedMessege))

#TO DECODE
elif initialInput.lower() == "d" :
    #Ask user encoded messege and key
    messege = input("Please type the encoded message: ").strip()
    key = int(input("Please input the key provided: ").strip())

    decodedMessege = []

    # Go through every letter in the encoded messege and if substracting the key from the ascii value of the letter is less than 32, add 90
    for letter in messege :
        while (ord(letter) - key) < 32 :
            key = key + 90
        decodedMessege.append(chr(ord(letter) - key))

    print(''.join(decodedMessege))
