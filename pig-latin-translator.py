# Get sentence from user
sentence = input("Enter your sentence: ").strip().lower()

# split sentence into words
listOfWords = sentence.split()

#loop through words and convert to pig latin
listOfWordsPigLatin = []

for x in listOfWords :
    if x[0] in "aeiou" :\
        listOfWordsPigLatin.append(x + "yay")
    else :
        listOfWordsPigLatin.append(x[1:] + x[0] + "ay")

#Put new words together in a entence
output = " ".join(listOfWordsPigLatin)

#output the final string
print(output)
