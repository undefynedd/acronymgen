import random

f = open("words.txt")
words = []
for line in f:
    words.append(line.strip())
f.close()

userinput = input("whats acronym\n")

def generate(acronym):
    list = []
    for char in acronym:
        possible = []
        
        for word in words:
            if word.lower().startswith(char.lower()): #if first letter matches
                possible.append(word.capitalize())

        w = random.choice(possible)
        list.append(w)   
    return list

print(" ".join(generate(userinput)))
