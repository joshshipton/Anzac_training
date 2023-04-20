n = input()
n = n.split()
num = int(n[0])
questions = int(n[1])

words = []
count = 0

dick = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}


for i in range(num):
    word = input()
    words.append(word)


for word in words:
    unique = set(word)
    hhh = []
    for letter in word:
        hhh.append(letter)
    if len(unique) != len(hhh):
        continue
    else:
        # check that it doesnt contain something after that letter in the alphabet
        
        hhh.sort()
        if dick[hhh[-1]] > questions:
            continue
        else:
            count += 1

print(count)






