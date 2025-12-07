sentence = input ("enter the sentence ")
slice = sentence.split()
Ndic ={}
for word in slice :
    word = word.upper()
    if word in Ndic:
        Ndic[word] +=1
    else:
        Ndic[word] = 1
print(Ndic)  