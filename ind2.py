s = str(input("Enter the word: "))

i = len(s)
j = 0
if i % 2 == 1:
    print("Wrong word!")
else:
    st = s.join([s[x:x + 2][::-1] for x in range(0, len(s), 2)])
    print("Changed word: ", st.replace(s, ''))
