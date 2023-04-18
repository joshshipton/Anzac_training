# Annabelle’s team loves big integers. Currently, she has a number and
# would like to make it bigger. She will do this by taking a digit and inserting
# it somewhere into her original number.
# For example, if her original number is 7853 and she is inserting a 6, then
# she can make the following numbers: 67853, 76853, 78653, 78563, 78536.
# The largest of these is 78653, so she will choose this.
# Given Annabelle’s original number and the digit she wishes to insert,
# what is the largest number she can make?

# get the biggest number in the string and append it to the front 

n = str(input())
n = n.split()
insert = n[0]
original = n[1]
to_insert = -1


for char in original:
    print(char,insert)
    if int(char) < int(insert):
        to_insert = original.index(char)
        print('insert at' + str(to_insert))

        break
if to_insert != -1: 
    print(original[0:to_insert] + insert + original[to_insert:])

else:
    print(original + insert)
            

# input, expected, got

# 6 7853
# 78653
# 78653

# 1 111111111
# 1111111111
# 1111111111

# 9 123456789012345678901234567890
# 9123456789012345678901234567890
# 9123456789012345678901234567890

# 6 9876789
# 98767896
# 96876789