from random import randint

word = input("Please enter a word: ")
originalWord = word
scramble = int(input("How many times should the word be scrambled? "))
newWord = ""
print("Here is the word",word,"scrambled",scramble,"times: ")
for x in range(scramble):
    temp = list(originalWord)
    while len(temp) != 0:
      generatedIndexValue = randint(0, len(temp)-1)
      newWord += temp[generatedIndexValue]
      del temp[generatedIndexValue]
    temp=originalWord
    print(newWord)
    newWord=""
