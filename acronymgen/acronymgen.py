import random

f = open("words.txt")
words = []
for line in f:
    words.append(line.strip())
f.close()

userinput = input("whats acronym\n")

def generate(acronym):
    for i in acronym:
        begin = []
        for word in words:
            if word.lower().startswith(i.lower()): #if first letter matches
                begin.append(word.lower())
        index = random.randint(0,len(begin)-1)
        print(begin[index].capitalize(), end=" ")
    print("\n")

generate(userinput)
