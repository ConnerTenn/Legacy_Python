word = str(raw_input("Input Text: "))
curPos = 0
length_string = len(word)
aExists = True


for i in xrange(length_string):
    if word[i] == 'a':
        print i

# while curPos < lenth_string and aExists:
#     index = word[curPos:].find('a')
#     if index == -1:
#         aExists = False
#     curPos = index + 1
#     print index, curPos
