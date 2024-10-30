#ACRONYMS CREATOR...

phrase = input("Enter a phrase: ")
words = phrase.split()
print(words)

result = ""

for i in words:
    result+=i[0].upper()

print(result)    
