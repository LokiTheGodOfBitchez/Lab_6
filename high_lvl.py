word1, word2 = input("Enter two words: ").split()
for ch in word1:
    if ch in word2:
        print("Yes", end=" ")
    else:
        print("No", end=" ")
