# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. 
# If a string is longer than the other, append the additional letters onto the end of the merged string
def mergeString(word1, word2):
    list3 = []
    len_word1 = len(word1)
    len_word2 = len(word2)

    if len_word1 == len_word2:
        for i in range(len_word1):
            list3.append(word1[i])
            list3.append(word2[i])
        newString = "".join(list3)
    elif len_word1 < len_word2:
        rem = word2[len_word1:len_word2]
        for i in range(len_word1):
            list3.append(word1[i])
            list3.append(word2[i])
        list3.extend(rem)
        newString = "".join(list3)
    else:
        rem = word1[len_word2:len_word1]
        for i in range(len_word2):
            list3.append(word1[i])
            list3.append(word2[i])
        list3.extend(rem)
        newString = "".join(list3)
    return newString

#Execution starts here
try:
    print("Enter the word1")
    word1 = input()
    print("Enter the word2")
    word2 = input()
except ValueError as e:
    print("The inputs are not a valid strings")

result = mergeString(word1, word2)
print("The Merged String", result)

# Example 
# a b c   p q r
# a p b q c r

# a b   p q r s
# a p b q r s

# a b c d  p q
# a p b q c d