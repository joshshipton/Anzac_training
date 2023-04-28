# Emilio’s team is competing at the South Pacific ICPC Divisional Finals. They have read the problems and immediately know all the solutions.
# Emilio finds simply winning the contest boring. Instead, he has convinced
# his team to spell out a word with their submissions. He has put together a
# list of n words that he would like to spell.
# Each question in the contest is labelled with an uppercase letter. The
# first question is labelled “A”, the second is labelled “B”, and so on. A word
# is spelled by solving questions in a specific order. For example, if Emilio’s
# team wants to spell LEAK, the team first solves problem L, then problem E, then problem A, and finally problem
# K. The team may only solve each problem once, so they may not spell words with duplicated letters (for example,
# they cannot spell EMILIO). Which words can Emilio’s team spell?
# Input
# The first line contains two integers n (1 ≤ n ≤ 100), which is the number of words in Emilio’s list, and m (1 ≤
# m ≤ 15), which is the number of questions in the contest.
# The next n lines describe the words. Each of these lines contains a word with at least 1 and at most 15
# uppercase letters. All the words are distinct.


n = input()
n = n.split()
num = int(n[0])
questions = int(n[1])

words = []
count = 0

dick = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13,
        'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}


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

# solved
